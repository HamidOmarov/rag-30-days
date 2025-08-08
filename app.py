# app.py  (repo root)
import gradio as gr
from day3.rag_system import RAGPipeline

# separate persistent dir for Spaces
rag = RAGPipeline(persist_dir="./chroma_db_space", collection_name="pdf_docs")

def chat_with_pdf(pdf_file, question):
    if pdf_file is None or not question:
        return "Please upload a PDF and enter a question."
    # index uploaded PDF (idempotent for small demos)
    rag.index_document(pdf_file.name, doc_id_prefix="upload")
    out = rag.query(question, k=4)
    return out["answer"]

demo = gr.Interface(
    fn=chat_with_pdf,
    inputs=[gr.File(label="Upload PDF", file_types=[".pdf"]),
            gr.Textbox(label="Ask a question")],
    outputs=gr.Textbox(label="Answer"),
    title="PDF RAG (Chroma + Groq)",
    description="Upload a PDF, ask a question. Uses Chroma for retrieval and Groq LLM for answering."
)

if __name__ == "__main__":
    demo.launch()
