import csv, sqlite3

# 1) writer object se 5 records
with open("product.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["pid", "pname", "category", "price"])
    w.writerow([1, "Pen", "Stationery", 10])
    w.writerow([2, "Notebook", "Stationery", 60])
    w.writerow([3, "Bag", "Accessories", 450])
    w.writerow([4, "Mouse", "Electronics", 500])
    w.writerow([5, "Marker", "Stationery", 80])

# 2) reader object se read
with open("product.csv", "r") as f:
    r = csv.reader(f)
    next(r)                 # heading line skip
    data = list(r)
    for row in data:
        print(row)

# 3) SQLite table "Product" me insert
con = sqlite3.connect("product.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Product(
    pid INTEGER PRIMARY KEY, pname TEXT, category TEXT, price REAL)""")
cur.executemany("INSERT OR IGNORE INTO Product VALUES(?,?,?,?)", data)
con.commit()

# 4) price > 70
print("\nPrice > 70:")
cur.execute("SELECT * FROM Product WHERE price > 70")
for row in cur.fetchall():
    print(row)
con.close()
