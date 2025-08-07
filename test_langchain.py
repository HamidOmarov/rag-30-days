from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# .env faylından API açarını yüklə
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# LLM obyekti yarat (OpenAI)
llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# Prompt (sual şablonu) yarat
prompt = PromptTemplate(
    input_variables=["name"],
    template="What would be a good company name for a company that makes {name}?"
)

# Chain yaradaraq LLM ilə promptu birləşdir
chain = LLMChain(llm=llm, prompt=prompt)

# Chain-i işə sal
response = chain.run("colorful socks")

print(response)
