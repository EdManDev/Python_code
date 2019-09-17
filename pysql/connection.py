import mysql.connector

mydb = mysql.connector.connect(
  host="pymysql",
  user="root",
  passwd=""
)

print(mydb)