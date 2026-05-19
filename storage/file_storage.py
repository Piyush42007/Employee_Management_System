import json
from json.decoder import JSONDecodeError
from models.employee import Employee

file_path = "data\employee.json"
#-------------------------------------------
# STORAGE
#-------------------------------------------

def load_data(file: str = file_path):
    employees = {}
    # Load Json file Data to variable data
    with open(file,"r") as f:
        try:
            try:
                data = json.load(f)
            except FileNotFoundError:
                print("FIle not found!")
                return 
        except JSONDecodeError:
                data = {} 

    # Convert data to objects and stored in dict employees (ID as key) 
    for emp_data in data.values():
            emp = Employee(emp_data["ID"],emp_data["name"],emp_data["salary"],emp_data["department"],)
            employees[emp_data["ID"]] = emp
    
    return employees


def save_data(employees,file: str = file_path):
    data = {}
    with open(file,"w") as f:
        for emp_id,emp in employees.items():
            data[emp_id] = emp.to_dict()
        json.dump(data,f , sort_keys=True, indent=2)

