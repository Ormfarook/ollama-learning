# 1. ingest PDF files
from langchain_unstructured import UnstructuredLoader
# from langchain_community.document_loaders import OnlinePDFLoader

doc_path = "./data/BOI.pdf"
model= "llama3.2"

if doc_path: 
    loader= UnstructuredLoader(file_path = doc_path)
    data = loader.load()
    print("done loading....")
else:
    print("Something wrong with the path. Upload a new one")

content = data[0].page_content
print(content[:200])
# 2. Extract text from PDF files and split into small chunks
# 3. Send the chunkks to the embedding model
# 4. Save the embeddings to a vector database
# 5. Perform similarity search on the vector database to find similar chunks with the embedded query 
# 6. retrieve the similar chunk present them to the user



