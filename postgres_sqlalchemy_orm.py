"""
Access the table using SQL Alchemy core
user: postgres
password: postgres

"""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connect to the database
engine = create_engine('postgres://postgres:postgres@localhost/red30')
Base = declarative_base(engine)
# access all the metadata from the engine
Base.metadata.reflect(engine)

# Class representation of the sales table
class Sales(Base):
    __table__ = Base.metadata.tables['sales']

    def __repr__(self):
        return '''<Sale(order_num='{0}', order_type='{1}', cust_name='{2}', prod_number='{3}',
            prod_name='{4}', quantity='{5}', price='{6}', discount='{7}', order_total='{8}')>'''.format(self.order_num,
            self.order_type, self.cust_name, self.prod_number, self.prod_name, self.quantity,
            self.price, self.discount, self.order_total)


def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__=='__main__':
    session = loadSession()

    # Read
    smallest_sales = session.query(Sales).order_by(Sales.order_total).limit(10)
    print(smallest_sales[0].cust_name)

    # Insert
    recent_sale = Sales(order_num=60090, order_type='Retail', cust_name='Vimal Anand',
        prod_number='EB567', prod_name='Understanding Postgres', quantity=3,
        price=100, discount=0, order_total=300)
    
    print(recent_sale)
    session.add(recent_sale)
    session.commit()

    # Update
    recent_sale.quantity = 2
    recent_sale.order_total = 200
    session.commit()
    updated_sale = session.query(Sales).filter(Sales.order_num==60090).first()
    print(updated_sale)

    # Delete
    returned_sale = session.query(Sales).filter(Sales.order_num==60090).first()
    session.delete(returned_sale)
    session.commit()