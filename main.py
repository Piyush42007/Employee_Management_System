from storage.file_storage import load_data,save_data
from services.employee_service import EmployeeService
from utils.validation import InputValidation

#--------------------------------------------
# UI
#--------------------------------------------

def add_ui(service,valid):
    emp_id = valid.prompt_id()
    name = valid.prompt_text("Enter Name: ")
    salary = valid.prompt_salary("Enter Salary: ")
    department = valid.prompt_text("Enter Department: ")

    if service.add_employee(emp_id,name,salary,department):
        print("Employee added!")
    else:
        print("Failed! ,Employee ID alredy exit")

def view_ui(service,valid):
    print(service.view_employee())

def search_ui(service,valid):
    emp_id = valid.prompt_id()

    emp = service.search_employee_by_id(emp_id)
    if emp == None:
        print("Employee ID not Exit")
    else:
        print("-"*50)
        print(emp)
        print("-"*50)

def update_ui(service,valid):
    emp_id = valid.prompt_id()
    new_salary = valid.prompt_salary("Enter new Salary: ")
    new_department = valid.prompt_text("Enter new Department: ")

    if service.update_employee(emp_id,new_salary,new_department):
        print(f"Employee with ID: {emp_id} updated with\nSalary: {new_salary}\nDepartment: {new_department}")
    else:
        print(f"Failed! , Employee with ID: {emp_id} not exit")

def delete_ui(service,valid):
    emp_id = valid.prompt_id()

    if service.delete_employee(emp_id):
        print(f"Employee with ID: {emp_id} Deleted!")
    else:
        print(f"Failed! , Employee with ID: {emp_id} not exit")


Menu_options ={
    1:("Add Employee",add_ui),
    2:("View service",view_ui),
    3:("Search Employee",search_ui),
    4:("Update Employee",update_ui),
    5:("Delete Employee",delete_ui)
}


def menu():
    employees = load_data()
    service = EmployeeService(employees)
    valid = InputValidation()
    while True:
        print("="*50)
        print("          Employee Management System")
        print("="*50,"\n")

        print("1. Add Employee\n2. View service\n3. Search Employee\n4. Update Employee\n5. Delete Employee\n6. Exit\n")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("choose a number from above option")
            continue

        if user_choice == 6:
            break
        elif user_choice in Menu_options:
            Menu_options[user_choice][1](service,valid)




if __name__ == "__main__":
    menu()
    