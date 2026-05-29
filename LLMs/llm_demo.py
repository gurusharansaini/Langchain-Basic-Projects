from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = 'gpt-3.5-turbo-instruct')

while input() != 'exit':
    result = llm.invoke("what is the capital of india")
    print("Answer : \n",result)
    print("-----------------------------------------------------------------------")