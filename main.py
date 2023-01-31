from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlmodel import Session, select

from db import init_db, get_session
from models import Blog

app = FastAPI()


class BlogCreate(BaseModel):
    title: str
    cover: str
    content: str


@app.on_event("startup")
def on_startup():
    init_db()


@app.post('/blogs')
def add_blog(item: BlogCreate, session: Session = Depends(get_session)):
    blog = Blog(title=item.title, cover=item.cover, content=item.content)
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return {
        "data": blog
    }


@app.get("/blogs")
async def get_blogs(session: Session = Depends(get_session)):
    statement = select(Blog)
    result = session.exec(statement).all()
    return {"data": result}


@app.get("/blogs/{blog_id}")
async def get_blogs(blog_id: int, session: Session = Depends(get_session)):
    statement = select(Blog).where(Blog.id == blog_id)
    result = session.exec(statement).first()
    return {"data": result}
