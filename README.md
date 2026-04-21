# 🧠 RAG IBM i RPG Assistant (Local LLM)

A Retrieval-Augmented Generation (RAG) system for querying IBM i RPG documentation using a local LLM (Ollama + GPT-OSS-20B).

---

## 🚀 Features

- 📄 PDF ingestion (RPG documentation)
- 🧠 Semantic search with FAISS
- ⚡ GPU embeddings (SentenceTransformers)
- 🤖 Local LLM (Ollama – GPT-OSS-20B)
- 🔍 Context-based answers (no hallucinations mode)
- 📚 Source attribution

---

## 🏗️ Architecture

PDF → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer

---

## 🧪 Example

**Question:**
> How are variables declared in RPG free format?

**Answer:**
- Explanation based on documentation
- RPG code example
- Sources from PDFs

---

## ⚙️ Setup

### 1. Clone repo

git clone https://github.com/chivitiH/rag-rpg-ibmi.git
cd rag-rpg-ibmi

---

### 2. Create environment

python -m venv venv
source venv/bin/activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Install Ollama

curl -fsSL https://ollama.com/install.sh | sh

---

### 5. Download model

ollama pull gpt-oss:20b

---

### 6. Run ingestion

python ingest.py

---

### 7. Run RAG

python rag.py

---

## 📁 Project Structure

rag-rpg-ibmi/

├── data/           # PDF documents  
├── db/             # FAISS vector database  
├── ingest.py       # Document processing  
├── rag.py          # RAG pipeline  
├── requirements.txt  
└── README.md  

---

## 🧠 Technical Highlights

- Local-first AI (no API required)
- GPU acceleration (embeddings)
- Retrieval-based accuracy
- Modular architecture

---

## ⚠️ Limitations

- Depends on document quality
- Local LLM less accurate than GPT-4
- Requires GPU for best performance

---

## 🎯 Use Case

- IBM i / RPG developers
- Legacy system documentation search
- Code assistance from internal docs

---

## 👤 Author

Yoni  
Machine Learning Engineer (certified)  
GitHub: https://github.com/chivitiH


## ⚠️ Data

PDF files are not included.  
Add your own documents in the `data/` folder and run:

python ingest.py

