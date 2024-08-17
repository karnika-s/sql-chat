# creates the DB and displays

import sqlite3      #comes with python 

# Connectt to SQlite
connection=sqlite3.connect("students.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()       #sara sql query fire krne ka kaam iska h 

# create the table
table_info="""
Create table STUDENTS(NAME VARCHAR(25),CLASS VARCHAR(25),
GRADES VARCHAR(25),MARKS INT);

"""
# cursor.execute(table_info)

# Insert records

# cursor.execute('''Insert Into STUDENTS values('Karnika','Data Science','A',100)''')
# cursor.execute('''Insert Into STUDENTS values('Leena','Data Science','B',905)''')
# cursor.execute('''Insert Into STUDENTS values('Shruti','Data Science','C',82)''')
# cursor.execute('''Insert Into STUDENTS values('Aakash','DEVOPS','D',57)''')
# cursor.execute('''Insert Into STUDENTS values('Ram','DEVOPS','E',38)''')
cursor.execute('''Insert Into STUDENTS values('Sita','DEVOPS','A',96)''')


# Dispaly ALl the records

print("The inserted records are : ")
data=cursor.execute('''Select * from STUDENTS''')
for row in data:
    print(row)

# Commit your changes in the databse
connection.commit()
connection.close()