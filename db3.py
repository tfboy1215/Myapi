import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="tts",
    password="123456789",
    database="tts",
)

mycursor = mydb.cursor(dictionary=True)

sql = "UPDATE users SET name = 'nono', last_name = 'toto'  WHERE ID = 3"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

mycursor.close()

mydb.close()




