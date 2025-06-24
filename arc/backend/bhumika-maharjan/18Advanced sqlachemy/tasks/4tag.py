from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

task_tag = Table(
    'task_tag',
    Base.metadata,
    Column('task_id', ForeignKey('tasks.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    tasks = relationship('Task', back_populates='owner')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='tasks')
    tags = relationship('Tag', secondary=task_tag, back_populates='tasks')

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    tasks = relationship('Task', secondary=task_tag, back_populates='tags')

engine = create_engine("postgresql://postgres:postgrespassword@localhost:5432/test1")  
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

user = User(name="Alice")

task1 = Task(title="Fix bugs", owner=user)
task2 = Task(title="Write docs", owner=user)

tag1 = Tag(name="urgent")
tag2 = Tag(name="backend")
tag3 = Tag(name="documentation")

task1.tags.extend([tag1, tag2])
task2.tags.append(tag3)

session.add_all([user, task1, task2, tag1, tag2, tag3])
session.commit()


tasks = session.query(Task).all()
for task in tasks:
    print(f"Task: {task.title}")
    for tag in task.tags:
        print(f" - Tag: {tag.name}")