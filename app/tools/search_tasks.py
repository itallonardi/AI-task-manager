from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field


class SearchTasksInput(BaseModel):
    status: str = Field(
        description="Status of tasks to search for (e.g., pending, completed)")


@tool("search_tasks", args_schema=SearchTasksInput)
def search_tasks(status: str) -> str:
    """Searches for tasks with the specified status."""
    simulated_tasks = [
        {"id": 1, "task_description": "Buy groceries",
            "due_date": "2024-07-15", "status": status},
        {"id": 2, "task_description": "Finish report",
            "due_date": "2024-07-20", "status": status}
    ]
    operation = {"status": "success", "data": simulated_tasks}
    return operation
