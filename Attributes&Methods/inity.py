class Employee:
    def __init__(self,name):
        self.name = name


    def display_employee_details(self):
        print(self.name)

employee = Employee("Mike")
employee.display_employee_details()

employee_two = Employee("Maggie")
employee_two.display_employee_details()
