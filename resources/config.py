from sqlalchemy import create_engine


db_user='root'
db_pass='password'
host = 'localhost'
port = 3306
driver = "com.mysql.cj.jdbc.Driver"
database = "my_spark_project"
engine = create_engine(
    f"mysql+pymysql://{db_user}:{db_pass}@{host}:{port}/{database}"
)


# fetching database credential from .evn
## pip install python-dotenv is required if using .env
# load_dotenv() # Load variables from .env
# import os
# db_username = os.getenv("MYSQL_USER")
# db_password = os.getenv("MYSQL_PASSWORD")
# host = os.getenv("MYSQL_HOST", "localhost")
# port = os.getenv("MYSQL_PORT", "3306")
# database = os.getenv("MYSQL_DB")
#
# engine = create_engine(
#     f"mysql+pymysql://{db_user}:{db_pass}@{host}:{port}/{database}")
