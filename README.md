# ⚖️ LexAI Document Assistant

## AI-Powered Legal & General Document Intelligence Platform

LexAI Document Assistant is an AI-powered document intelligence application built using **Generative AI, Retrieval-Augmented Generation (RAG), LangChain, Groq LLM, HuggingFace Embeddings, FAISS, SQLite, and Streamlit**.

The application allows users to upload PDF, DOCX, and TXT documents and interact with them using natural language.

Users can:

- Ask questions about documents
- Search document content
- Generate summaries
- Analyze potentially important clauses
- Explore specific clauses
- Compare two documents
- View source and page references
- Maintain analysis history
- View interactive analytics
- Export analysis results

---

# 📌 Table of Contents

1. [Project Overview](#-project-overview)
2. [Problem Statement](#-problem-statement)
3. [Project Objective](#-project-objective)
4. [Solution](#-solution)
5. [Key Features](#-key-features)
6. [How RAG Works](#-how-rag-works)
7. [System Architecture](#-system-architecture)
8. [Project Workflow](#-project-workflow)
9. [Project Folder Structure](#-project-folder-structure)
10. [Folder and File Explanation](#-folder-and-file-explanation)
11. [Technology Stack](#-technology-stack)
12. [Installation](#-installation)
13. [Environment Configuration](#-environment-configuration)
14. [Running the Application](#-running-the-application)
15. [Using the Application](#-using-the-application)
16. [Document Processing](#-document-processing)
17. [RAG Pipeline](#-rag-pipeline)
18. [Risk Analysis](#-risk-analysis)
19. [Document Comparison](#-document-comparison)
20. [Analytics Dashboard](#-analytics-dashboard)
21. [Database](#-database)
22. [Vector Store](#-vector-store)
23. [Testing](#-testing)
24. [Troubleshooting](#-troubleshooting)
25. [Security](#-security)
26. [Future Enhancements](#-future-enhancements)
27. [Disclaimer](#-disclaimer)
28. [Author](#-author)
29. [License](#-license)

---

# 🚀 Project Overview

Large documents such as contracts, agreements, policies, reports, terms and conditions, and business documents often contain a large amount of information.

Finding a particular clause or answering a specific question manually can take considerable time.

LexAI Document Assistant solves this problem by combining:

- Document processing
- Natural Language Processing
- Vector embeddings
- Semantic search
- Retrieval-Augmented Generation
- Large Language Models
- Interactive dashboards

Instead of sending the entire document directly to the LLM, the application first searches the document for relevant information.

The relevant information is then provided to the LLM as context.

This makes the generated response more closely grounded in the uploaded document.

---

# 🎯 Problem Statement

Traditional document analysis has several challenges:

- Large documents are difficult to read manually.
- Important clauses can be difficult to locate.
- Searching by exact keywords may miss semantically related information.
- Comparing multiple documents can be time-consuming.
- Users may need summaries before reviewing the complete document.
- Important clauses may require additional review.
- Previous analysis may not be easily tracked.

LexAI provides a single interface for these document intelligence tasks.

---

# 💡 Solution

LexAI implements a RAG-based document intelligence pipeline.

```text
Upload Document
      ↓
Extract Text
      ↓
Clean Text
      ↓
Split Into Chunks
      ↓
Generate Embeddings
      ↓
Store in FAISS
      ↓
User Question
      ↓
Semantic Search
      ↓
Retrieve Relevant Chunks
      ↓
Build Prompt
      ↓
Groq LLM
      ↓
Generate Answer
      ↓
Show Source + Page
      ↓
Save History
🎯 Project Objectives
The project aims to:
1. Build a practical Generative AI application.
2. Implement Retrieval-Augmented Generation.
3. Process multiple document formats.
4. Enable document-specific question answering.
5. Generate document summaries.
6. Identify potentially important clauses.
7. Provide structured risk analysis.
8. Compare two documents.
9. Provide source and page references.
10. Store user analysis history.
11. Provide interactive analytics.
12. Create a modular and maintainable architecture.
✨ Key Features
📄 Document Upload
Supported document formats:
PDF
DOCX
TXT
Uploaded documents are processed automatically.
💬 AI Document Chat
Users can ask questions about a selected document.
Example:
What is the termination period?
Other examples:
Who are the parties involved?

What are the payment terms?

What are the main obligations?

What happens if the agreement is terminated?

What is the governing law?

What are the confidentiality requirements?
The application retrieves relevant document sections before generating the answer.
🔍 Document Search
Users can search document content using keywords or phrases.
Examples:
termination
payment
liability
confidentiality
indemnity
renewal
jurisdiction
insurance
The application displays matching content and page information.
📝 Document Summarization
The application can generate structured summaries.
The summary can contain:
- Parties
- Purpose
- Obligations
- Payment
- Contract duration
- Termination
- Confidentiality
- Intellectual Property
- Liability
- Indemnity
- Dispute Resolution
- Governing Law
- Deadlines
- Important provisions
⚠️ Risk Analysis
The risk analysis module identifies potentially important provisions that may require further review.
Risk levels:
🔴 High
🟠 Medium
🟢 Low
Potential areas include:
- Unlimited liability
- Broad indemnification
- Automatic renewal
- Restrictive termination conditions
- Payment penalties
- Intellectual property provisions
- Confidentiality obligations
- Jurisdiction requirements
- Ambiguous obligations
- Contract penalties
Example:
Overall Risk: Medium

High Risk: 2
Medium Risk: 4
Low Risk: 3
Each finding may contain:
Clause
Risk Level
Reason
Recommendation
Page
📋 Clause Explorer
The Clause Explorer allows users to investigate individual clauses.
Examples:
Termination
Payment
Confidentiality
Liability
Indemnity
Intellectual Property
Renewal
Governing Law
Dispute Resolution
Example:
Find and explain the termination clause.
The system retrieves relevant content and generates an explanation.
🔄 Document Comparison
Two documents can be compared.
The comparison can identify differences in:
- Parties
- Payment
- Duration
- Termination
- Liability
- Confidentiality
- Obligations
- Intellectual Property
- Jurisdiction
- Other provisions
Workflow:
Document A
     +
Document B
     ↓
Comparison Module
     ↓
Extract Differences
     ↓
Generate Structured Comparison
📊 Analytics Dashboard
The application includes an interactive analytics dashboard.
Dashboard KPIs
Total Documents
Total Questions
Total Summaries
Total Risk Analyses
Charts
Risk Distribution
Risk Findings by Document
Risk Analysis Trend
Questions by Document
Plotly is used for interactive visualization.
🕘 History
The application stores previous activities.
Examples:
- Questions
- Answers
- Summaries
- Risk analyses
- Document information
- Analysis timestamps
SQLite is used for local persistence.
⚙️ Settings
The settings page provides information about the current application configuration.
Examples:
LLM Provider
LLM Model
Embedding Model
Vector Store
Database
Chunk Size
Chunk Overlap
Top-K
🧠 How RAG Works
RAG stands for:
Retrieval-Augmented Generation

Instead of asking the LLM to answer from its general knowledge, LexAI retrieves relevant information from the uploaded document first.
Step 1: Upload Document
The user uploads:
contract.pdf
Step 2: Extract Text
The document loader extracts text.
For PDF:
PDF
 ↓
PyPDF
 ↓
Page Text
For DOCX:
DOCX
 ↓
python-docx
 ↓
Paragraph Text
For TXT:
TXT
 ↓
Python File Reader
 ↓
Text
Step 3: Clean Text
Extracted text may contain:
- Extra spaces
- Unnecessary line breaks
- Formatting problems
The text cleaner normalizes the content.
Step 4: Text Chunking
Large text is divided into smaller chunks.
Example:
Large Document
       ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
Chunk 5
Configured using:
CHUNK_SIZE
CHUNK_OVERLAP
Step 5: Generate Embeddings
Each chunk is converted into a numerical vector.
Embedding model:
sentence-transformers/all-MiniLM-L6-v2
Example:
"Termination requires 30 days notice."

              ↓

        Embedding Model

              ↓

[0.12, -0.34, 0.52, ...]
Step 6: Store Embeddings
Embeddings are stored in:
FAISS
FAISS enables efficient similarity search.
Step 7: User Asks a Question
Example:
What is the termination period?
The question is converted into an embedding.
Step 8: Similarity Search
FAISS compares the question embedding with stored document embeddings.
The most relevant chunks are retrieved.
Step 9: Build Context
The retrieved document chunks are added to the prompt.
Example:
Question:
What is the termination period?

Context:
The agreement may be terminated by either party
with thirty days written notice.
Step 10: Groq LLM
The context and question are sent to the configured Groq model.
The LLM generates the answer.
Step 11: Display Result
The application displays:
Answer
Source
Page
Relevant Context
🏗️ System Architecture
                       USER
                         │
                         ▼
              ┌────────────────────┐
              │ Streamlit UI       │
              └─────────┬──────────┘
                        │
          ┌─────────────┼──────────────┐
          │             │              │
          ▼             ▼              ▼
      Documents       Chat         Analytics
          │             │              │
          ▼             │              ▼
  Document Loader      │        SQLite Database
          │             │
          ▼             │
    Text Cleaner        │
          │             │
          ▼             │
    Text Splitter       │
          │             │
          ▼             │
     Embeddings         │
          │             │
          ▼             │
      FAISS ◄───────────┘
          │
          ▼
     Retriever
          │
          ▼
     Context
          │
          ▼
      Groq LLM
          │
          ▼
     AI Response
          │
          ▼
   Source + Page
📁 Project Folder Structure
LexAI_Document_Assistant/
│
├── app.py
├── config.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── data/
│   ├── documents/
│   └── processed/
│
├── database/
│   └── lexai.db
│
├── vectorstore/
│   └── index/
│
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── document_loader.py
│   ├── text_cleaner.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   ├── rag_chain.py
│   ├── summarizer.py
│   ├── risk_analyzer.py
│   ├── comparator.py
│   ├── history.py
│   ├── export.py
│   └── utils.py
│
├── dashboard/
│   ├── __init__.py
│   ├── analytics.py
│   ├── charts.py
│   └── risk_dashboard.py
│
├── prompts/
│   ├── legal_qa.txt
│   ├── summarization.txt
│   ├── risk_analysis.txt
│   └── comparison.txt
│
├── assets/
│
└── tests/
    ├── __init__.py
    ├── test_loader.py
    ├── test_rag.py
    ├── test_database.py
    └── test_risk.py
📂 Detailed Folder Explanation
app.py
Main Streamlit application.
It provides:
📄 Documents
💬 Legal AI Chat
🔍 Document Search
📝 Summary
⚠️ Risk Analysis
📋 Clause Explorer
🔄 Compare Documents
📊 Analytics Dashboard
🕘 History
⚙️ Settings
config.py
Contains configuration values.
Examples:
GROQ_API_KEY
LLM_MODEL
EMBEDDING_MODEL
CHUNK_SIZE
CHUNK_OVERLAP
TOP_K
DATABASE PATH
VECTOR STORE PATH
requirements.txt
Contains all required Python packages.
Main dependencies:
streamlit
python-dotenv
pypdf
python-docx
langchain
langchain-community
langchain-text-splitters
langchain-core
langchain-groq
langchain-huggingface
sentence-transformers
faiss-cpu
plotly
pandas
numpy
reportlab
pytest
📁 src/
Contains the main backend logic.
database.py
Handles SQLite database operations.
document_loader.py
Loads PDF, DOCX, and TXT files.
text_cleaner.py
Cleans extracted text.
text_splitter.py
Creates document chunks.
embeddings.py
Creates HuggingFace embeddings.
vector_store.py
Creates and loads FAISS indexes.
retriever.py
Retrieves relevant document chunks.
llm.py
Initializes the Groq LLM.
rag_chain.py
Implements the main RAG question-answering pipeline.
summarizer.py
Generates document summaries.
risk_analyzer.py
Analyzes potentially important document clauses.
comparator.py
Compares two documents.
history.py
Manages analysis history.
export.py
Handles output/export functionality.
utils.py
Contains reusable helper functions.
📊 dashboard/
Contains dashboard functionality.
analytics.py
Calculates application statistics.
charts.py
Creates Plotly charts.
risk_dashboard.py
Handles risk dashboard functionality.
📝 prompts/
Stores LLM prompts separately.
legal_qa.txt
summarization.txt
risk_analysis.txt
comparison.txt
This allows prompts to be updated without changing the main Python code.
🗄️ Database Design
LexAI uses SQLite.
Database:
database/lexai.db
Main tables:
documents
│
├── id
├── document
├── path
└── created_at


question_history
│
├── id
├── document
├── question
├── answer
├── sources
└── created_at


summaries
│
├── id
├── document
├── summary
└── created_at


risk_analysis
│
├── id
├── document
├── overall
├── high
├── medium
├── low
├── result
└── created_at
🧠 Vector Store
LexAI uses FAISS.
Document
    ↓
Chunks
    ↓
Embeddings
    ↓
FAISS
FAISS is used to find document chunks that are semantically similar to the user's question.
🛠️ Technology Stack
Technology	Purpose
Python	Core programming
Streamlit	Web interface
LangChain	RAG orchestration
Groq	LLM
HuggingFace	Embeddings
Sentence Transformers	Embedding model
FAISS	Vector search
SQLite	Database
PyPDF	PDF processing
python-docx	DOCX processing
Pandas	Data processing
NumPy	Numerical processing
Plotly	Dashboard visualization
ReportLab	PDF generation
Pytest	Testing
