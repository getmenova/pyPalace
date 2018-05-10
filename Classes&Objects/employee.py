class Employee:
    name = "Mike"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    def has_achieved_target(self):
        if self.salesMadeThisWeek >=5:
            print('Target has been achieved')
            return True
        else:
            print('Target has not been achieved')
            return False

employeeOne = Employee()
print(employeeOne.name,end=' ')
print(employeeOne.has_achieved_target())  