# 🚀 Exploring SQLAlchemy for Database Connections

- This project demonstrates how to use **SQLAlchemy** in Python to connect
with relational databases such as **MySQL, SQL Server, and Snowflake**.
- It covers different result-fetching techniques and integration with
Pandas for DataFrame-based analysis.
------------------------------------------------------------------------

## ⚙️ Setup
### 1. Clone the repository

``` bash
git clone https://github.com/your-username/sqlalchemy-connections-demo.git
cd sqlalchemy-connections-demo
```
### 2. Install dependencies

``` bash
pip install sqlalchemy pandas
```

### 3. Update your config

In `resources/config.py`, update your database credentials:

``` python
from sqlalchemy import create_engine

db_user = 'root'
db_pass = 'password'
host = 'localhost'
port = 3306
database = 'my_spark_project'

engine = create_engine(
    f"mysql+pymysql://{db_user}:{db_pass}@{host}:{port}/{database}"
)
```
## 📝 Usage

### Running queries with SQLAlchemy

``` python
from sqlalchemy import text
from resources import config

engine = config.engine
with engine.connect() as conn:
    cursor = conn.execute(text("SELECT first_name, last_name FROM customer LIMIT 5"))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
```

### Different fetch methods

-   `fetchone()` → get a single row\
-   `fetchall()` → retrieve all rows\
-   `fetchmany(n)` → batch rows\
-   `scalars()` → get column values directly\
-   `mappings()` → dictionary-style results

### Fetching into a Pandas DataFrame

``` python
import pandas as pd
from resources import config

query = "SELECT first_name, last_name FROM customer LIMIT 5"
df = pd.read_sql(query, config.engine)
print(df.head())
```
------------------------------------------------------------------------

## 💡 Key Learnings

-   SQLAlchemy abstracts away **vendor-specific connection details**.\
-   Works across **MySQL, SQL Server, Snowflake, PostgreSQL, SQLite,
    Oracle**, and more.\
-   Flexible result handling: tuples, batches, scalars, dictionaries.\
-   Seamless integration with **Pandas** for analytics workflows.
------------------------------------------------------------------------
## 📌 Tags

#SQLAlchemy #Python #Pandas #DataEngineering #MySQL #SQLServer
#Snowflake

