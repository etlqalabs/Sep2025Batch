class Vehicle:
    def start(self):
        print("Vehicle starts...")

    def stop(self):
        print("Vehicle stops...")

class Car:

    def start(self):
        print("Car starts...")

    def stop(self):
        print("Car stops...")

    def honk(self):
        print("Beep beep")

class Bike(Car,Vehicle):
    pass

# Initaiting classes

bike = Bike()
bike.start()
bike.stop()
bike.honk()