from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    role: Mapped[str] = mapped_column(String(20))  # user / assistant
    content: Mapped[str] = mapped_column(Text)

    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))

    chat: Mapped["Chat"] = relationship(back_populates="messages")