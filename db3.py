import sqlite3

con = sqlite3.connect("shop.db")   # database file ban jayegi
cur = con.cursor()                 # cursor se queries chalti hain

cur.execute("""CREATE TABLE IF NOT EXISTS Cust_Master(
    Cid INTEGER PRIMARY KEY, CName TEXT, ContactNo TEXT, City TEXT)""")
cur.execute("""CREATE TABLE IF NOT EXISTS Prod_Master(
    Pid INTEGER PRIMARY KEY, PName TEXT, Company TEXT, Price REAL, Qty INTEGER)""")

# OR IGNORE: dobara run karne pe error nahi aayega
cur.executemany("INSERT OR IGNORE INTO Cust_Master VALUES(?,?,?,?)", [
    (1, "Raj", "9876543210", "Surat"),
    (2, "Amit", "9123456780", "Vadodara"),
    (3, "Neha", "9988776655", "Rajkot")])
cur.executemany("INSERT OR IGNORE INTO Prod_Master VALUES(?,?,?,?,?)", [
    (1, "Mouse", "Logitech", 500, 20),
    (2, "Keyboard", "HP", 800, 15),
    (3, "Monitor", "Dell", 9000, 5)])
con.commit()                       # save

# B: Prod_Master ka data
cur.execute("SELECT * FROM Prod_Master")
for row in cur.fetchall():
    print(row)
con.close()
