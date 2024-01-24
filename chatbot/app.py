from dotenv import load_dotenv
import os

load_dotenv()  # Loads the .env file

openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import openai
import gradio as gr

import chat


# llm = ChatOpenAI(temperature=0.7, model='gpt-4')

# def predict(message, history):
#     history_langchain_format = []
#     for human, ai in history:
#         history_langchain_format.append(HumanMessage(content=human))
#         history_langchain_format.append(AIMessage(content=ai))
#     history_langchain_format.append(HumanMessage(content=message))
#     gpt_response = llm.invoke(history_langchain_format)
#     return gpt_response.content

gr.ChatInterface(chat.predict,
                 chatbot=gr.Chatbot(height=300),
                 title="Vegan Meal Prep Chatbot",
                 theme="soft").launch()


