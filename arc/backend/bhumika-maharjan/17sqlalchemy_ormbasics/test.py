
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://postgres:postgrespassword@localhost/test1", echo=True)

from sqlalchemy import text

# with engine.connect() as conn:
#     result = conn.execute(text("select 'hello world'"))
#     print(result.all())


# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#     )
#     conn.commit()







# begin-once
# with engine.begin() as conn:
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
#     )
    
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x}  y: {row.y}")


from sqlalchemy.orm import Session
# stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
# with Session(engine) as session:
#     result = session.execute(stmt, {"y": 6})
#     for row in result:
#         print(f"x: {row.x}  y: {row.y}")

with Session(engine) as session:
    result = session.execute(
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
    )
    session.commit()

