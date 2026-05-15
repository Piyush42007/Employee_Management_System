from storage.file_storage import Employee_storage
from services.employee_service import Employee_service
from utils.validation import Input_validation as valid

#--------------------------------------------
# UI
#--------------------------------------------

def add_ui(employees):
    emp_id = valid.prompt_id()
    name = valid.prompt_text("Enter Name: ")
    salary = valid.prompt_salary("Enter Salary: ")
    department = valid.prompt_text("Enter Department: ")

    if Employee_service.add_employee(employees,emp_id,name,salary,department):
        Employee_storage.save_data(employees)
        print("Employee added!")
    else:
        print("Failed! ,Employee ID alredy exit")

def view_ui(employees):
    print(Employee_service.view_employee(employees))

def search_ui(employees):
    emp_id = valid.prompt_id()

    if Employee_service.search_employee_by_id(employees,emp_id) == None:
        print("Employee ID not Exit")
    else:
        print("-"*50)
        print(Employee_service.search_employee_by_id(employees,emp_id))
        print("-"*50)

def update_ui(employees):
    emp_id = valid.prompt_id()
    new_salary = valid.prompt_salary("Enter new Salary: ")
    new_department = valid.prompt_text("Enter new Department: ")

    if Employee_service.update_employee(employees,emp_id,new_salary,new_department):
        Employee_storage.save_data(employees)
        print(f"Employee with ID: {emp_id} updated with\nSalary: {new_salary}\nDepartment: {new_department}")
    else:
        print(f"Failed! , Employee with ID: {emp_id} not exit")

def delete_ui(employee):
    emp_id = valid.prompt_id()

    if Employee_service.delete_employee(employee,emp_id):
        Employee_storage.save_data(employee)
        print(f"Employee with ID: {emp_id} Deleted!")
    else:
        print(f"Failed! , Employee with ID: {emp_id} not exit")


Menu_options ={
    1:("Add Employee",add_ui),
    2:("View Employees",view_ui),
    3:("Search Employee",search_ui),
    4:("Update Employee",update_ui),
    5:("Delete Employee",delete_ui)
}


def menu():
    employees = Employee_storage.load_data()
    while True:
        print("="*50)
        print("          Employee Management System")
        print("="*50,"\n")

        print("1. Add Employee\n2. View Employees\n3. Search Employee\n4. Update Employee\n5. Delete Employee\n6. Exit\n")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("choose a number from above option")
            continue

        if user_choice == 6:
            break
        elif user_choice in Menu_options:
            Menu_options[user_choice][1](employees)




menu()
    