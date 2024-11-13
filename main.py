from functools import wraps

def batch_job(n):
    """Decorator to process documents in batches of size n."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            docs = kwargs.get("docs", args[2] if len(args) > 2 else [])
            for i in range(0, len(docs), n):
                batch = docs[i:i + n]
                func(*args[:2], docs=batch)
        return wrapper
    return decorator

@batch_job(n=5)
def add_documents(v: VertexLlM, collection: Collection, docs: list[Document]):
    new_docs = set()
    for doc in docs:  # only add new docs to speed up process
        res = collection.get(ids=doc.metadata["id"])
        if len(res["ids"]) == 0:
            new_docs.add(doc)
    if len(new_docs) == 0:
        return
    collection.add(
        documents=[d.page_content for d in new_docs],
        embeddings=[v.get_embedding(d.page_content) for d in new_docs],
        metadatas=[d.metadata for d in new_docs],
        ids=[d.metadata["id"] for d in new_docs]
    )
