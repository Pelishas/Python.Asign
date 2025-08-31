# ssignment 1: Design Your Own Class! 🏗️
# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.
# Activity 2: Polymorphism Challenge! 🎭


class Smartphone:
  def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

Phone1 = Smartphone("Apple", "iPhone 13", "128GB")
Phone2 = Smartphone("Samsung", "Galaxy S21", "256GB")
Phone3 = Smartphone("Google", "Pixel 6", "128GB")
Phone4 = Smartphone("OnePlus", "9 Pro", "256GB")

print(Phone2.brand, Phone2.model, Phone2.storage)
print(Phone4.brand, Phone4.model, Phone4.storage)
print(Phone1.brand, Phone1.model, Phone1.storage)

class TheatreTalent:
    def perform(self):
        return "Generic performance"

class Singer(TheatreTalent):
    def perform(self):
        return "Singing Pop music"

class Dancer(TheatreTalent):
    def perform(self):
        return "Performing Hip Hop dance"

class Actor(TheatreTalent):
    def perform(self):
        return "Acting in a drama"

class Musician(TheatreTalent):
    def perform(self):
        return "Playing rumba"

# Demonstrating polymorphism
talents = [Singer(), Dancer(), Actor(), Musician()]
for talent in talents:
    print(talent.perform())
