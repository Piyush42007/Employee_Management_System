class InputValidation():
    @staticmethod
    def prompt_id(prompt: int = "Enter ID: "):
        while True:
            try:
                value = int(input(prompt))
            except ValueError:
                print("ID should be a Positive number")
                continue
            
            if value > 0:
                return value
            else:
                print("ID should be a Positive number")
                continue

    @staticmethod     
    def prompt_text(prompt):
        while True:
            value = input(prompt).title()
            if not value:
                print("This field can't be empty")
                continue
            return value
    @staticmethod
    def prompt_salary(prompt):
        while True:
            try:
                value = float(input(prompt))
            except ValueError:
                print("Invalid Input!")
                continue
            
            if value > 0:
                return value
            else:
                print("Salary should above zero")
                continue
