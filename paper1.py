import sqlite3

conn=sqlite3.connect("college.db")
cur=conn.cursor()


cur.execute("create table if not exists students(roll no intger primary key, name text,subject1 integer, subject2 integer ,subject3 integer)")


data=[
    (1,"Amit",45,60,70),
    (2, "Bhavin", 78, 66, 54),
    (3, "Chirag", 32, 48, 59),
    (4, "Divya",  88, 91, 79),
    (5, "Esha",   55, 62, 68),
    (6, "Farhan", 67, 70, 72),
    (7, "Gita",   91, 85, 90),
    (8, "Harsh",  40, 35, 44),
    (9, "Isha",   73, 77, 80),
    (10, "Jay",   60, 58, 65)]

cur.executemany("insert or ignore into students values(?,?,?,?,?)",data)
conn.commit()



def getdata(min,max):
    cur.execute("select * from students where subject1 between ? and ?",(min,max))
    rows=cur.fetchall()
    print("Rollno Name sub1 sub2 sub3")
    for r in rows:
        print(r)


lo=int(input("enter min marks:"))
hi=int(input("enter max marks:"))
getdata(lo,hi)
conn.close()
