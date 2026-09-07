import os
import chromadb
from dotenv import load_dotenv
from openai import OpenAI
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

load_dotenv()
embedding_function = OpenAIEmbeddingFunction(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    api_base="https://ws-1ue1906kn7u4jwic.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
    model_name="qwen3.7-text-embedding",
)
chorma = chromadb.PersistentClient(path="./rag_db")

col = chorma.get_or_create_collection(
    name="knowledge",
    embedding_function=embedding_function,#用上面的方法 就是使用阿里云的embed模型
)
#存入文档
docs = [
    "苹果是一种常见的水果，甜甜的很好吃。",
    "香蕉是黄色的，剥皮吃的水果。",
    "狗是人类忠实的伙伴，会看家护院。",
]
col.add(
    ids=["a", "b", "c"],
    documents=docs,
)
results = col.query(
    query_texts=["我想吃水果，有什么甜的？"],
    n_results=2,
)
print("命中的段落:")
for doc in results["documents"][0]:
    print("  -", doc)