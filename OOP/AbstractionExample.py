from abc import ABC, abstractmethod

class Vehicle(ABC):
    def start(self):
        print("Vehicle starts...")

    def stop(self):
        print("Vehicle stops...")

    @abstractmethod
    def fly(self):
        pass

class AirPlane(Vehicle):
    def fly(self):
        print("Air plane flies")


airplane = AirPlane()
airplane.start()
airplane.stop()
airplane.fly()
