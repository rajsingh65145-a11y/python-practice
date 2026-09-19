import sqlite3

conn = sqlite3.connect("shop.db")
cur = conn.cursor()

cur.execute("""create table if not exists cust_muster(
    cid integer primary key,
    cname text,
    conatactno text,
    city text
)""")

cur.execute("""create table if not exists prod_master(
    pid integer primary key,
    pname text,
    company text,
    price real,
    qty integer
)""")

cur.executemany(
    "insert or ignore into prod_master values(?,?,?,?,?)",
    [
        (1, "Mouse", "logitech", 500, 20),
        (2, "keyboard", "HP", 800, 15),
        (3, "monitor", "dell", 9000, 5),
    ]
)

conn.commit()

cur.execute("select * from prod_master")

for row in cur.fetchall():
    print(row)

conn.close()
