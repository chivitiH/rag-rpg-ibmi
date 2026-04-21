import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_PATH = "data/"
DB_PATH = "db/"

def load_docs():
    docs = []
    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            docs.extend(loader.load())
    return docs

def main():
    print("📄 Loading PDFs...")
    docs = load_docs()

    print("✂️ Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(docs)

    print(f"Chunks: {len(chunks)}")

    print("🧠 Creating embeddings...")
    embeddings = HuggingFaceEmbeddings()

    print("💾 Storing in FAISS...")
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_PATH)

    print("✅ Done!")

if __name__ == "__main__":
    main()
