import sqlite3

# step 1: creating new database
     
conn=sqlite3.connect('emp.db')

print("database successfully conected")

# step 2: creating table

conn.execute("create table tblemp11(eno int primary key,ename text,gender text,jdate text,salary integer)")
print("table successfully created")


# step 3: insert multiple records      

conn.execute("insert into tblemp11 values(1,'rohit','M','2001-12-21',24000)")
conn.execute("insert into tblemp11 values(2,'karan','M','2007-9-11',50000)")  
conn.execute("insert into tblemp11 values(3,'harsh','M','2006-3-11',60000)")
conn.execute("insert into tblemp11 values(4,'laksh','M','2008-8-2',70000)")
conn.commit()
print("record successfully inserted")


#step 4: fetchone() is used

a=conn.execute("select * from tblemp11")
b=a.fetchone()
print(b)

print("emp id:",b[0])
print("emp name:",b[1])

c=a.fetchone()
print(c)

conn.close()




