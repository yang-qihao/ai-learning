import os
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://ws-1ue1906kn7u4jwic.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "你好，世界！"}

@app.get("/chat")
def chat(q:str):
    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[{"role":"user","content":q},]
    )
    reply = response.choices[0].message.content
    return {"reply": reply}
