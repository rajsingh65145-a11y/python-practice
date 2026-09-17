import sqlite3

conn=sqlite3.connect('college.db')
print("database successfully created")


conn.execute("create table if not exists tblstudent09(rollno int primary key, name text, gender text, marks integer)")
print("Table successfully created")


e1=int(input("enter roll no:"))
e2=input("enter student name:")
e3=input("enter gender:")
e4=int(input("enter marks:"))


conn.execute(f"insert into tblstudent09 values{e1,e2,e3,e4}")
print("record successfully inserted")



conn.commit()
conn.close()


conn.execute("select *from tblstudent09")
