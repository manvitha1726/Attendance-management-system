import mysql.connector

conn = mysql.connector.connect(user='root', password='',host='localhost',database='miniproject',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()