import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="ffs",
    password="123456789",
    database="ffs",
)

mycursor = mydb.cursor(dictionary=True)

sql = "DELETE FROM users WHERE username = 'yoyo' and password = '555'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

mycursor.close()

mydb.close()




