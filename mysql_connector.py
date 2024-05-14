import mysql.connector

class MyDB():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="apirest"
        )
        self.cursor = self.mydb.cursor()