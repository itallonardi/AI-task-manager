from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from ..services.langchain_service import process_input_text

router = APIRouter()


class ChatRequest(BaseModel):
    text: str
    topic: Optional[str] = Field(
        None, description="The topic of the conversation")


@router.post("/chat/")
async def chat_message(request: ChatRequest):
    try:
        topic = request.topic or "general"
        response = await process_input_text(request.text, topic)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
