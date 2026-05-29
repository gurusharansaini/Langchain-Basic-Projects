from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = 'gpt-3.5-turbo-instruct')
e = input()
while e != 'exit':
    
    result = llm.invoke(e)
    print("Answer : \n",result)
    print("-----------------------------------------------------------------------")
    e = input()