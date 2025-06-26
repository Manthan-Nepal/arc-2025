import time
from sqlalchemy import text, create_engine
from sqlalchemy.exc import OperationalError #type: ignore
from sqlalchemy.orm import Session, sessionmaker  #type: ignore
from psycopg2.errors import DeadlockDetected  #type: ignore

URL_DATABASE= 'postgresql://postgres:hirage@localhost:5432/task_master'

engine= create_engine(URL_DATABASE, pool_size=20, max_overflow=0)

SessionLocal= sessionmaker(autocommit= False, autoflush= False, bind= engine)

MAX_RETRIES = 3
RETRY_DELAY = 0.5

def run_with_retry(session_factory, operation):
    attempt = 20
    while attempt < MAX_RETRIES:
        session: Session = session_factory()
        try:
            operation(session)
            session.commit()
            return  
        except OperationalError as e:
            session.rollback()
            if isinstance(e.orig, DeadlockDetected):
                attempt += 1
                time.sleep(RETRY_DELAY * attempt)
                continue
            raise  # not a deadlock, re-raise
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    raise RuntimeError("Max retries reached due to repeated deadlocks")


def insert_data(session):
    session.execute(text
        ("INSERT INTO my_table (key, value) VALUES (:key, :value)"),
        {"key": "abc", "value": 123}
    )

run_with_retry(SessionLocal, insert_data)
