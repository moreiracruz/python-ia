from openai import OpenAI

client = OpenAI(
  base_url= 'http://127.0.0.1:1234/v1'
)

response = client.chat.completions.create(
  model= 'google/gemma-3-1b',
  messages=[
    {"role": "system", "content": "Você é um assistente de IA que sempre responde de forma muito sarcática."},
    {"role": "user", "content": "Responda de forma sucinta, em uma UNICA linha, o que é IA Generativa?"}
  ],
  temperature=1.0
)

# print(response)
print(response.choices[0].message.content)
