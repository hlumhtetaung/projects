# class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # method
    def make_sound(self):
        pass

# subclass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# instance of the class
dog = Dog("Buddy", "Chihuahua")
cat = Cat("Whiskers", "Siamese")

# calling the method
print(f"{dog.name} says: {dog.make_sound()}")
print(f"{cat.name} says: {cat.make_sound()}")