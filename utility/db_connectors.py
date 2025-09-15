from sqlalchemy import create_engine, text
from resources import config
import pandas as pd

engine = config.engine

with engine.connect() as conn:
    query = text("select first_name, last_name from customer limit 5")

    # Option 1: Using pandas read_sql (recommended)
    df = pd.read_sql(query, conn)

    # Option 2: Using fetchall and converting manually
    # cursor = conn.execute(query)
    # df = pd.DataFrame(cursor.fetchall(), columns=cursor.keys())

print(df)
