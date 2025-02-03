from ollama import chat

stream = chat(
    model='llama3.2',
    messages=[{'role': 'user', 'content': 'Por que o céu é azul?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)