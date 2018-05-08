class Employee:
    def employeeDetails(self):
        self.name = 'Nova'
        self.age = 99
        print("Name = {}".format(self.name))
        print("Age = ",self.age)

    def print_employee_details(self):
        print("Printing in another method :")
        print("Name:",self.name)
        print("Age:",self.age)


employee = Employee()
employee.employeeDetails()
employee.age
employee.print_employee_details()
