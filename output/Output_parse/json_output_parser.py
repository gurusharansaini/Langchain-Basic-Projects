from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()

template1 = PromptTemplate(
    template="gite me the name, age and cityof fictional person \n {format_instruction}",

    partial_variables= {'format_instruction':parser.get_format_instructions()}
)

chain = template1 | model | parser

result = chain.invoke({})

print(result)