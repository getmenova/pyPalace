class RentCar:
    def __init__(self):
        self.car_list = {'Hatchback':30,'Sedan':50,'SUV':100}

    def display_details(self):
        print("Cost per day: ")
        print("Hatchback $",self.car_list['Hatchback'])
        print('Sedan $',self.car_list['Sedan'])
        print('SUV $',self.car_list['SUV'])
    
    def calculate_price(self,name_car,days):
        if name_car in self.car_list:
            return days * self.car_list[name_car]
            if days>0:
                print('Error. days needs to be more than 0')
        else:
            print('Sorry, this car is not in our list')
    
class Customer:
    def rent_car(self,car):
        self.car_list.remove(car_list[car])
        print('Rent with success')
        
        
car = RentCar()
customer = Customer()
car.display_details()

while True:
    print('''
        Enter 1 to display the list of avaliable cars
        Enter 2 to rent a car
        Enter 3 to quit
    ''')
    user_choice = int(input())
    if user_choice is 1:
        car.display_details()

    elif user_choice is 2:
        car_name = input('Enter with the name of the car you want :')
        days = int(input('Enter the number of days you would like to borrow the car:'))
        total_price = car.calculate_price(car_name,days)
        print('The price will be : {}'.format(total_price))
    elif user_choice is 3:
        quit()