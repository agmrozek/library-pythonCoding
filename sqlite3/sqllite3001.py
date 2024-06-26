import sqlite3

conn = sqlite3.connect("testdatabase.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER, firstname TEXT, lastname TEXT, age INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS credentials (id INTEGER, username TEXT, email TEXT)''')

insert_query = "INSERT INTO credentials (username, email) VALUES (?, ?)"
user_data = ('john_doe', 'john.doe@email.com')
cursor.execute(insert_query, user_data)

insert_userdata = "INSERT INTO users (firstname, lastname, age) VALUES (?, ?, ?)"
add_user = ('Billy','Bob','34')
cursor.execute(insert_userdata, add_user)

select_query = "SELECT * FROM users"
cursor.execute(select_query)
records = cursor.fetchall()

for record in records:
    print(record)

conn.commit()
conn.close()
