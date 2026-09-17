import sqlite3

conn=sqlite3.connect('school.db')
print("database successfully connected")

conn.execute("create table if not exists tblstudent77(rollno int primary key,name text,subject text,marks integer)")
print("table successfully created ")


conn.execute("insert into tblstudent77 values(1,'harsh','maths',99)")
conn.execute("insert into tblstudent77 values(2,'karan','science',80)")
conn.execute("insert into tblstudent77 values(3,'laksh','GK',67)")
print("data successfully inserted")



conn.commit()
print("changes successfully commited")

conn.close()
print("connection closed")
