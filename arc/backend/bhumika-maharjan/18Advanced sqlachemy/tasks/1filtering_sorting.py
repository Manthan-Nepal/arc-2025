from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import desc, select

Base = declarative_base()

class Sales(Base):
    __tablename__ = 'sales'
    
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)

engine = create_engine("postgresql://postgres:postgrespassword@localhost/test3")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# sales_data = [
#     Sales(product_name='Laptop', quantity=5, price=1000.0),
#     Sales(product_name='Smartphone', quantity=10, price=500.0),
#     Sales(product_name='Tablet', quantity=7, price=300.0),
#     Sales(product_name='Monitor', quantity=3, price=150.0),
# ]

# session.add_all(sales_data)
# session.commit()

stmt = session.query(Sales)               
stmt = stmt.filter(Sales.quantity > 5)   
stmt = stmt.order_by(Sales.price.asc()) 


# stmt = select(Sales).where(Sales.quantity > 5).order_by(desc(Sales.price))

filtered_sorted_sales = stmt.all()        

print("Sales with quantity > 5, sorted by price ascending:")
for sale in filtered_sorted_sales:
    print(f"{sale.product_name}: quantity={sale.quantity}, price={sale.price}")
