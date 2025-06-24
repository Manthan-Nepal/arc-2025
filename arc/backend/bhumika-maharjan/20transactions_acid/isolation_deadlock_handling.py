import time
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from psycopg2.errors import DeadlockDetected

DATABASE_URL = "postgresql://postgres:postgrespassword@localhost/fastapi"

Base = declarative_base()

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    balance = Column(Integer)

engine = create_engine(DATABASE_URL, isolation_level="SERIALIZABLE")
Session = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

def transfer_funds_with_retry(from_id, to_id, amount, retries=2):
    for attempt in range(retries):
        session = Session()
        try:
            from_acc = session.query(Account).filter(Account.id == from_id).with_for_update().one()
            to_acc = session.query(Account).filter(Account.id == to_id).with_for_update().one()

            if from_acc.balance < amount:
                raise ValueError("Insufficient funds")

            from_acc.balance -= amount
            to_acc.balance += amount

            session.commit()
            print(f"Transferred {amount} from {from_acc.name} to {to_acc.name}")
            return
        except OperationalError as e:
            session.rollback()
            if isinstance(e.orig, DeadlockDetected):
                print(f"Deadlock detected. Retrying... ({attempt+1})")
                time.sleep(1)
            else:
                raise
        finally:
            session.close()
    raise RuntimeError("Transfer failed after retries.")


if __name__ == "__main__":
    if __name__ == "__main__":
        session = Session()
        try:
            acc1 = Account(id=1, name="Alice", balance=100)
            acc2 = Account(id=2, name="Bob", balance=100)
            session.add_all([acc1, acc2])
            session.commit()
            print("Accounts created.")
        except Exception as e:
            session.rollback()
            print("Error creating accounts:", e)
        finally:
            session.close()


        transfer_funds_with_retry(1, 2, 50)
