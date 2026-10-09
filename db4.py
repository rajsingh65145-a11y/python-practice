import sqlite3, csv

con = sqlite3.connect("shop.db")
cur = con.cursor()

# 1) Column add (purane rows me email_id NULL rahega)
try:
    cur.execute("ALTER TABLE Cust_Master ADD COLUMN email_id TEXT")
except sqlite3.OperationalError:
    print("email_id column pehle se hai")
con.commit()

# 2) Sab customers ka CSV
cur.execute("SELECT * FROM Cust_Master")
rows = cur.fetchall()
headers = [d[0] for d in cur.description]   # column ke naam

with open("customers.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(headers)     # pehli line = heading
    w.writerows(rows)       # baaki sab rows
print("customers.csv ban gayi")
con.close()
