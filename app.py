import langchain

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

f = open('api_key.txt')
api_key = f.read()
chat = ChatOpenAI(api_key=api_key, model="gpt-4o-mini")

# caso 1
# resultado = chat.invoke([HumanMessage(content="¿Puedes decirme la hora en sevilla?")])
# print(resultado.content)

# caso 2
# Especificamos la personalidad que debe tener el sistema
resultado = chat.invoke([SystemMessage(content='Eres un historiador que conoce'
                                               ' los detalles de todas las ciudades del mundo'),
                         HumanMessage(content='¿Puedes decirme donde se encuentra caceres?')])

print(resultado.content)
