employees = []

def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    salary = float(input("Enter employee salary: "))
    employee = {'name': name, 'age': age, 'salary': salary}
    employees.append(employee)
    print("Employee added successfully!")

def display_employees():
    if not employees:
        print("No employees are there to represent")
    else:
        print("List of Employees:")
        for employee in employees:
            print(f"Name: {employee['name']}, Age: {employee['age']}, Salary: {employee['salary']}")

def search_employee():
    name = input("Enter employee name to search: ")
    found = False
    for employee in employees:
        if employee['name'] == name:
            print(f"Employee found - Name: {employee['name']}, Age: {employee['age']}, Salary: {employee['salary']}")
            found = True
            break
    if not found:
        print("Employee not found.")

def remove_employee():
    name = input("Enter employee name to remove: ")
    for employee in employees:
        if employee['name'] == name:
            employees.remove(employee)
            print("Employee removed successfully!")
            break
    else:
        print("Employee not found.")

def menu():
    print("Employee Management System")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Remove Employee")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5):")
        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            remove_employee()
        elif choice == '5':
            print("Exiting")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
