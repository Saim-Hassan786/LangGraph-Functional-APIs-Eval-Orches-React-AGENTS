from langgraph.func import entrypoint, task
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseModel, Field
from typing import cast
import os
from IPython.display import display,Markdown

_:bool = load_dotenv(find_dotenv())
google_api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=google_api_key
)

class InstructionGenerator(BaseModel):
    workers_instructions: list[str] = Field(
        description="List of sections and their details for the startup report. Each section should be a detailed instruction.",
        default_factory=list
    )

@task
def task_orchestrator(idea: str) -> InstructionGenerator:
    prompt = f"""
    Generate a one liner list of instructions for creating a business report for the following startup idea: {idea}
    
    Each instruction should be detailed and cover one of these aspects:
    1. Market Analysis instruction
    2. Target Audience analysis instruction
    3. Potential Challenges assessment instruction
    4. Revenue Projections calculation instruction
    
    Format each instruction as a separate detailed point that a worker could follow.
    The output should be a list of detailed instructions.
    """
    
    instructions = cast(InstructionGenerator, llm.with_structured_output(InstructionGenerator).invoke(prompt))
    return instructions


@task
def call_worker(instructions)->str:
    result = llm.invoke(instructions).content
    return result


@task
def combine_result(result:list[str])->str:
    return "\n\n".join(result)


@entrypoint()
def call_orchestrator(idea: str):
    instructions = task_orchestrator(idea).result()
    print("\nGenerated Instructions:")
    print("=====================")
    print("\n\n",instructions.model_dump())

    workers = [call_worker(instructions) for instructions in instructions.workers_instructions]
    print("\n\n", workers)

    result = [worker.result() for worker in workers]
    # display(Markdown(result))
    
    final_report = combine_result(result).result
    return final_report
    
    # for i, instruction in enumerate(instructions.workers_instructions, 1):
    #     print(f"\n{i}. {instruction}")

def kickoff():
    final_report = call_orchestrator.invoke("I want to start a startup that sells lead generation AI Agents")
    print("\n\n", final_report)

if __name__ == "__main__":
    kickoff()