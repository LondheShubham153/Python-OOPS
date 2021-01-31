class Car:
    def __init__(self,name):
        self.wheels = 4
        self.name = name
    
    def brake(self):
        print(self.name," has stopped for big car")
    
    def accelerate(self):
        print(self.name," is accelerating")

class MiniCar(Car):

    def __init__(self,name):
        super().__init__(name)
        pass
    
    def brake(self):
        print(self.name," has stopped for mini car")

def use_brakes(car):  #DMD
    car.brake()

big_car = Car("Audi")
mini_car = MiniCar("Reva")

#using big car
use_brakes(big_car)

#using mini car
use_brakes(mini_car)
