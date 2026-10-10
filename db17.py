import sqlite3
import csv
import matplotlib.pyplot as plt

con = sqlite3.connect("company.db")
cur = con.cursor()

# ---- Tables banao ----
cur.execute("DROP TRIGGER IF EXISTS del_emp")
cur.execute("DROP TABLE IF EXISTS tblEmployee")
cur.execute("DROP TABLE IF EXISTS tblDepartment")

cur.execute("""CREATE TABLE tblDepartment
               (DeptID INTEGER PRIMARY KEY,
                DeptName TEXT)""")
cur.execute("""CREATE TABLE tblEmployee
               (EmpID INTEGER PRIMARY KEY,
                Name TEXT,
                City TEXT,
                Salary INTEGER,
                DeptID INTEGER)""")

# ---- Records insert ----
depts = [(1, "HR"), (2, "Marketing"), (3, "IT"), (4, "Finance"), (5, "Admin")]
cur.executemany("INSERT INTO tblDepartment VALUES (?,?)", depts)

emps = [
    (1, "Amit", "Surat", 45000, 2),
    (2, "Neha", "Mumbai", 38000, 2),
    (3, "Raj", "Ahmedabad", 52000, 2),
    (4, "Priya", "Pune", 30000, 1),
    (5, "Karan", "Delhi", 42000, 3),
    (6, "Sneha", "Surat", 60000, 3),
    (7, "Rohan", "Vadodara", 35000, 4),
    (8, "Riya", "Rajkot", 48000, 4),
    (9, "Ritu", "Surat", 25000, 5),
    (10, "Vivek", "Mumbai", 41000, 3)
]
cur.executemany("INSERT INTO tblEmployee VALUES (?,?,?,?,?)", emps)
con.commit()

# ---- A. Trigger: department delete hote hi uske employees delete ----
cur.execute("""CREATE TRIGGER del_emp
               AFTER DELETE ON tblDepartment
               BEGIN
                   DELETE FROM tblEmployee WHERE DeptID = OLD.DeptID;
               END;""")
con.commit()
print("Trigger ban gaya")

# ---- B. Pie chart: har department me kitne employees ----
cur.execute("""SELECT d.DeptName, COUNT(e.EmpID)
               FROM tblDepartment d
               JOIN tblEmployee e ON d.DeptID = e.DeptID
               GROUP BY d.DeptName""")
data = cur.fetchall()
names = [row[0] for row in data]     # department ke naam
counts = [row[1] for row in data]    # employees ki ginti
plt.pie(counts, labels=names, autopct="%1.1f%%")   # % ke saath pie
plt.title("Employee Distribution in Departments")
plt.show()

# ---- C. Marketing ke employees jinki salary > 40000, csv me export ----
cur.execute("""SELECT e.EmpID, e.Name, e.City, e.Salary
               FROM tblEmployee e
               JOIN tblDepartment d ON e.DeptID = d.DeptID
               WHERE d.DeptName = 'Marketing' AND e.Salary > 40000""")
rows = cur.fetchall()
print("\nMarketing employees (Salary > 40000):")
for row in rows:
    print(row)

with open("marketing_employees.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["EmpID", "Name", "City", "Salary"])
    w.writerows(rows)
print("marketing_employees.csv ban gayi")

# ---- Trigger test (examiner ko dikhane ke liye) ----
cur.execute("DELETE FROM tblDepartment WHERE DeptID = 5")   # Admin delete
con.commit()
cur.execute("SELECT * FROM tblEmployee")
print("\nAdmin delete ke baad employees (Ritu gayab hona chahiye):")
for row in cur.fetchall():
    print(row)

con.close()
