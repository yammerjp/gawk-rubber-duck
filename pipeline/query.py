# reload.py
from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("関数を変数にし、間接的に呼び出す方法を教えてください")
print(response)
