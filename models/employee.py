#------------------------------------------
# MODELS
#------------------------------------------

class Employee:
    def __init__(self,emp_id: str,name: str,salary: float,department: str):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def __str__(self):
        return ( f"ID: {self.emp_id}\n"
                f"Name: {self.name}\n"
                f"Salary: {self.salary}\n"
                f"Department: {self.department}"
        )

    def update(self,new_salary,new_department):
        self.salary = new_salary
        self.department = new_department

    def to_dict(self):
        return {"ID":self.emp_id,"name":self.name,"salary":self.salary,"department":self.department}