from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = DirectoryLoader(
    "data/docs",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 400,
    chunk_overlap = 50
)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

docs = splitter.split_documents(documents)
vectordb = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="chroma_db"   
)

vectordb.persist()
print("The documents have been indexed")
