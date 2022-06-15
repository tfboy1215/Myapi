import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ffs",
    password="123456789",
    database="ffs",
)

mycursor = mydb.cursor(dictionary=True)

sql = "UPDATE users SET name = 'uu', last_name = 'ss'  WHERE ID = 3"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

mycursor.close()

mydb.close()




