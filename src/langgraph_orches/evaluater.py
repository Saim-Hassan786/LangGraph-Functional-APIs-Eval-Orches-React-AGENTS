from langgraph.func import entrypoint, task
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
# from pydantic import BaseModel, Field
# from typing import cast
import os

_:bool = load_dotenv(find_dotenv())
google_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=google_api_key
)


@task
def poem_generator(input_data:str)-> str:
    return llm.invoke(f"Generate a funny poem about the {input_data}").content

@task
def poem_evaluator(poem:str)-> str:
    return llm.invoke(f"Evaluate the poem whether it is funny or not {poem}, in output return only one out of following 2 words either 'funny' or 'retry' ").content

@entrypoint()
def evaluate_report_optimizer(topic:str)->str:
    poem = None
    while True:
        poem = poem_generator(topic).result()
        print("\n\n Generated Poem", poem)
        evaluated = poem_evaluator(poem).result()
        print("\n\n Evaluated Poem",evaluated)
        if evaluated.lower() == "funny":
            break
        else:
            continue
    return poem


def evalit():
    obj = evaluate_report_optimizer.invoke("Indian Politics")
    print("\n\n Final Poem",obj)
