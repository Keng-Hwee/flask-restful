import sqlite3

# Create a file in the current directory (which is going to be our database file)
connection = sqlite3.connect('data.db')

# responsible for executing the queries and store results
cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'kh', 'asdf')
insert_query = "INSERT INTO users VALUES(?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'rolf', 'qwerty'),
    (3, 'anne', 'zxcvb')
]
cursor.executemany(insert_query, users)

# Retrieve data
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query): # loop thru the list
    print(row)

connection.commit()

connection.close()