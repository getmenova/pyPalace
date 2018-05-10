class Employee:
    def set_number_of_working_hours(self):
        self.set_number_of_working_hours = 40
    
    def display_number_of_working_hours(self):
        print(self.set_number_of_working_hours)

class Trainee(Employee):
    def set_number_of_working_hours(self):
        self.set_number_of_working_hours = 45   

    def reset_number_of_working_hours(self):
        super().set_number_of_working_hours()




employee = Employee()
employee.set_number_of_working_hours()
print('Number of working hours of employee:',end='')
employee.display_number_of_working_hours()

trainee = Trainee()
trainee.set_number_of_working_hours()
print('Number of working hours of trainee:',end='')
trainee.display_number_of_working_hours()

trainee.reset_number_of_working_hours()
print('Number of working hours of trainee:',end='')
trainee.display_number_of_working_hours()