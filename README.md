# RAG 30 Days Sprint 🚀

This repository contains a 30-day sprint to master Retrieval-Augmented Generation (RAG) systems using Python, LangChain, and modern AI tools.

## 📅 Day Tracker

| Day | Folder | Description | Status |
|-----|--------|-------------|--------|
| 1 | day1 | Python + Flask setup | ✅ |
| 2 | day2 | LangChain + Groq | ✅ |
| 3 | day3 | Full RAG System | ✅ |
| 4 | day4 | Upwork + Portfolio | ✅ |
| 5 | day5 | Client outreach | ⏳ |

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

✅ **Week 1 Complete:**
- Python environment setup
- LangChain integration
- Full RAG system deployed
- Upwork profile launched
- 5 client proposals sent

🎯 **Current Focus:** Landing first client

## 📊 Sprint Metrics

- **Days Active:** 4/30
- **Projects Completed:** 3
- **Proposals Sent:** 5
- **GitHub Commits:** 20+
- **Deploy Status:** 🟢 Live on HuggingFace

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

> 👣 Four day down, 26 to go. Keep shipping.

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

📅 Day 4 Summary
━━━━━━━━━━━━━━━
✅ Achievements:
- Upwork profile 100%
- Portfolio deployed
- 5 proposals sent
- Skills verified

📊 Metrics:
- Hours worked: 8
- Connects used: 50-70
- Response rate: 0% (too early)

🎯 Tomorrow:
- Monitor responses
- 10 more proposals
- FastAPI learning

## 💼 Professional Portfolio

🔗 **[Portfolio Website](https://hamidomarov.github.io)**
🔗 **[Upwork Profile](https://upwork.com/freelancers/~01xyz)**

### Services Offered:
- RAG System Development
- Custom Chatbot Creation
- PDF Processing Pipelines
- Vector Database Integration
- LangChain Implementation

### Completed Projects:
1. **RAG Document Assistant** - Full-stack PDF Q&A system
2. **EthicaGuard** - Toxic content detection with 95% accuracy
3. **Neural Sonata** - AI music visualization platform


💭 Notes:
Entry-level jobs targeted for quick wins


### Live Demo
🔗 [HuggingFace Space Link](https://huggingface.co/spaces/HamidOmarov/First_RAG_System)

## 📬 Contact

Made by [Hamid Omarov](https://www.linkedin.com/in/hamidomarov)  
Check out my portfolio: [Notion Page](https://www.notion.so/AI-Content-Factory-Operations-2400a72a724c8050b5c6ddc0e6a0a77d)
