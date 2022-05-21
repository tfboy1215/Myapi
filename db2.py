import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ffs",
    password="123456789",
    database="ffs",
)

mycursor = mydb.cursor(dictionary=True)

sql = "SELECT * FROM users"

mycursor.execute(sql)

data = mycursor.fetchall()

mycursor.close()

mydb.close()

for x in data:
    print(x)


