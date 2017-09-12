class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = 5

    def doSomething(self):
        print("in car do something")
        return self.get_descriptive_name()

    def get_descriptive_name(self):
        print("In Car")
        long_name = str(self.year)+ ' '+self.make + ' ' + self.model + ' '+ str(self.__odometer_reading)
        return long_name

class ElectricCar(Car):
    '''ElectricCar'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.name = "Test 1 car"

    def charge(self):
        print("Electric Car is charging")

    def get_descriptive_name(self):
        print("In ElectricCar")
        long_name = str(self.year)+ ' '+self.make + ' ' + self.model
        return long_name


c = Car('audi', 'a4', 2016)
ec = ElectricCar('Tesla', 's4', 2016)
print(ec.doSomething())




