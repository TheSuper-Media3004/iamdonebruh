from app.rag import rag_chain

qa = rag_chain()

result = qa.invoke({"query": "What is machine learning?"})

print("\nANSWER:\n")
print(result["result"])

print("\nSOURCES:\n")

for doc in result["source_documents"]:
    print(doc.metadata)