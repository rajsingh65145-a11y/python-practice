import sqlite3, csv

con = sqlite3.connect("school.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS School")
cur.execute("DROP TABLE IF EXISTS School_New")
cur.execute("""CREATE TABLE School(
    StudentID INTEGER PRIMARY KEY, Name TEXT, Class TEXT, Marks INTEGER, Age INTEGER)""")
cur.executemany("INSERT INTO School VALUES(?,?,?,?,?)", [
    (1, "Raj",   "10", 85, 15),
    (2, "Amit",  "10", 72, 16),
    (3, "Neha",  "9",  91, 14),
    (4, "Priya", "9",  78, 14),
    (5, "Karan", "10", 88, 15),
    (6, "Meena", "8",  65, 13),
    (7, "Rohit", "8",  82, 13)])
con.commit()

# 1) CSV export
cur.execute("SELECT * FROM School")
rows = cur.fetchall()
with open("school.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["StudentID", "Name", "Class", "Marks", "Age"])
    w.writerows(rows)

# 2) Marks > 80
print("Marks > 80:")
cur.execute("SELECT * FROM School WHERE Marks > 80")
for row in cur.fetchall():
    print(row)

# 3) Table delete
cur.execute("DROP TABLE School")

# 4) CSV se School_New me import
cur.execute("""CREATE TABLE School_New(
    StudentID INTEGER PRIMARY KEY, Name TEXT, Class TEXT, Marks INTEGER, Age INTEGER)""")
with open("school.csv", "r") as f:
    r = csv.reader(f)
    next(r)                                   # heading skip
    cur.executemany("INSERT INTO School_New VALUES(?,?,?,?,?)", list(r))
con.commit()

print("\nSchool_New:")
cur.execute("SELECT * FROM School_New")
for row in cur.fetchall():
    print(row)
con.close()
