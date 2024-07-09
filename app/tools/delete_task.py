from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field


class DeleteTaskInput(BaseModel):
    task_id: str = Field(description="ID of the task")


@tool("delete_task", args_schema=DeleteTaskInput)
def delete_task(task_id: str) -> str:
    """Deletes the task with the specified ID."""
    return {"status": "success", "operation": "delete", "task_id": task_id}
