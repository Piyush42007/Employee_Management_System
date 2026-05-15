from models.employee import Employee

#------------------------------------
# service functions
#------------------------------------

class Employee_service:
    @staticmethod
    def add_employee(employees: dict,emp_id: int,name: str,salary: float,department: str) -> bool:
        # return False if ID alredy exit
        if emp_id in employees:
            return False
        
        # add employee and return True
        employees[emp_id] = Employee(emp_id,name,salary,department)
        return True
        
    @staticmethod
    def view_employee(employees: dict) -> str:
        emp_view_str = "-"*50 + "\n"
        for emp in employees.values():
            emp_view_str += str(emp) + "\n" + "-"*50 + "\n"
        return emp_view_str
        
    @staticmethod
    def search_employee_by_id(employees: dict,emp_id: int) -> str|None:
        # return None if ID not exit
        if emp_id not in employees:
            return None
        # return employee data as str
        return str(employees[emp_id])

    @staticmethod
    def update_employee(employees: dict,emp_id: int,new_salary: float,new_department: str) -> bool:
        if emp_id not in employees:
            return False
        employees[emp_id].update(new_salary,new_department)
        return True

    @staticmethod
    def delete_employee(employees: dict,emp_id: int) -> bool:
        if emp_id not in employees:
            return False
        employees.pop(emp_id)
        return True