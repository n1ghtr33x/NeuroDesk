from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.token import Token
from app.schemas.user import UserCreate, User
from app.services.user_service import (
    authenticate_user,
    get_user_by_username,
    create_user,
)
from app.core.security import create_access_token

router = APIRouter(prefix='/auth', tags=['authentication'])


@router.post('/register', response_model=User, status_code=201)
async def register(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    existing_user = await get_user_by_username(db, user_data.username)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Username already registered'
        )

    return await create_user(db, user_data)

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})

    return Token(access_token=access_token, token_type="bearer")