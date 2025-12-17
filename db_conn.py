import mysql.connector as db
def connect():
    return db.connect(
        host="localhost",
        user="root",database="bank_system",
        password="0103"
        )
    