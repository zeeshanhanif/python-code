class Car():
    def dosomething(self):
        print("car dosomething")

class AutomaticCar():
    def dosomething(self):
        print("AutomaticCar dosomething")
    def testAuto(self):
        print("AutomaticCar auto")

class ElectricalCar(AutomaticCar,Car):
    def workig(self):
        print("working")


a = Car()
b = AutomaticCar()
c = ElectricalCar()
c.dosomething()
c.testAuto()
