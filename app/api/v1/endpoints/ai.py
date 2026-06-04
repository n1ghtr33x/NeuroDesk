from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.api.v1.dependencies import get_current_active_user
from app.models.user import User
from app.services.ai_service import generate_ai_response
from app.schemas.chat import ChatRequest, Completions


router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/chat", response_model=Completions)
async def chat(
    data: ChatRequest,
    current_user: User = Depends(get_current_active_user)
):
    answer = await generate_ai_response(data.message)

    return answer