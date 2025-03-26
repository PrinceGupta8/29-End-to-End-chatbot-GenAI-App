#import all the libraries
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import openai



from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()

#initialize keys to environment
os.environ['langchain_api_key']=os.getenv('langchain_api_key')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ["LANGCHAIN_PROJECT"]='Basic Q&A Generative AI App'

prompt=ChatPromptTemplate.from_messages(
    [
        ('system','you are a helpful assistant please provide answer to the question'),
        ('user','Question{question}')
    ]
)


def generate_response(question,llm,api_key,temperature,max_tokens):
    openai.api_key=api_key
    llm=ChatOpenAI(model=llm,temperature=temperature,max_tokens=max_tokens)
    parser=StrOutputParser()
    chain=prompt|llm|parser
    answer=chain.invoke({'question':question})
    return answer
    

st.title('Basic Q&A Generative AI Chatbot')
st.sidebar.title('Settings')
api_key=st.sidebar.text_input('Enter your OpenAI api key',type='password')
llm=st.sidebar.selectbox('Select a model',['gpt-4o','gpt-4-turbo','gpt-4'])
temperature=st.sidebar.slider('Temperature',min_value=0,max_value=1,value=1)
max_tokens=st.sidebar.slider('Maximum Tokens',min_value=50,max_value=300,value=150)

input=st.text_input('message')
if input:
    if api_key:
        response=generate_response(input,llm,api_key,temperature,max_tokens)
        st.write(response)
    else:
        st.write('Please write api key')








