from app.rag import rag_chain

qa = rag_chain()

result = qa.invoke({"query": "Who is narendra modi"})


print(result["result"])


for doc in result["source_documents"]:
    print(doc.metadata)
