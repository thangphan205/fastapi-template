import sqlite3
from passlib.context import CryptContext
from datetime import datetime

# import psycopg2
from settings import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Connecting to postgresql

# connection = psycopg2.connect(
#     user="",
#     password="",
#     host="127.0.0.1",
#     port="5432",
#     database="",
# )
# cursor = connection.cursor()

# Connecting to sqlite
connection = sqlite3.connect(settings.SQLALCHEMY_DATABASE_URL)
cursor = connection.cursor()

USERNAME = "admin"
HASHED_PASSWORD = pwd_context.hash("hocmang")
EMAIL = "thangphan205@gmail.com"
FULL_USERNAME = "Thang Phan"
USER_ROLE = 100
IS_ACTIVE = 1
DATETIME_NOW = datetime.now()
LOGIN_FAIL = 0
DEPARTMENT = "IT"
DESCRIPTION = "hocmang.net"
# Preparing SQL queries to INSERT a record into the database.
query = """INSERT INTO users(
   username, hashed_password, email, full_username, role, 
   is_active, department, last_login, created_date, login_fail,
   description
   ) VALUES 
   ('{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}')""".format(
    USERNAME,
    HASHED_PASSWORD,
    EMAIL,
    FULL_USERNAME,
    USER_ROLE,
    IS_ACTIVE,
    DEPARTMENT,
    DATETIME_NOW,
    DATETIME_NOW,
    0,
    DESCRIPTION,
)
print(query)
cursor.execute(query)

# Commit your changes in the database
connection.commit()
print("Inserted username : {}".format(USERNAME))

# Closing the connection
connection.close()
