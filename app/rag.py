import os

from dotenv import load_dotenv
from langchain_classic.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_classic.chains.retrieval_qa.base import RetrievalQA



load_dotenv()

def rag_chain():

    llm = OllamaLLM(
        model="mistral",
        base_url=os.getenv("BASE_URL")
    )
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    
    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )
    retriver = vectordb.as_retriever(search_kwargs={"k":3})
    template = """
Use the only context below to answer the question
if the answer is not in context say:
"sorry the provided context isnt sufficient to apply an answer"

Context:
{context}

Question:
{question}

Answer:
    """
    prompt = PromptTemplate(
        template=template,
        input_variables=["context","question"]
    )
    
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriver,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    return chain