import langchain

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

f = open('api_key.txt')
api_key =f.read()
chat= ChatOpenAI(api_key =api_key,model="gpt-4o-mini")

resultado = chat.invoke([HumanMessage(content="¿Puedes decirme la hora en sevilla?")])
print(resultado.content)