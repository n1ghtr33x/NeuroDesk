from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.api.v1.dependencies import get_current_active_user
from app.models.user import User
from app.services.ai_service import generate_ai_response


router = APIRouter(prefix="/ai", tags=["ai"])


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(
    data: ChatRequest,
    current_user: User = Depends(get_current_active_user)
):
    answer = await generate_ai_response(data.message)

    return {
        "message": data.message,
        "answer": answer
    }