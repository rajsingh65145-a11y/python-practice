import sqlite3, csv

# (a) table banao aur connection close karo
con = sqlite3.connect("college.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Student")
cur.execute("""CREATE TABLE Student(
    roll_no INTEGER PRIMARY KEY,
    name TEXT(20),
    city TEXT(20),
    age INTEGER)""")
con.commit()
con.close()

# (b) dobara connect karke 10 records
con = sqlite3.connect("college.db")
cur = con.cursor()
data = [
    (1, "Amit",   "Navsari", 20),
    (2, "Bhavin", "Surat",   21),
    (3, "Chirag", "Navsari", 19),
    (4, "Divya",  "Vyara",   20),
    (5, "Esha",   "Navsari", 22),
    (6, "Farhan", "Surat",   21),
    (7, "Gita",   "Navsari", 20),
    (8, "Harsh",  "Bardoli", 19),
    (9, "Isha",   "Navsari", 21),
    (10, "Jay",   "Valsad",  20)]
cur.executemany("INSERT INTO Student VALUES(?,?,?,?)", data)
con.commit()

# (c) course column add + city Navsari aur course BCA wale students
cur.execute("ALTER TABLE Student ADD COLUMN course TEXT")
cur.execute("UPDATE Student SET course = 'BCA' WHERE roll_no IN (1,3,5,9)")
cur.execute("UPDATE Student SET course = 'BBA' WHERE course IS NULL")
con.commit()

print("Navsari + BCA students:")
cur.execute("SELECT * FROM Student WHERE city = 'Navsari' AND course = 'BCA'")
for row in cur.fetchall():
    print(row)

# (d) database ko sql file mein dump karo
with open("student_table.sql", "w") as f:
    for line in con.iterdump():
        f.write(line + "\n")
print("\nstudent_table.sql created")

# (e) CSV export + IDLE mein display
cur.execute("SELECT * FROM Student")
rows = cur.fetchall()
headers = [d[0] for d in cur.description]
with open("student.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(rows)

print("\nCSV file data:")
with open("student.csv") as f:
    print(f.read())
con.close()
