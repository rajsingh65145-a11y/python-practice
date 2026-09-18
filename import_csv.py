import csv

# File open karna - read mode mein
f2 = open("student.csv", "r")

# reader object banana
r1 = csv.reader(f2)

# row by row read karna
for row in r1:
    print(row)

# file close karna - IMPORTANT step
f2.close()
