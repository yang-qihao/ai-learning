import os
import json
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def get_weather(city):
    return {"city": city, "weather" : "晴天" , "temp":"28度"}
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://ws-1ue1906kn7u4jwic.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)
tools = [
    {
        "type" : "function",
        "function" : {
            "name":"get_weather" ,#工具名
             "description":"查询某地的天气",
             "parameters":{ "type":"object",
                   "properties":{
                     "city":{"type":"string","description":"城市名"},
                                },
                "required":["city"],
                   },
                },
    },
]
messages = [{"role": "user", "content": "北京今天天气怎么样？"}]
response = client.chat.completions.create(
    model="qwen-plus",
    messages=messages,
    tools=tools,               # 关键：把工具箱传进去
)
message = response.choices[0].message
# print("AI 想调用的工具:", message.tool_calls)
# print("AI 想调用的工具:", message)
if message.tool_calls:
    tool_call = message.tool_calls[0]                       # 取第一个工具请求
    tool_name = tool_call.function.name                     # 工具名
    args = json.loads(tool_call.function.arguments)         # 把参数字符串转成字典
    city = args["city"]                                     # 取出 city
    result = get_weather(city)                              # 真去"执行“
    # 5. 把AI的工具请求 + 执行结果，一起追加进对话历史
    messages.append(message)                                # 先把AI的"工具请求"记进去
    messages.append({                                       # 再把"结果"记进去
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(result, ensure_ascii=False),  # 结果转成JSON字符串
    })
    # 6. 再调一次AI，让它根据结果回答
    response2 = client.chat.completions.create(
        model="qwen-plus",
        messages=messages,
    )
    print("AI回答:", response2.choices[0].message.content)
else:
    print("AI直接回答:", message.content)