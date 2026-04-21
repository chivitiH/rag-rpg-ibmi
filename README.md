# 🧠 RAG IBM i RPG Assistant (Local LLM)

A Retrieval-Augmented Generation (RAG) system to query IBM i RPG documentation using a local LLM (Ollama + GPT-OSS-20B).

---

## 🚀 Features

- 📄 PDF ingestion (RPG documentation)
- 🧠 Semantic search with FAISS
- ⚡ GPU embeddings (SentenceTransformers)
- 🤖 Local LLM (Ollama – GPT-OSS-20B)
- 🔍 Context-grounded answers
- 📚 Source attribution

---

## 🏗️ Architecture

PDF → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer

---

## 🧪 Example

**Question**
How are variables declared in RPG IV free format?

**Answer (generated)**
- Explanation based on retrieved documents  
- RPG code example  
- References to source PDFs  

---

## ⚙️ Setup

git clone https://github.com/chivitiH/rag-rpg-ibmi.git  
cd rag-rpg-ibmi  

python -m venv venv  
source venv/bin/activate  

pip install -r requirements.txt  

curl -fsSL https://ollama.com/install.sh | sh  
ollama pull gpt-oss:20b  

python ingest.py  
python rag.py  

---

## 📁 Project Structure

rag-rpg-ibmi/  

├── data/           # Your PDFs (not included)  
├── db/             # Vector database (generated)  
├── ingest.py       # PDF → embeddings → FAISS  
├── rag.py          # Retrieval + LLM  
├── requirements.txt  
└── README.md  

---

## 🧠 Technical Highlights

- Fully local RAG pipeline (no API required)  
- FAISS vector search  
- Transformer embeddings (sentence-transformers)  
- LLM integration via Ollama  
- Clean modular design  

---

## ⚠️ Data

PDF files are not included.  

Add your own documents in `data/` and run:

python ingest.py  

---

## 🎯 Use Cases

- IBM i / RPG developers  
- Legacy documentation search  
- Code assistance from internal knowledge base  

---

## 👤 Author

Yoni  
Machine Learning Engineer  
https://github.com/chivitiH  

