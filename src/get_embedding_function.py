from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings


def get_embedding_function():
    """
    embeddings = BedrockEmbeddings(
        credentials_profile_name="default"
        )
    """
    embeddings = OllamaEmbeddings(base_url="http://192.168.0.18:11434", model="llama3")
    
    return embeddings
