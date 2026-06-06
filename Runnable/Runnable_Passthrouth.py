from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a joke on topic {topic}",
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables = ['text']
)


model = ChatOpenAI()

parsers = StrOutputParser()

joke_gen = RunnableSequence(prompt1,model,parsers)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'Explanation':RunnableSequence(prompt2,model,parsers)
})

final_chain = RunnableSequence(joke_gen, parallel_chain)
result = final_chain.invoke({'topic':'AI'})

print(result)

