import os
import sqlite3

conn = sqlite3.connect('test2.db', timeout=30)
cursor = conn.cursor()
z="INSERT INTO Reference(NAME) Values('Geoffrey Bowker')"
cursor.execute(z)
p = cursor.execute("Select * from Reference Limit 1")
for row in p:
    x= "python scholar.py -c 1 --author " + row[0]
    print (x)


conn.commit()
print ("Records created successfully")
conn.close()