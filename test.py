import pinecone

pinecone.init(
    api_key="b6516b9c-690e-4233-9bfa-5d3ec3c95a7e",
    environment="us-east1-gcp"
)

index = pinecone.Index("youtube-search1")
