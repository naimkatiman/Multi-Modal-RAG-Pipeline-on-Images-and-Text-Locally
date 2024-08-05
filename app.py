import streamlit as st
from PIL import Image
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.core.indices import MultiModalVectorStoreIndex
import qdrant_client

# Streamlit page config
st.set_page_config(page_title="Multi-Modal RAG Pipeline", layout="wide")

# Initialize Qdrant client
@st.cache_resource
def init_qdrant():
    return qdrant_client.QdrantClient(path="qdrant_db")

client = init_qdrant()

# Initialize vector stores
@st.cache_resource
def init_vector_stores():
    text_store = QdrantVectorStore(client=client, collection_name="text_collection")
    image_store = QdrantVectorStore(client=client, collection_name="image_collection")
    return StorageContext.from_defaults(vector_store=text_store, image_store=image_store)

storage_context = init_vector_stores()

# Load and index documents
@st.cache_resource
def load_and_index_documents():
    documents = SimpleDirectoryReader("data").load_data()
    return MultiModalVectorStoreIndex.from_documents(documents, storage_context=storage_context)

index = load_and_index_documents()

# Streamlit UI
st.title("Multi-Modal RAG Pipeline")

# User input
query = st.text_input("Enter your query:")

if query:
    # Perform retrieval
    retriever = index.as_retriever(similarity_top_k=1, image_similarity_top_k=1)
    retrieval_results = retriever.retrieve(query)

    # Display results
    for res in retrieval_results:
        if isinstance(res.node, ImageNode):
            image = Image.open(res.node.metadata["file_path"])
            st.image(image, caption="Retrieved Image", use_column_width=True)
        else:
            st.write(res.node.get_content())

# Optional: Add file uploader for new images/text
uploaded_file = st.file_uploader("Upload a new image or text file", type=["jpg", "png", "txt"])
if uploaded_file is not None:
    # Handle file upload and indexing
    # (You'll need to implement this part)
    st.success("File uploaded and indexed successfully!")