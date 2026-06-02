from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import verify_password, get_password_hash


async def get_user_by_username(
    db: AsyncSession,
    username: str
) -> User | None:
    result = await db.execute(
        select(User).where(User.username == username)
    )

    return result.scalar_one_or_none()


async def create_user(
    db: AsyncSession,
    user_data: UserCreate
) -> User:
    user = User(
        username=user_data.username,
        hashed_password=get_password_hash(user_data.password),
        is_active=True
    )

    db.add(user)

    await db.commit()
    await db.refresh(user)

    return user


async def authenticate_user(
    db: AsyncSession,
    username: str,
    password: str
) -> User | None:
    user = await get_user_by_username(db, username)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user