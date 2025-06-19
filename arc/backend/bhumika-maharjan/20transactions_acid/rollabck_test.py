from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class User(Base):
    __tablename__ = 'usersname'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)  

engine = create_engine("postgresql://postgres:postgrespassword@localhost/fastapi") 
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

user1 = User(name="alish")
user2 = User(name="alens")  

try:
    session.add_all([user1, user2])
    session.commit()
    print("Users committed successfully.")
except IntegrityError as e:
    print("Rollback triggered due to error:", e)
    session.rollback()

user3 = User(name="barb")
session.add(user3)
session.commit()

print("User 'bob' committed successfully.")

