class Vehicle:
    def start(self):
        print("Vehiile starts")

    def stop(self):
        print("Vehicle stops")

    def speedup(self):
        print("Vehicle speeding..")


class Car(Vehicle):
    def start(self):
        print("Car starts")

    def stop(self):
        print("Car stops")

    def honk(self):
        print("Beep beep..")

class CallingClass:
    car = Car()
    car.start()
    car.stop()
    car.speedup()
    car.honk()
