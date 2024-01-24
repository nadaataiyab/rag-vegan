from langchain.schema import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(temperature=0.7, model='gpt-4')

def predict(message, history):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = llm.invoke(history_langchain_format)
    return gpt_response.content