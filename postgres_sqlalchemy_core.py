"""
Access the table using SQL Alchemy core
user: postgres
password: postgres
"""

from sqlalchemy import create_engine, Table, MetaData

engine =  create_engine('postgres://postgres:postgres@localhost/red30')

with engine.connect() as connection:
    meta = MetaData(engine)
    # select the sales table from the red30 database
    sales_table = Table('sales', meta, autoload=True, autoload_with=engine)

    # insert statement
    insert_statement  = sales_table.insert().values(order_num=500900,
        order_type='retail',
        cust_name = 'Vimal Anand',
        prod_number = 'EB521',
        prod_name = 'Understandinng Database',
        quantity=1,
        price=1000,
        discount=0,
        order_total=1000)

    connection.execute(insert_statement)

    # Read from the database
    select_statement = sales_table.select().limit(10)
    result_set = connection.execute(select_statement)

    for r in result_set:
        print(r)

    # Update
    update_statement = sales_table.update().where(
        sales_table.c.order_num==500900).values(quantity=5, order_total=5000)
    connection.execute(update_statement)

    # Check the updated value

    check_statement = sales_table.select().where(
        sales_table.c.order_num==500900)
    result = connection.execute(check_statement)
    for r in result:
        print(r)

    # Delete the record
    delete_statement = sales_table.delete().where(
        sales_table.c.order_num==500900)

    # Check deleted record
    record = sales_table.select().where(
        sales_table.c.order_num==500900)
    print(record.rowcount)
    