from langchain.embeddings import VertexAIEmbeddings

def batch_get_embeddings(text_list: list[str], task: str = "RETRIEVAL_QUERY") -> list[list[float]]:
    # Initialize the VertexAIEmbeddings from LangChain
    embedding_model = VertexAIEmbeddings(model="text-embedding-004")
    token_factor = 4
    token_limit = 12000

    batch_token_count = 0
    batch_inputs: list[str] = []
    embeddings: list[list[float]] = []

    for text in text_list:
        # Check if text chunk exceeds token limit
        text_token_count = len(text) / token_factor
        if text_token_count > token_limit:
            raise ValueError(f"Single text chunk exceeds token limit: {text_token_count} > {token_limit}")

        if batch_token_count + text_token_count > token_limit:
            # Process current batch
            embeddings += embedding_model.embed_documents(batch_inputs)
            batch_token_count = 0
            batch_inputs = []

        batch_inputs.append(text)
        batch_token_count += text_token_count

    # Process any remaining text in the final batch
    if batch_inputs:
        embeddings += embedding_model.embed_documents(batch_inputs)

    return embeddings
