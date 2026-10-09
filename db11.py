
import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect("sales.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Sales")
cur.execute("""CREATE TABLE Sales(
    SalesID INTEGER PRIMARY KEY, Item TEXT, Region TEXT,
    Quantity INTEGER, Revenue REAL)""")

sales = [
 (1, "Laptop",   "North", 10, 50000),
 (2, "Mouse",    "South", 30, 9000),
 (3, "Keyboard", "East",  25, 12500),
 (4, "Monitor",  "North", 22, 33000),
 (5, "Printer",  "West",  8,  24000),
 (6, "Phone",    "South", 15, 60000),
 (7, "Tablet",   "East",  12, 36000),
 (8, "Charger",  "North", 40, 8000),
 (9, "Speaker",  "West",  21, 10500),
 (10, "Camera",  "South", 5,  25000)]
cur.executemany("INSERT INTO Sales VALUES(?,?,?,?,?)", sales)
con.commit()

# 3) North region
print("North region sales:")
cur.execute("SELECT * FROM Sales WHERE Region = 'North'")
for row in cur.fetchall():
    print(row)

# 4) Quantity > 20 wale sab ka Revenue + 1000
cur.execute("UPDATE Sales SET Revenue = Revenue + 1000 WHERE Quantity > 20")
con.commit()
print("Updated rows:", cur.rowcount)

# 5) Bar chart: region-wise total revenue
cur.execute("SELECT Region, SUM(Revenue) FROM Sales GROUP BY Region")
res = cur.fetchall()
plt.bar([r[0] for r in res], [r[1] for r in res], color="orange")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.title("Total Revenue by Region")
plt.show()
con.close()
