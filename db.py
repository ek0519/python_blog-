from sqlmodel import create_engine, SQLModel, Session


engine = create_engine("postgresql+psycopg2://127.0.0.1:5432/python_blog", echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
