from langchain_community.document_loaders import TextLoader


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()
loader = TextLoader('cricket.txt',encoding='utf-8')

doc = loader.load()
prompt = PromptTemplate(
    template="write a summary on following poem - \n {poem}",
    input_variables = ['poem']
)


model = ChatOpenAI()
parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)
result = chain.invoke({'poem':doc[0].page_content})

print(result)