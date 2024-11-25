import ollama

result = ollama.generate(model='llama3.2:latest',
  prompt='Give me a joke on Generative AI',
)
print(result)
print(result['response'])

response = ollama.chat(model='llama3.2:latest', messages=[
  {
    'role': 'user',
    'content': 'Give me a joke on Generative AI',
  },
])
print(response)
print(response['message']['content'])
