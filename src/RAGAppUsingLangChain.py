from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

raw_documents = TextLoader("../resources/LangchainRetrieval.txt").load()
#print(raw_documents)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=20)
documents = text_splitter.split_documents(raw_documents)
print(len(documents))

#print(documents[0])
#print(documents[1])

oembed = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text")
db = Chroma.from_documents(documents, embedding=oembed)
query = "What is text embedding and how does langchain help in doing it"
docs = db.similarity_search(query)
print(len(docs))
#print(docs[3].page_content)

template = """Answer the question based only on the following context:

{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOllama(
    model="llama3.2:latest",
    temperature=0
)

retriever = db.as_retriever()

def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

msg = chain.invoke("What is text embedding and how does langchain help in doing it")
print(msg)