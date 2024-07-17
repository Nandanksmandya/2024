class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Bark"


class Cat(Animal):
    def speak(self):
        return "Meow"


dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Bark
print(cat.speak())  # Output: Meow
