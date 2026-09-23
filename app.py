import streamlit as st
from pathlib import Path
from src.database import init_db, log_question
from src.utils import save_uploaded_file
from src.rag_chain import build_rag, ask_rag
from src.summarizer import summarize_file
from src.risk_analyzer import analyze_risk
from dashboard.charts import show_dashboard

st.set_page_config(page_title="AI Legal Document Assistant", page_icon="⚖️", layout="wide")
init_db()
st.title("⚖️ AI Legal Document Assistant")
st.caption("RAG + GenAI assistant for understanding uploaded legal documents. Not a substitute for qualified legal advice.")

tabs = st.tabs(["Legal AI Chat", "Documents", "Summary", "Risk Analysis", "Dashboard"])

with tabs[0]:
    q = st.text_area("Ask a question about your uploaded legal documents")
    if st.button("Ask Legal AI", type="primary") and q.strip():
        try:
            with st.spinner("Searching documents and generating answer..."):
                answer, sources = ask_rag(q)
            st.markdown(answer)
            st.subheader("Sources")
            for s in sources: st.write(f"{s['source']} | page {s['page'] or 'N/A'} | similarity distance {s['score']:.4f}")
            log_question(q, sum(s["score"] for s in sources)/len(sources))
        except Exception as e: st.error(str(e))

with tabs[1]:
    files = st.file_uploader("Upload PDF, DOCX or TXT", type=["pdf", "docx", "txt"], accept_multiple_files=True)
    if st.button("Save Documents") and files:
        for f in files: save_uploaded_file(f)
        st.success("Documents saved. Click Build / Refresh RAG Index.")
    if st.button("Build / Refresh RAG Index"):
        try:
            with st.spinner("Creating chunks, embeddings and FAISS index..."): build_rag()
            st.success("RAG index created successfully.")
        except Exception as e: st.error(str(e))
    st.write("Current documents:")
    for p in Path("data/documents").glob("*"): st.write("•", p.name)

with tabs[2]:
    f = st.file_uploader("Select a document to summarize", type=["pdf", "docx", "txt"], key="summary")
    if f and st.button("Generate Summary"):
        path = save_uploaded_file(f)
        try: st.markdown(summarize_file(path))
        except Exception as e: st.error(str(e))

with tabs[3]:
    f = st.file_uploader("Select a document for review flags", type=["pdf", "docx", "txt"], key="risk")
    if f and st.button("Analyze Review Areas"):
        path = save_uploaded_file(f)
        try: st.markdown(analyze_risk(path))
        except Exception as e: st.error(str(e))

with tabs[4]:
    show_dashboard(st)
