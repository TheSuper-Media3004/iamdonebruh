from fastapi import FastAPI
from pydantic import BaseModel #validation bs -- literally 4 hrs wtf
from rag import rag_chain

app = FastAPI()


chain = rag_chain()

class Question(BaseModel):
    question : str

@app.post("/ask")
async def ask_question(question:Question):
    result = chain.invoke(question.question)
    sources = []

    for doc in result["source_documents"]:
        sources.append({
            "source":doc.metadata.get("source"),
            "pages":doc.metadata.get("page")
        })
    return {
        "result":result["result"],
        "sources":sources
    }
            
#---last edited on 15-03-2026
