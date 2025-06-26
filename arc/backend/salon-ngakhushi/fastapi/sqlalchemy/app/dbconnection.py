from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base # type: ignore

URL_DATABASE= 'postgresql://vel:hirage@localhost:5432/task_manager'

engine= create_engine(URL_DATABASE, pool_size=20, max_overflow=0)

SessionLocal= sessionmaker(autocommit= False, autoflush= False, bind= engine)

Base= declarative_base()