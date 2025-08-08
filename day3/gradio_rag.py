# day3/gradio_rag.py
import gradio as gr
from dotenv import load_dotenv
from rag_system import RAGPipeline
import traceback
import os

load_dotenv()  # ensure GROQ_API_KEY is loaded for ChatGroq

# Use a writable persistent dir
rag = RAGPipeline(persist_dir="./chroma_db_space", collection_name="pdf_docs")

def chat_with_pdf(pdf_path: str, question: str):
    try:
        if not pdf_path:
            return "Please upload a PDF."
        if not question or not question.strip():
            return "Please enter a question."

        # Index the uploaded PDF (path is a string because of type='filepath')
        rag.index_document(pdf_path, doc_id_prefix="upload")

        # Ask
        out = rag.query(question, k=4)
        return out["answer"]
    except Exception as e:
        # Surface the exact error to the UI for debugging
        return f"Error: {e}\n\n{traceback.format_exc()}"

demo = gr.Interface(
    fn=chat_with_pdf,
    inputs=[
        gr.File(label="Upload PDF", file_types=[".pdf"], type="filepath"),
        gr.Textbox(label="Ask a question", placeholder="What does the PDF say?"),
    ],
    outputs=gr.Textbox(label="Answer"),
    title="PDF RAG (Chroma + Groq)",
    description="Upload a PDF and ask a question. Uses Chroma for retrieval and Groq LLM for answers."
)

if __name__ == "__main__":
    # Optional: show whether the env var is visible to this process
    print("GROQ key present:", bool(os.getenv("GROQ_API_KEY")))
    demo.launch()
