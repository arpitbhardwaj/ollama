from ollama import Client

client = Client(host='http://localhost:11434')

response = client.chat(model='llama3.2:latest', messages=[
    {
        'role': 'user',
        'content': 'Explain gravity to a 6 year old kid?',
    },
])
print(response)

response = client.chat(model='llama3.2:latest', messages=[
    {"role": "system",
     "content": "You are Jarvis from Iron man and the user is Tony Stark. Respond in only a single line."},
    {'role': 'user', 'content': 'Hi'},
])
print(response['message']['content'])
