import subprocess
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# =========================
# CONFIG
# =========================
DB_PATH = "db/"
MODEL_NAME = "gpt-oss:20b"


# =========================
# LOAD VECTOR DB
# =========================
def load_db():
    print("🔄 Loading vector DB...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    db = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    print("✅ DB loaded")
    return db


# =========================
# CALL OLLAMA
# =========================
def ask_ollama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", MODEL_NAME],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        output = result.stdout.decode()

        # 🔥 Nettoyage complet du reasoning parasite
        if "Thinking..." in output:
            output = output.split("Thinking...")[-1]

        if "...done thinking." in output:
            output = output.replace("...done thinking.", "")

        if "We need to" in output:
            # coupe tout avant la vraie réponse si le modèle bavarde
            if "##" in output:
                output = "##" + output.split("##", 1)[1]

        return output.strip()

    except Exception as e:
        return f"❌ Ollama error: {e}"


# =========================
# FORMAT SOURCES
# =========================
def format_sources(docs):
    sources = list(set([
        doc.metadata.get("source", "unknown")
        for doc in docs
    ]))
    return [s.split("/")[-1] for s in sources]


# =========================
# MAIN
# =========================
def main():
    print("🚀 Script started")

    db = load_db()
    retriever = db.as_retriever(search_kwargs={"k": 5})

    print("\n💬 Ask your question (type 'exit' to quit)\n")

    while True:
        query = input(">>> ")

        if query.lower() == "exit":
            print("👋 Bye")
            break

        print("🔎 Retrieving context...")
        docs = retriever.invoke(query)

        context = "\n\n".join([doc.page_content for doc in docs])

        # =========================
        # PROMPT PRO++
        # =========================
        prompt = f"""
You are a senior IBM i RPG expert.

Answer STRICTLY using the provided context.
Do NOT add any external knowledge.
If something is not explicitly written in the context, say "I don't know".

STRICT RULES:
- Do NOT explain your reasoning
- Do NOT include thoughts like "Thinking" or "We need to"
- Only output the final answer
- Be concise and professional
- If unsure, say "I don't know"

IMPORTANT:
- Use ONLY RPG IV free format syntax
- Do NOT mix with CL or fixed format

FORMAT:

## Explanation
(clear explanation)

## Example (RPG Free Format)
[RPG CODE HERE]

## References
(list document names from context)

Context:
{context}

Question:
{query}
"""

        # =========================
        # GENERATION
        # =========================
        print("🤖 Generating answer...\n")
        response = ask_ollama(prompt)

        # =========================
        # OUTPUT
        # =========================
        print("🧠 Answer:\n")
        print(response)

        print("\n📚 Sources:")
        for s in format_sources(docs):
            print("-", s)

        print("\n" + "="*60 + "\n")


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    main()