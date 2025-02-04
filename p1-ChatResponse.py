from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='llama3.2:latest', messages=[
  {
    'role': 'user',
    'content': 'Me dê 5 cores que combinam com azul',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)