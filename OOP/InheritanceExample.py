class Vehicle:
    def start(self):
        print("Vehicle starts...")

    def stop(self):
        print("Vehicle stops...")

class Car(Vehicle):
    seating_capacity=4

    def honk(self):
        print("Beep beep")

class Bike(Vehicle):
    seating_capacity = 2

# Initaiting classes
print("Vehicle class .....")
vehicle = Vehicle()
vehicle.start()
vehicle.stop()

print("Car class .....")
car =  Car()
print(car.seating_capacity)
car.honk()
car.start()
car.stop()


