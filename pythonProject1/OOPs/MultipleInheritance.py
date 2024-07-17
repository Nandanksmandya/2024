class Animal:
    def speak(self):
        return "Some sound"


class Pet:
    def show_affection(self):
        return "Shows affection"


class Dog(Animal, Pet):
    def speak(self):
        return "Bark"


dog = Dog()
print(dog.speak())  # Output: Bark
print(dog.show_affection())  # Output: Shows affection
