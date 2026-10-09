# 1) Write
f = open("data.txt", "w")
f.write("Hello, ye pehli line hai\n")
f.write("Python bahut easy hai\n")
f.write("File handling mazedaar hai\n")
f.close()

# 2) Read
f = open("data.txt", "r")
print(f.read())
f.close()

# 3) Total lines
f = open("data.txt", "r")
lines = f.readlines()          # list banti hai, har line ek item
print("Total lines:", len(lines))
f.close()

# 4) First line
print("First line:", lines[0])
