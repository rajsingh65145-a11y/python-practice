import sqlite3, csv
import matplotlib.pyplot as plt

con = sqlite3.connect("result.db")
cur = con.cursor()

# (a) table + 10 records
cur.execute("DROP TABLE IF EXISTS Result")
cur.execute("""CREATE TABLE Result(
    Rno INTEGER PRIMARY KEY, Student_name TEXT,
    IC INTEGER, CPPM INTEGER, DMA INTEGER, Maths INTEGER, CS INTEGER)""")
data = [
    (1, "Amit",   45, 40, 38, 42, 50),
    (2, "Anjali", 50, 45, 42, 48, 40),
    (3, "Bhavin", 70, 65, 60, 72, 68),
    (4, "Chirag", 35, 30, 40, 38, 44),
    (5, "Divya",  85, 90, 88, 80, 92),
    (6, "Esha",   55, 60, 58, 62, 65),
    (7, "Alpesh", 48, 44, 47, 50, 45),
    (8, "Harsh",  30, 28, 35, 33, 31),
    (9, "Isha",   75, 78, 80, 72, 77),
    (10, "Jay",   60, 58, 62, 65, 59)]
cur.executemany("INSERT INTO Result VALUES(?,?,?,?,?,?,?)", data)

# (b) Total aur Percentage column (5 subjects, har ek 100 ka)
cur.execute("ALTER TABLE Result ADD COLUMN Total INTEGER")
cur.execute("ALTER TABLE Result ADD COLUMN Percentage REAL")
cur.execute("UPDATE Result SET Total = IC + CPPM + DMA + Maths + CS")
cur.execute("UPDATE Result SET Percentage = Total / 5.0")
con.commit()

# (c) name 'A' se start + percentage 40 se 50
print("Names starting with A and percentage 40-50:")
cur.execute("SELECT Student_name, Percentage FROM Result WHERE Student_name LIKE 'A%' AND Percentage BETWEEN 40 AND 50")
for row in cur.fetchall():
    print(row)

# (d) IC aur CPPM ascending order
print("\nIC and CPPM in ascending order:")
cur.execute("SELECT IC, CPPM FROM Result ORDER BY IC ASC, CPPM ASC")
for row in cur.fetchall():
    print(row)

# (e) CSV export
cur.execute("SELECT * FROM Result")
rows = cur.fetchall()
headers = [d[0] for d in cur.description]
with open("student_results.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(rows)
print("\nCSV exported")
con.close()

# (f) CSV padhke bar chart
rno, total = [], []
with open("student_results.csv") as f:
    r = csv.DictReader(f)
    for line in r:
        rno.append(line["Rno"])
        total.append(int(line["Total"]))

plt.bar(rno, total, color="green", label="Total Marks")
plt.title("Roll No vs Total Marks")
plt.xlabel("Roll No")
plt.ylabel("Total Marks")
plt.legend()
plt.show()
