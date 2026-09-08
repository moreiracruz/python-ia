import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

destino = 'João Pessoa, Brasil'
numero_dias = 7
numero_crianças = 2
atividade = 'praia'

prompt = f'Crie um roteiro de viagem para {destino} de {numero_dias} dias, para uma família com {numero_crianças} crianças, que gosta de {atividade}'

modelo = ChatOpenAI(
    model= 'gpt-5.6-luna', #gpt-3.5-turboy
    temperature=0.5,
    api_key=api_key
)

try:
    resposta = modelo.invoke(prompt)
    print(resposta.content)
except Exception as e:
    print(e)

