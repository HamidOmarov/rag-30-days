from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

# Step 1: Set up the LLM (Groq with LLaMA 3.1)
llm = ChatGroq(model="llama3-8b-8192")

# Step 2: Define prompt template with Azerbaijan context
template = """
You are an expert assistant with deep knowledge about Azerbaijan.

Here is some context about Azerbaijan:
Azerbaijan is a country located at the crossroads of Eastern Europe and Western Asia. It is known for its rich culture, history, oil resources, and modern capital Baku.

Now, answer the following question clearly and concisely:   
{question}
"""

prompt = PromptTemplate.from_template(template) 

# Step 3: Create the LangChain LLMChain     
chain = LLMChain(llm=llm, prompt=prompt)

# Step 4: Run the chain with a user question
if __name__ == "__main__":
    user_question = input("Enter your question: ")
    answer = chain.run(user_question)
    print("\nAnswer:\n", answer)
# Step 5: Test the chain with a sample question
    # Example: "What is the capital of Azerbaijan?"
    # This will prompt the user to enter a question and provide an answer based on the context
    # Note: Ensure you have the necessary environment set up to run this code, including the
    # LangChain and Groq libraries installed and configured.
    # You can run this script in an environment where the Groq model is accessible.
    # Make sure to handle any exceptions or errors that may arise during execution. 