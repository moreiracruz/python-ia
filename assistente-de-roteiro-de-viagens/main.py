import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

destino = 'João Pessoa, Brasil'
numero_dias = 7
numero_crianças = 2
atividade = 'música'

prompt = f'Crie um roteiro de viagem para {destino} de {numero_dias} dias, para uma família com {numero_crianças} crianças, que gosta de {atividade}'

client = OpenAI(
    base_url='http://127.0.0.1:1234/v1',
    api_key='api_key'
)
resposta = client.chat.completions.create(
    model='google/gemma-3-1b',
    # model= 'gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': 'Você é um assistente de roteiro de viagens.'
        },
        {
            'role': 'user',
            'content': prompt
        }
    ]
)

print(resposta.choices[0].message.content)
