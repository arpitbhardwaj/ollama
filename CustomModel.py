import ollama
modelfile='''
FROM llama3.2:latest
SYSTEM You are Jarvis from Iron man and the user is Tony Stark.
'''

ollama.create(model='jarvis2', modelfile=modelfile)
ollama.list()
ollama.delete('jarvis2')
ollama.list()
