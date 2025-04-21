# ASSIGNMENT 1: DESIGN YOUR OWN CLASS
# This is a Car class
class Car:
    def __init__(self, make, model, year):
        # Initialize car details
        self.make = make        # Car brand 
        self.model = model      # Car model 
        self.year = year        # Year of the car 

    def introduce(self):
        # Method to introduce the car
        print(f"I am a {self.year} {self.make} {self.model}, ready to hit the road!")

# Inheriting from Car class
class SportsCar(Car):
    def __init__(self, make, model, year, car_speed):
        # Using parent constructor to initialize the base car details
        super().__init__(make, model, year)
        self.car_speed = car_speed  

    def race(self):
        # Method to simulate racing action for a sports car
        print(f"The {self.make} {self.model} races at a speed of {self.car_speed} km/h!")

# Create Car objects
car1 = Car("Toyota", "Corolla", 2021)
car2 = SportsCar("Ferrari", "488 GTB", 2022, 330)

# Call their methods
car1.introduce()
car2.introduce()
car2.race()




# ACTIVITY 2: POLYMORPHISM CHALLENGE!
# Base class: Vehicle
class Vehicle:
    def move(self):
        print("This vehicle is moving.")

# Car class inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat class inherits from Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Objects for each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Call the move method for each vehicle
car.move()  
plane.move()  
boat.move()  
