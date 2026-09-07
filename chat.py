import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()          # 这一句：把 .env 里的内容读进来

client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),   # 从"环境"里取 key，而不是写死
    base_url="https://ws-1ue1906kn7u4jwic.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)
messages=[
        {"role": "system", "content": "你是一个友好的助手，回答要简短。"}
    ]

print("开始对话！输入 quit 退出。")
while True:
    user_input = input("你：")
    if user_input == "quit":
        print("bye")
        break
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
    model="qwen-plus",
    messages=messages,
   )
    reply = response.choices[0].message.content
    print("AI:", reply)
    messages.append({"role": "assistant", "content": reply})