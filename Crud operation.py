student = {}

def insert_data():
    student["roll no"] = int(input("enter roll no: "))
    student["name"] = input("enter name: ")
    student["div"] = input("enter division: ")
    student["marks"] = float(input("enter marks: "))
    student["city"] = input("enter city: ") 
    
    print("\ndata inserted successfully")
    print(student)

def update_data():
    key=input("enter key to update(roll no/name/div/marks/city)")
    if key in student:
        value=input("enter new value")

        if key=="roll no":
            student[key]=int(value)
        elif key=="marks":
            student[key]=float(value)
        else:
            student[key]=value 

        print("\n data updated succesfully") 
        print(student)
    else:
        print("key not found")

def delete_data():
    key=input("enter key to delete:")
    if key in student:
        student.pop(key)
        print("\n data deleted successfully:")
        print(student)
    else:
        print("key not found")

while True:
    print("\n-----------student directory menu----") 
    print("1.insert")
    print("2.update")
    print("3.delete")
    print("4.exit")

    choice=int(input("enter your choic:e"))

    if choice==1:
        insert_data()
    elif choice==2:
        update_data()
    elif choice==3:
        delete_data()
    elif choice==4:
        print("program was ended")
        break
    else:
        print("invalid choice!")              