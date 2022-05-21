import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tts",
    password="123456789",
    database="tts",
)

mycursor = mydb.cursor(dictionary=True)

sql = "INSERT INTO users (username, password, name, last_name, user_role_id) VALUES ('yoyo', '555', 'yy', 'uu', '2')"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

ID = mycursor.lastrowid

print(ID)


sql = "SELECT * FROM users WHERE ID = {}".format(ID)

mycursor.execute(sql)

data = mycursor.fetchall()

print(data)

mycursor.close()

mydb.close()




