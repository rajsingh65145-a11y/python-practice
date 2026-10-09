import sqlite3

con = sqlite3.connect("emp.db")
cur = con.cursor()

while True:
    print("\n1. Sales department ki details")
    print("2. Employee (emp_id = 105) ki details")
    print("3. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        cur.execute("SELECT * FROM Employee WHERE department_name = 'Sales'")
        for row in cur.fetchall():
            print(row)
    elif ch == "2":
        cur.execute("SELECT * FROM Employee WHERE emp_id = 105")
        print(cur.fetchone())
    elif ch == "3":
        break
    else:
        print("Wrong choice")
con.close()
