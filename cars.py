# This is a class that describes a car.

class car:
     def __init__(self,model,make,year_of_production,fuel_capacity,colour):
        self.make = make
        self.model = model
        self.year_of_production = year_of_production
        self.fuel_capacity = fuel_capacity
        self.colour = colour

def print_make(self,make):
    print("The car is of {0} make".format(self.make))

my_car = car ("Ford","Mustang","195hp","16 gal","Black")
print(my_car)