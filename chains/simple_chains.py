from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Generate 5 intersting facts about topic {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result  = chain.invoke({'topic':'cricket'})

print(result)
