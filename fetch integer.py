import sqlite3 as sq


conn=sq.connect('emp.db')

num=int(input("enter employee no:"))


a=conn.execute(f"select *from tblemp11 where eno={num}")


for i in a:
    print(i)


conn.close()    
