import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="green_grocer", # your username
                      passwd="password", # your password
                      db="spaza") # name of the data base
cursor = db.cursor ()


cursor.execute ("SELECT * FROM Products")
data = cursor.fetchall ()
for row in data:
    print row[1]



cursor.close ()


db.close ()