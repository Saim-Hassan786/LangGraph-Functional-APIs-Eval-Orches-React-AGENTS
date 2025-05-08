from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv, find_dotenv
from langchain_core.tools import tool
import os
from datetime import datetime

_:bool = load_dotenv(find_dotenv())
google_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=google_api_key
)

@tool
def current_time():
    """Returns the current time"""
    return datetime.now()

@tool
def get_my_name():
    "Returns My Name"
    return "Saim Hassan"



agent = create_react_agent(
    model = llm,
    tools = [current_time,get_my_name],
    prompt="""
    You are helpful assistant that can help with tasks and questions
    You can use the following tools as well
    -current_time
    -get_my_name
    """
)

def main():
    response = agent.invoke({"messages":"what is my name and current time"})
    for message in response["messages"]:
        message.pretty_print()