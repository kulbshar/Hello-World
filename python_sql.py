# Execution Example
# file_path = 'transaction.csv'
# table_name = 'develop_load'
# schema  = 'public'
# dbname = 'xoriant'
# host = 'localhost'
# port = '5432'
# user = 'postgres'
# pwd = 'xoriant@123'

# Connect to Postgres SQL

import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(
    "xoriant", "postgres", "xoriant@123", "localhost", "5432"
)


# you have to create the database sm_app inside the default postgres database

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_database_query = "CREATE DATABASE sm_app"

# Create Database sm_app
# create_database(connection, create_database_query)

# Check connection to sm_app
print("Connection to sm_app Databse")
connection = create_connection(
    "sm_app", "postgres", "xoriant@123", "localhost", "5432"
)


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

# Now create the users table inside the sm_app database:


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL, 
  age INTEGER,
  gender TEXT,
  nationality TEXT
)
"""

execute_query(connection, create_users_table)


# In addition, foreign key referencing is also specified differently,
# as shown in the following script that creates the posts table:
create_posts_table = """
CREATE TABLE IF NOT EXISTS posts (
  id SERIAL PRIMARY KEY, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER REFERENCES users(id)
)
"""

execute_query(connection, create_posts_table)


users = [
    ("James", 25, "male", "USA"),
    ("Leila", 32, "female", "France"),
    ("Brigitte", 35, "female", "England"),
    ("Mike", 40, "male", "Denmark"),
    ("Elizabeth", 21, "female", "Canada"),
]

user_records = ", ".join(["%s"] * len(users))
insert_query = (
    f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"
)

print("Insert into table 'users'")
connection.autocommit = True
cursor = connection.cursor()
# cursor.execute(insert_query, users)

print("Insert into table 'post'")
posts = [
    ("Happy", "I am feeling very happy today", 1),
    ("Hot Weather", "The weather is very hot today", 2),
    ("Help", "I need some help with my work", 2),
    ("Great News", "I am getting married", 1),
    ("Interesting Game", "It was a fantastic game of tennis", 5),
    ("Party", "Anyone up for a late-night party today?", 3),
]

post_records = ", ".join(["%s"] * len(posts))

insert_query = (
    f"INSERT INTO posts (title, description, user_id) VALUES {post_records}"
)

connection.autocommit = True
cursor = connection.cursor()
# cursor.execute(insert_query, posts)


# Read from table
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"The error '{e}' occurred")


print("read from table 'users'")
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

print("read from table 'post'")
select_posts = "SELECT * FROM posts"
posts = execute_read_query(connection, select_posts)

for post in posts:
    print(post)


print("read from table 'post' & 'user' using join")

select_users_posts = """
SELECT
  users.id,
  users.name,
  posts.description
FROM
  posts
  INNER JOIN users ON users.id = posts.user_id
"""

users_posts = execute_read_query(connection, select_users_posts)

for users_post in users_posts:
    print(users_post)


# update

update_post_description = """
UPDATE
  posts
SET
  description = "The weather has become pleasant now"
WHERE
  id = 2
"""

execute_query(connection,  update_post_description)


# Delete
delete_comment = "DELETE FROM comments WHERE id = 5"
execute_query(connection, delete_comment)
