class Car():

    def __init__(self,make,model,year,battery):
        self.make = make
        self.model = model
        self.year = year
        self.battery =  battery
        self.__odometer_reading = 5



    def get_descriptive_name(self):
        print("In Car")
        long_name = str(self.year)+ ' '+self.make + ' ' + self.model + ' '+ str(self.__odometer_reading)
        return long_name


class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

b = Battery()
c = Car('audi', 'a4', 2016, b)
c.battery.describe_battery()





