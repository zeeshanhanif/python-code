from car import Car
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

