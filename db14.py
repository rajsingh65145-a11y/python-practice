import sqlite3

con = sqlite3.connect("marks.db")
cur = con.cursor()

# ---- A. Table + 10 records ----
cur.execute("DROP TABLE IF EXISTS Marks_Sheet")
cur.execute("""CREATE TABLE Marks_Sheet
               (Roll_no INTEGER PRIMARY KEY,
                Stud_name TEXT,
                Stat_Marks INTEGER,
                Dhp_Marks INTEGER,
                Oops_Marks INTEGER)""")

data = [
    (1, "Rahul", 90, 85, 88),
    (2, "Riya", 70, 75, 80),
    (3, "Amit", 60, 65, 55),
    (4, "Neha", 95, 90, 92),
    (5, "Rohan", 80, 85, 90),
    (6, "Priya", 50, 60, 55),
    (7, "Raj", 88, 92, 85),
    (8, "Sneha", 75, 70, 72),
    (9, "Karan", 65, 60, 70),
    (10, "Ritu", 91, 89, 94)
]
cur.executemany("INSERT INTO Marks_Sheet VALUES (?,?,?,?,?)", data)
con.commit()

# ---- B. Total_marks column add karo aur calculate karo ----
cur.execute("ALTER TABLE Marks_Sheet ADD COLUMN Total_marks INTEGER")
cur.execute("UPDATE Marks_Sheet SET Total_marks = Stat_Marks + Dhp_Marks + Oops_Marks")
con.commit()

# ---- C. Total_marks 250 se zyada wale students ----
cur.execute("SELECT * FROM Marks_Sheet WHERE Total_marks > 250")
print("Total marks 250 se zyada:")
for row in cur.fetchall():
    print(row)

# ---- D. Cursor se saare records display karo ----
cur.execute("SELECT * FROM Marks_Sheet")
print("\nSaare records:")
for row in cur:                 # cursor ko seedha loop me use kar sakte hain
    print(row)

con.close()
