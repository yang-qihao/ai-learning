import os
import chromadb
from dotenv import load_dotenv
from openai import OpenAI
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://ws-1ue1906kn7u4jwic.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)
embedding_function = OpenAIEmbeddingFunction(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    api_base="https://ws-1ue1906kn7u4jwic.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    model_name="qwen3.7-text-embedding",
)
chroma = chromadb.PersistentClient(path="./rag_db")
col = chroma.get_or_create_collection(
    name="knowledge",
    embedding_function=embedding_function,
)

def speak_with_context(question):
    # 1. 检索：找到和最相关的 2 段
    results = col.query(query_texts=[question], n_results=2)
    found_docs = results["documents"][0]
    # 2. 把这几段拼成"资料"
    context = "\n".join(found_docs)
    # 3. 拼 prompt，喂给 LLM
    prompt = f"""请根据以下资料回答问题。如果资料里没有答案，就说"不知道"。
【资料】
{context}
【问题】
{question}
"""
    response = client.chat.completions.create(
        model="qwen-plus",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
# 测试
print("问: 我想吃水果，有什么甜的？")
print("答:", speak_with_context("我想吃水果，有什么甜的？"))
print()
print("问: 今天股票涨了吗？")
print("答:", speak_with_context("今天股票涨了吗？"))