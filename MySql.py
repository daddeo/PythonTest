# install the MySQL connector with PyCharm
# 1. open command prompt
# 2. run "pip3 install mysql-connector"
#
# current as of now is v2.2.9

import mysql.connector

db = mysql.connector.connect(
    host="localhost", user="{username}", passwd="{password}", database="{name}"
)

# show all available databases
cursor = db.cursor()
cursor.execute("show databases")
for i in cursor:
    print(i)

# instead of using cursor can just use the result
result = cursor.fetchall()  # fetch all rows
print(result)

result = cursor.fetchone()  # fetch one row
print(result)
