student=[]
n=int(input(" how many student you want add?"))

for i in range(n):
    name=input("enter student name:")
    student.append(name)

print("\noriginal list:") 
print(student)

sorted_list=sorted(student)
print("\n list in sorted order")
print(sorted_list)

count=len(student)
print("\n total number of student",count)

print("\n last 3 names in the last:")
print(student[-3::])