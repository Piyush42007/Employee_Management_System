from models.employee import Employee
from storage.file_storage import save_data

#------------------------------------
# service functions
#------------------------------------

class EmployeeService:
    def __init__(self,storage: dict) -> None:
        self.storage =storage

    def add_employee(self,emp_id: int,name: str,salary: float,department: str) -> bool:
        # return False if ID alredy exit
        if emp_id in self.storage:
            return False
        
        # add employee and return True
        self.storage[emp_id] = Employee(emp_id,name,salary,department)
        save_data(self.storage)
        return True
        
    def view_employee(self) -> str:
        if not self.storage:
            return "No Employee found!"
        emp_view_str = "-"*50 + "\n"    
        for emp in self.storage.values():
            emp_view_str += str(emp) + "\n" + "-"*50 + "\n"
        return emp_view_str
        
    def search_employee_by_id(self,emp_id: int) -> str|None:
        # return None if ID not exit
        if emp_id not in self.storage:
            return None
        # return employee data as str
        return str(self.storage[emp_id])

    def update_employee(self,emp_id: int,new_salary: float,new_department: str) -> bool:
        if emp_id not in self.storage:
            return False
        self.storage[emp_id].update(new_salary,new_department)
        save_data(self.storage)
        return True

    def delete_employee(self,emp_id: int) -> bool:
        if emp_id not in self.storage:
            return False
        self.storage.pop(emp_id)
        save_data(self.storage)
        return True