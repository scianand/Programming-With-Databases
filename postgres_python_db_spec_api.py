"""
Postgres SQL table creation using Python Database Specification API

"""

import psycopg2
import pandas

def create_table(conn):
    cursor = conn.cursor()

    # create table if not exist
    cursor.execute(""" CREATE TABLE IF NOT EXISTS Sales(ORDER_NUM INT PRIMARY KEY,
        ORDER_TYPE TEXT,
        CUST_NAME TEXT,
        PROD_NUMBER TEXT,
        PROD_NAME TEXT,
        QUANTITY TEXT,
        PRICE REAL,
        DISCOUNT REAL,
        ORDER_TOTAL REAL);""")
    conn.commit()
    
    print("table created!")

    # insert data into the table
    df = pandas.read_csv("red30-postgres.csv")

    for row in df.itertuples():
        cursor.execute(""" INSERT INTO Sales(ORDER_NUM,
            ORDER_TYPE,
            CUST_NAME,
            PROD_NUMBER,
            PROD_NAME,
            QUANTITY,
            PRICE,
            DISCOUNT,
            ORDER_TOTAL) VALUES (%s, %s, %s, %s, %s,
            %s, %s, %s, %s)""", (row.order_num, row.order_type, row.cust_name, row.prod_number,
            row.prod_name, row.quantity, row.price, row.discount, row.order_total))
    
    conn.commit()
    print("data inserted!")



if __name__ == '__main__':
    conn = psycopg2.connect(database="red30",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432")

    create_table(conn)

    conn.close()