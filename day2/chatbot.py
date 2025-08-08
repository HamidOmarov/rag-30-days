cat > day2/chatbot.py << 'PY'
from dotenv import load_dotenv
load_dotenv()

import gradio as gr
from langchain_groq import ChatGroq

def chat(message, history):
    llm = ChatGroq(model="llama3-8b-8192")
    resp = llm.invoke(message)
    return resp.content

demo = gr.ChatInterface(chat)
if __name__ == "__main__":
    demo.launch()
PY
