import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GITHUB_MODELS_TOKEN"],
)

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Responde en una frase: ¿qué es una póliza de seguro"}
    ],
)

print(response.choices[0].message.content)
print(f"Tokens usados: {response.usage.total_tokens}")