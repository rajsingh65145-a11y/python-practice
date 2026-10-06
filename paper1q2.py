import sqlite3

con = sqlite3.connect("college.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Students(
    roll_no INTEGER PRIMARY KEY, s_name TEXT,
    subject1 INTEGER, subject2 INTEGER, subject3 INTEGER)""")
con.commit()

def insert_record():
    r = int(input("Roll no: "))
    n = input("Name: ")
    s1 = int(input("Subject1: "))
    s2 = int(input("Subject2: "))
    s3 = int(input("Subject3: "))
    cur.execute("INSERT INTO Students VALUES(?,?,?,?,?)", (r, n, s1, s2, s3))
    con.commit()
    print("Record inserted")

def display_all():
    cur.execute("SELECT * FROM Students")
    for row in cur:                      # cursor ko loop mein use kiya
        print(row)

def highest_sub1():
    cur.execute("SELECT * FROM Students WHERE subject1 = (SELECT MAX(subject1) FROM Students)")
    for row in cur.fetchall():
        print("Topper in subject1:", row)

while True:
    print("\n1. Insert\n2. Display All\n3. Highest in Subject1\n4. Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        insert_record()
    elif ch == 2:
        display_all()
    elif ch == 3:
        highest_sub1()
    elif ch == 4:
        break
    else:
        print("Wrong choice")
con.close()
