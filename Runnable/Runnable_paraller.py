from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about topic {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template="Generate a linkdin post about {topic}",
    input_variables = ['topic']
)


model = ChatOpenAI()

parsers = StrOutputParser()

parallel_chain = RunnableParallel({
    'twite':RunnableSequence(prompt1,model,parsers),
    'Linkdin':RunnableSequence(prompt2,model,parsers)
})


result = parallel_chain.invoke({'topic':'AI'})

print(result)

