import os

FileName="employee.txt"
def add_record():
    Employee_ID=input("Enter Employee ID: ")
    Name=input("Enter Name: ")
    Position=input("Enter Position: ")
    Salary=input("Enter Salary: ")
    with open(FileName,'a') as file:
        file.write(f"{Employee_ID},{Name},{Position},{Salary}\n")
    print("Record Added")
def view_records():
   with open(FileName,'r') as file:
       for line in file:
           print(line)
def search_employees():
    Id=input("Enter Employee ID: ")

    with open(FileName,'r') as file:
        lines=file.readlines()
    for a in lines:
        if a.startwith(Id+","):
            print("\nRecord Found:")
            print(a.strip())
            return
    print("\nNo records found.")
def update_record():
    Employee_ID=input("Enter Employee ID: ")
    newdata=[]
    found=False
    with open(FileName,'r') as file:
        lines=file.readlines()
        for a in lines:
            data=a.strip().split(",")
            if a.startswith(Employee_ID+","):
                found=True
                print("\nRecord found")
                name =input("Enter Name: ") or data[2]
                position =input("Enter Position: ") or data[3]
                salary =input("Enter Salary: ") or data[4]
                new_record=f"{Employee_ID},{name},{position},{salary}\n"
                newdata.append(new_record)
            else:
                newdata.append(a)

        if not found:
            print("\nNo records found.")
            return
        with open(FileName,'w') as file:
            file.writelines(newdata)
        print("\nRecord Updated")
def delete_record():
    Employee_ID=input("Enter Employee ID: ")
    found=False
    newdata=[]
    with open(FileName,'r') as file:
        lines=file.readlines()
        for a in lines:
            if not a.startswith(Employee_ID+","):
                newdata.append(a)
            else:
                found=True
    with open(FileName,'w') as file:
        file.writelines(newdata)
        print("\nRecord Deleted")

def main():
    while True:

        print("\nWelcome to Employee Recors Manager")
        value=input("\n1. Add new employee record\n\
    2  . View all employee records\n\
    3. Search for an employee by Employee ID\n\
    4. Update an employee's information\n\
    5. Delete an employee record\n\
    6. Exit\n Enter your choice: ")
        if value== "1":
            add_record()
        elif value== "2":
            view_records()
        elif value== "3":
            search_employees()
        elif value== "4":
            update_record()
        elif value== "5":
            delete_record()
        elif value== "6":
            break
        else:
            print("Invalid choice, please try again.")

main()



