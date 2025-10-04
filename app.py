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
# resultado = chat.invoke([SystemMessage(content='Eres un historiador que conoce'
# ' los detalles de todas las ciudades del mundo'),
# HumanMessage(content='¿Puedes decirme donde se encuentra caceres?')])

# print(resultado.content)

##caso 3
# Obtener varios resultados invocando al chat de OpenAI con "generate"
resultado = chat.generate([
    [
        SystemMessage(content='Eres un historiador que conoce los detalles de todas las ciudades del mundo'),
        HumanMessage(content='¿Puedes decirme dónde se encuentra Cáceres?')
    ],
    [
        SystemMessage(content='Eres un joven rudo que no le gusta que le pregunten, solo quiere estar de fiesta'),
        HumanMessage(content='¿Puedes decirme dónde se encuentra Cáceres?')
    ]
])

print(f'El primer resultado es {resultado.generations[0][0].text}')

print(f'El segundo resultado es {resultado.generations[1][0].text}')
