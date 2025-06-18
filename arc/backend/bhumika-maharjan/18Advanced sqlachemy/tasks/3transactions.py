from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

engine = create_engine("postgresql://postgres:postgrespassword@localhost:5432/test3")

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

user = User(name="bhumika")

with session.begin():
    session.add(user)


