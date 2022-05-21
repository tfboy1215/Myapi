import mysql.connector


def con():
    mydb = mysql.connector.connect(
        host="localhost",
        user="tts",
        password="123456789",
        database="tts",
    )
    return mydb


class Select():
    def userAll():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()

        return data
