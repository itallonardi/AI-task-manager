from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field


class AddTaskInput(BaseModel):
    task_description: str = Field(description="Description of the task")
    due_date: str = Field(description="Due date of the task")


@tool("add_task", args_schema=AddTaskInput)
def add_task(task_description: str, due_date: str) -> str:
    """Adds a new task with a due date."""
    return {"status": "success", "operation": "add", "task_description": task_description, "due_date": due_date}
