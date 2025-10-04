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
        SystemMessage(content='Eres un historiador que conoce los detalles de todas las civilizaciones antiguas'),
        HumanMessage(content='¿Podrías explicarme cómo se construyeron las pirámides de Egipto?')
    ],
    [
        SystemMessage(content='Eres un joven rebelde que odia los temas serios y solo quiere divertirse en fiestas'),
        HumanMessage(content='¿Qué opinas de las pirámides de Egipto?')
    ]
])


print(f'El primer resultado es {resultado.generations[0][0].text}')

print(f'El segundo resultado es {resultado.generations[1][0].text}')
