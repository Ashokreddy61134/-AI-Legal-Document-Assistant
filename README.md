# AI Legal Document Assistant RAG

A Streamlit RAG application for uploading PDF, DOCX and TXT legal documents, retrieving relevant passages with FAISS and HuggingFace embeddings, answering questions with Groq GenAI, generating summaries, identifying review areas, and tracking usage in SQLite.

## Architecture

Legal Document -> Loader -> Text Extraction -> Chunking -> Embeddings -> FAISS

Question -> Query Embedding -> Similarity Search -> Context -> Groq LLM -> Answer + Sources -> SQLite Analytics -> Dashboard

## Windows / VS Code Setup

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Put your Groq API key in `.env`:

```text
GROQ_API_KEY=your_key_here
```

Run:

```powershell
streamlit run app.py
```

Open the Streamlit URL shown in the terminal, upload documents, save them, build the RAG index, and ask questions.

## Notes
- The first HuggingFace embedding run may download the model.
- Never commit `.env` or API keys.
- This application is for document understanding and review support, not legal advice.
