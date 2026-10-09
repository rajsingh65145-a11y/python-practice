import sqlite3, csv

con = sqlite3.connect("clinic.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Clinic")
cur.execute("DROP TABLE IF EXISTS Clinic_New")
cur.execute("""CREATE TABLE Clinic(
    DoctorID INTEGER PRIMARY KEY, DoctorName TEXT, Specialization TEXT,
    Patients INTEGER, Fees REAL)""")
cur.executemany("INSERT INTO Clinic VALUES(?,?,?,?,?)", [
    (1, "Dr. Mehta",   "Cardiology",  30, 800),
    (2, "Dr. Shah",    "Neurology",   20, 1000),
    (3, "Dr. Patel",   "Cardiology",  25, 900),
    (4, "Dr. Joshi",   "Orthopedic",  18, 700),
    (5, "Dr. Desai",   "Dermatology", 40, 500),
    (6, "Dr. Trivedi", "ENT",         22, 600)])
con.commit()

# 1) CSV export
cur.execute("SELECT * FROM Clinic")
rows = cur.fetchall()
with open("clinic.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["DoctorID", "DoctorName", "Specialization", "Patients", "Fees"])
    w.writerows(rows)

# 2) Cardiology doctors
print("Cardiology doctors:")
cur.execute("SELECT * FROM Clinic WHERE Specialization = 'Cardiology'")
for row in cur.fetchall():
    print(row)

# 3) Table drop
cur.execute("DROP TABLE Clinic")

# 4) Data wapas Clinic_New me
cur.execute("""CREATE TABLE Clinic_New(
    DoctorID INTEGER PRIMARY KEY, DoctorName TEXT, Specialization TEXT,
    Patients INTEGER, Fees REAL)""")
with open("clinic.csv", "r") as f:
    r = csv.reader(f)
    next(r)
    cur.executemany("INSERT INTO Clinic_New VALUES(?,?,?,?,?)", list(r))
con.commit()

print("\nClinic_New:")
cur.execute("SELECT * FROM Clinic_New")
for row in cur.fetchall():
    print(row)
con.close()
