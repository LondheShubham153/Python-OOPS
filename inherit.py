class Car:
    def __init__(self,name):
        self.wheels = 4
        self.name = name
    
    def brake(self):
        print(self.name," has stopped")
    
    def accelerate(self):
        print(self.name," is accelerating")

class MiniCar(Car):

    def __init__(self,name):
        super().__init__(name)
        pass

mini = MiniCar("nano")
print(mini.wheels)
mini.brake()
mini.accelerate()

