from typing import Optional

from sqlmodel import SQLModel, Field


class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    cover: str
    content: str
