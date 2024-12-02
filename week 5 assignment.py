
"""Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation."""

class Smartphone:
    def __init__(self, contact_number, app_name):
        self.contact_number = contact_number
        self.app_name = app_name

    def make_call(self):
        if self.contact_number:
            return f"call to {self.contact_number} has been initiated successfully."
        else:
            return f"failed to place the call"
    
    def install_app(self):
        if self.app_name:
            return f"{self.app_name} has been successfully installed"
        else:
            return f"there was an error trying to install the app"


contact = "+254738469372"
app = "FaceBook"
phone_instance = Smartphone(contact, app)
print(phone_instance.make_call())
print(phone_instance.install_app())


"""Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each 
class define move() differently (for example, Car.move() prints "Driving" 🚗, 
while Plane.move() prints "Flying" ✈️)."""

class Cow:
    def move(self):
        print("Walk")

class Bird:
    def move(self):
        print("Fly")
    
cow1 = Cow()
bird1 = Bird()
cow1.move()
bird1.move()