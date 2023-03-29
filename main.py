import config.config as config
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)

while True:
    print("Enter 'exit' to quit.")
    query = input("Prompt: ")

    if query.lower() == 'exit':
        exit()

    response = index.query(query)
    print(response)
