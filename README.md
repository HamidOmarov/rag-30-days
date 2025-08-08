# RAG 30 Days Sprint 🚀

This repository contains a 30-day sprint to master Retrieval-Augmented Generation (RAG) systems using Python, LangChain, and modern AI tools.

## 📅 Day Tracker

| Day | Folder | Description            | Status |
|-----|--------|------------------------|--------|
| 1   | day1   | Hello world test file  | ✅     |
| 2   | day2   | TBD                    | ⏳     |
| ... | ...    | ...                    | ...    |

## 📂 Folder Structure

rag-30-days/
│
├── day1/
│ └── hello_ai.py
│
├── README.md

markdown
Copy
Edit

## 🧠 Goal

To build a production-ready RAG pipeline in 30 days and land a remote AI job by the end of the sprint.

## 🛠️ Tools

- Python
- LangChain
- ChromaDB / Weaviate / FAISS
- OpenAI API
- Streamlit (optional UI)
- Git & GitHub

## 📈 Progress

Check commits and folders daily to follow the sprint. Each folder corresponds to 1 day of learning and building.

## 📅 Day 1 – Getting Started with Python & Flask

### ✅ What I Learned
- Refreshed core **Python basics** (variables, functions, classes, etc.)
- Built my first **Flask API** with real-world JSON responses
- Practiced structured coding with **Copilot assistance**

### 🛠️ What I Built
- `hello_ai.py`: A minimal Python script to print a welcome message
- `api.py`: A Flask application with 3 endpoints:
  - `/hello`: greeting message
  - `/calculate`: accepts 2 numbers (POST) and returns their sum
  - `/ai-ready`: motivational message for AI learning

### 🔮 Tomorrow's Plan
- Begin **LangChain** setup and environment configuration
- Start working on **RAG-based document processing**
- Set up folder structure and `day2` workflow

> 👣 One day down, 29 to go. Keep shipping.



📅 Day 2 – LangChain Basics & My First Chatbot
✅ What I Learned

Got hands-on with LangChain components: LLMChain, PromptTemplate

Integrated Groq API into LangChain LLM flow

Built my first functional chatbot using a simple chain logic

Practiced chaining user input → prompt → response generation

🛠️ What I Built

first_chain.py: a hello-world chain using PromptTemplate + LLMChain

chatbot.py: a simple question-answer chatbot using Groq LLM

Reusable design: change the prompt, change the behavior

📚 Key Takeaways

Prompt design is everything — small tweaks lead to major output changes

Groq models are blazing fast, but careful prompting is still necessary

LangChain is modular and beginner-friendly once you get the flow

🔮 Tomorrow's Plan

Begin building a real RAG pipeline

Add PDF loading and explore chunking strategies

Start using Chroma for vector storage

## Day 3: First RAG System ✅

### What I Built
- PDF processing pipeline (loader + optimal chunker)
- Compared 3 chunking strategies (fixed, recursive, token)
- ChromaDB vector storage (persistent)
- SentenceTransformer embeddings (MiniLM)
- Gradio chat interface (upload PDF → ask)
- Deployment on Hugging Face Spaces

### Key Learnings
- Fixed vs Recursive vs Token-based chunking trade-offs
- Embedding format must be list[list[float]] for Chroma
- New Chroma API uses `PersistentClient`
- Prompt design: extractive answers + fallback

### Live Demo
🔗 [HuggingFace Space Link](https://didactic-winner-q7g79xg9gp4626w56-7860.app.github.dev/)

## 📬 Contact

Made by [Hamid Omarov](https://www.linkedin.com/in/hamidomarov)  
Check out my portfolio: [Notion Page](https://www.notion.so/AI-Content-Factory-Operations-2400a72a724c8050b5c6ddc0e6a0a77d)
