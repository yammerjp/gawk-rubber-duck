import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('dist/text').load_data()
index = VectorStoreIndex.from_documents(documents)

index.storage_context.persist()
