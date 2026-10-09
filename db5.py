import sqlite3

con = sqlite3.connect("emp.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Employee(
    emp_id INTEGER PRIMARY KEY, emp_name TEXT, contact_no TEXT,
    department_name TEXT, DOJ TEXT)""")

emps = [
 (101, "Raj",   "9000000001", "Sales",    "2020-01-10"),
 (102, "Amit",  "9000000002", "HR",       "2019-03-15"),
 (103, "Neha",  "9000000003", "IT",       "2021-07-01"),
 (104, "Priya", "9000000004", "Sales",    "2022-02-20"),
 (105, "Karan", "9000000005", "Accounts", "2018-11-05"),
 (106, "Meena", "9000000006", "IT",       "2020-09-12"),
 (107, "Rohit", "9000000007", "Sales",    "2023-04-18"),
 (108, "Sneha", "9000000008", "HR",       "2021-12-25"),
 (109, "Vijay", "9000000009", "IT",       "2019-06-30"),
 (110, "Pooja", "9000000010", "Accounts", "2022-08-08")]
cur.executemany("INSERT OR IGNORE INTO Employee VALUES(?,?,?,?,?)", emps)
con.commit()

cur.execute("SELECT * FROM Employee")
for row in cur.fetchall():       # cursor se display
    print(row)
con.close()
