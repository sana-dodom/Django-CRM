import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dodom@2012"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE db_dcrm")

print("All Done!") 