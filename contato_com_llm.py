# contato_com_llm.py
from openai import OpenAI

client = OpenAI(
    base_url= 'http://127.0.0.1:1234/v1',
    api_key='llm-studio'
)

def recebe_linha_e_retorna_json(linha):
    resposta_do_llm = client.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            {"role": "system", "content": """
            Você é um especialista em análise de dados e conversão de dados para JSON.
            Você receberá uma linha de texto que é uma resenha de um aplicativo em um marketplace online.
            Eu quero que você analise essa resenha, e me retorne um JSON com as seguintes chaves:
            - 'usuario': o nome do usuário que fez a resenha
            - 'resenha_original': a resenha no idioma original que você recebeu
            - 'resenha_pt': a resenha traduzida para o português
            - 'avaliacao': uma avaliação se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra' (apenas uma dessas opções),
               para isto vocÊ deve avaliar o sentimento da mensagem.
               
            Você forneceu explicações e formato do dados.
            
            Exemplo:
            ```json
            {
              "usuario": "Usuário não especificado",
              "resenha_original": "53409593$Safoan Riyad$J'aimais bien ChatGPT. Mais la derniÃ¨re mise Ã  jour a tout gÃ¢chÃ©. Elle a tout oubliÃ©.",
              "resenha_pt": "Adoro o ChatGPT! A última vez que eu atualizei, tudo parece ter esquecido. É incrível!",
              "avaliacao": "Positiva"
            }
            ```
            
            **Explicação da avaliação:**
            
            *   **`usuario`**: Não foi possível determinar o nome do usuário com base na resenha.
            *   **`resenha_original`**: A resenha original é em árabe, e a tradução para português ("Adoro o ChatGPT! A última vez que eu atualizei, tudo parece ter esquecido.") expressa uma opinião positiva sobre o aplicativo.
            *   **`resenha_pt`**: A tradução para português ("Adoro o ChatGPT! A última vez que eu atualizei, tudo parece ter esquecido.") indica um sentimento positivo.
            *   **`avaliacao`**: O sentimento da resenha é considerado "Positiva" devido à expressão de entusiasmo e a menção de "tudo parece ter esquecido".

            Mais o desejado é apenas o JSON.
            
            Exemplo:
            
            '{
              "usuario": "Usuário não especificado",
              "resenha_original": "53409593$Safoan Riyad$J'aimais bien ChatGPT. Mais la derniÃ¨re mise Ã  jour a tout gÃ¢chÃ©. Elle a tout oubliÃ©.",
              "resenha_pt": "Adoro o ChatGPT! A última vez que eu atualizei, tudo parece ter esquecido. É incrível!",
              "avaliacao": "Positiva"
            }'
            
            """},
            {"role": "user", "content": f"Resenha: {linha}"}
        ],
        temperature=0.0
    )
    return resposta_do_llm.choices[0].message.content.strip().replace("```json", '').replace("```", '')