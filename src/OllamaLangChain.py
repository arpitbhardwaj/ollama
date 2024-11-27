from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that gives a one-line definition of the word entered by user"),
        ("human", "{user_input}"),
    ]
)

messages = chat_template.format_messages(user_input="Sesquipedalian")
print(messages)

llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)

ai_msg = llm.invoke(messages)
print(ai_msg)

chain = chat_template | llm | StrOutputParser()

chain_msg = chain.invoke({"user_input": "Onomatopoeia"})
print(chain_msg)