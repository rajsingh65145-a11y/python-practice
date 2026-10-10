import sqlite3                      # database ke liye
import csv                          # csv export ke liye

con = sqlite3.connect("medicine.db")   # database banao / kholo
cur = con.cursor()                     # cursor se queries chalti hain

# ---- A. Table banao aur 10 records daalo ----
cur.execute("DROP TABLE IF EXISTS Medicine")   # dobara run karne par error na aaye
cur.execute("""CREATE TABLE Medicine
               (Med_Id INTEGER PRIMARY KEY,
                Med_Name TEXT,
                Qty INTEGER,
                Rate REAL)""")

data = [
    (1, "Crocin", 10, 25.0),
    (2, "Dolo 650", 20, 30.0),
    (3, "Cetirizine", 15, 12.5),
    (4, "Azithromycin", 5, 90.0),
    (5, "Calpol", 12, 28.0),
    (6, "Paracetamol", 30, 15.0),
    (7, "Combiflam", 8, 40.0),
    (8, "Cipla Cold", 6, 55.0),
    (9, "Vicks Action", 10, 35.0),
    (10, "Pantoprazole", 14, 60.0)
]
cur.executemany("INSERT INTO Medicine VALUES (?,?,?,?)", data)  # saare records ek saath
con.commit()                                                     # save karo
print("Table ban gayi aur 10 records insert ho gaye")

# ---- B. Total column add karo aur calculate karo ----
cur.execute("ALTER TABLE Medicine ADD COLUMN Total REAL")   # naya column
cur.execute("UPDATE Medicine SET Total = Qty * Rate")       # Total = Qty x Rate
con.commit()

# ---- C. Jin medicine ka naam 'C' se start hota hai ----
cur.execute("SELECT * FROM Medicine WHERE Med_Name LIKE 'C%'")
print("\nC se start hone wali medicines:")
for row in cur.fetchall():          # saari rows ek ek karke
    print(row)

# ---- D. Poora table medicines.csv me export karo ----
cur.execute("SELECT * FROM Medicine")
rows = cur.fetchall()
headers = [d[0] for d in cur.description]       # column ke naam
with open("medicines.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(headers)                         # pehle heading
    w.writerows(rows)                           # phir saara data
print("\nmedicines.csv ban gayi")

con.close()                                     # connection band
