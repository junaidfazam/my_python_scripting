
from sqlalchemy import create_engine, text
from resources import config


engine= config.engine
with engine.connect() as conn:
    ## cursor is CursorResult object
    cursor = conn.execute(text("select first_name,last_name from customer limit 10"))

    # fetch ALL record. o/p is list having tuple for each row
    all_rows = cursor.fetchall()

    # fetch ONE record. o/p is a tuple one row
    one_row = cursor.fetchone()

    # fetch 10 record. o/p is list having tuple for each row
    batch_row = cursor.fetchmany(10)

    # for single select column it gives a list of values and not the tuple
    tables = cursor.scalars().all()

    # Iteration on result
    for row in all_rows:
        print(row)

    # Using cursor to fetch data in dictionary
    for row in cursor.mappings(): # mappings().fetchmany(10)
        print(row) # output is tuple

