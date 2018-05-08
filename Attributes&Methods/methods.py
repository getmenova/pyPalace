class Employee:
    def employeeDetails(self):
        self.name = "Mike"
    @staticmethod
    def welcome_message():
        print('Hallo, Hello, Hi *beep*')

employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcome_message()
