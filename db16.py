import sqlite3
import csv

con = sqlite3.connect("books.db")
cur = con.cursor()

# ---- A. Table banao ----
cur.execute("DROP TABLE IF EXISTS tblBooks")
cur.execute("""CREATE TABLE tblBooks
               (BookID INTEGER PRIMARY KEY,
                Title TEXT,
                Author TEXT,
                Subject TEXT,
                Price REAL)""")

# ---- B. 10 records insert ----
books = [
    (1, "Learning Python", "Mark Lutz", "Python", 750),
    (2, "Python Crash Course", "Eric Matthes", "Python", 500),
    (3, "Python Basics", "Ravi Kumar", "Python", 300),
    (4, "Let Us C", "Yashavant Kanetkar", "C", 400),
    (5, "Java Complete", "Herbert Schildt", "Java", 650),
    (6, "DBMS Concepts", "Korth", "Database", 550),
    (7, "Automate Boring Stuff", "Al Sweigart", "Python", 450),
    (8, "HTML and CSS", "Jon Duckett", "Web", 350),
    (9, "Python for Beginners", "Amit Shah", "Python", 250),
    (10, "Data Structures", "Seymour Lipschutz", "DS", 380)
]
cur.executemany("INSERT INTO tblBooks VALUES (?,?,?,?,?)", books)
con.commit()

# ---- C. Python subject ki books jinki Price > 350 ----
cur.execute("SELECT * FROM tblBooks WHERE Subject = 'Python' AND Price > 350")
print("Python books (Price > 350):")
for row in cur.fetchall():
    print(row)

# ---- D. CSV me export karo ----
cur.execute("SELECT * FROM tblBooks")
rows = cur.fetchall()
headers = [d[0] for d in cur.description]
with open("books.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(rows)

# ---- CSV wapas read karke IDLE me dikhao ----
print("\nCSV file ka data:")
with open("books.csv", "r") as f:
    r = csv.reader(f)
    for line in r:
        print(line)

con.close()
