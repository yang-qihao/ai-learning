import os
from dotenv import load_dotenv
from openai import OpenAI
import math

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://ws-1ue1906kn7u4jwic.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

def cosine_similarity(a, b): #余弦相似度
    dot = sum(x * y for x, y in zip(a, b))      # 1. 对应位置相乘再求和
    norm_a = math.sqrt(sum(x * x for x in a))   # 2. a 的长度
    norm_b = math.sqrt(sum(x * x for x in b))   # 3. b 的长度
    return dot / (norm_a * norm_b)              # 4. 相除

resp = client.embeddings.create(
    model="qwen3.7-text-embedding",
    input=["苹果", "香蕉", "狗"],
)
v_apple = resp.data[0].embedding
v_banana = resp.data[1].embedding
v_dog = resp.data[2].embedding

print("苹果 vs 香蕉:", cosine_similarity(v_apple, v_banana))
print("苹果 vs 狗:", cosine_similarity(v_apple, v_dog))