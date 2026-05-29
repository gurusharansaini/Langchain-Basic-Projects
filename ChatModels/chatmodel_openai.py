from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4')
e = ""
while e != 'exit':
    e = input()
    result = model.invoke(e)
    print(result)
    print("------------------------------------------------------------")