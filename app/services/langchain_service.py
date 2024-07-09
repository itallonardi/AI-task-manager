import os
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_tools_agent, AgentExecutor
from dotenv import load_dotenv
from ..tools.add_task import add_task
from ..tools.search_tasks import search_tasks
from ..tools.delete_task import delete_task

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OPENAI_API_KEY found in environment variables")

llm = ChatOpenAI(api_key=api_key, model="gpt-4o", temperature=0)
tools = [add_task, search_tasks, delete_task]
prompt = hub.pull("hwchase17/openai-tools-agent")

agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


async def process_input_text(text: str, topic: str) -> str:
    print(f"Processing text: {text} with topic: {topic}")
    response = agent_executor.invoke({"input": text})
    print(f"Tool response: {response}")
    return response['output']
