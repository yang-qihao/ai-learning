import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()          # 这一句：把 .env 里的内容读进来

client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),   # 从"环境"里取 key，而不是写死
    base_url="https://ws-1ue1906kn7u4jwic.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[{"role": "user", "content": "你好，用一句话介绍你自己"}],
)

print(response.choices[0].message.content)