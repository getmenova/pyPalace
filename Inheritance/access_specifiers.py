class Car:
    numberOfWheels = 4
    _color = "Black"
    __year_of_manufacture = 2017 #_Car__year_of_manufacture

    def show_year_of_manufacture(self):
        return self.__year_of_manufacture


class Bmw(Car):
    def __init__(self):
        print("Protected attribute color: ",self._color)




car = Car()
bmw = Bmw()
print("Public attribute number of wheels",car.numberOfWheels)
print("Private attribute yearOfManufacture: ",car.show_year_of_manufacture())
