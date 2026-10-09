import sqlite3
import matplotlib.pyplot as plt

con = sqlite3.connect("orders.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Orders")      # fresh start
cur.execute("""CREATE TABLE Orders(
    OrderID INTEGER PRIMARY KEY, CustomerName TEXT, Product TEXT,
    Quantity INTEGER, Amount REAL)""")

orders = [
 (1, "Raj",   "Laptop",    1, 45000),
 (2, "Amit",  "Mouse",     3, 1500),
 (3, "Neha",  "Phone",     2, 40000),
 (4, "Raj",   "Keyboard",  2, 3000),
 (5, "Priya", "Monitor",   1, 9000),
 (6, "Amit",  "Pen Drive", 5, 2500),
 (7, "Neha",  "Headphone", 3, 6000),
 (8, "Karan", "Bag",       2, 1800),
 (9, "Priya", "Charger",   2, 1200),
 (10, "Karan", "Tablet",   2, 15000)]
cur.executemany("INSERT INTO Orders VALUES(?,?,?,?,?)", orders)
con.commit()

# 3) Amount > 5000
print("Amount > 5000:")
cur.execute("SELECT * FROM Orders WHERE Amount > 5000")
for row in cur.fetchall():
    print(row)

# 4) Quantity < 2 delete
cur.execute("DELETE FROM Orders WHERE Quantity < 2")
con.commit()
print("Deleted rows:", cur.rowcount)

# 5) Line chart: har customer ne kitna kharch kiya
cur.execute("SELECT CustomerName, SUM(Amount) FROM Orders GROUP BY CustomerName")
res = cur.fetchall()
names  = [r[0] for r in res]
totals = [r[1] for r in res]

plt.plot(names, totals, marker="o")
plt.xlabel("Customer")
plt.ylabel("Amount Spent")
plt.title("Amount spent by each Customer")
plt.show()
con.close()
