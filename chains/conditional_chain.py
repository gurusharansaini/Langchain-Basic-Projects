from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

class Feedback(BaseModel):
    sentiment :Literal['positive','negative'] = Field(description="Give the sentiment of feedback")

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the following feedback into positive or negative \n  {feedback} \n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write an approprate response to this positive feedback \n  {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write an approprate response to this negative feedback \n  {feedback}",
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment =="positive", prompt2 | model | parser),
    (lambda x:x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x:"could not find sentiment")

)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'this is a smart phone'})
print(result)