class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Bird(Animal):
    def __init__(self, name, colour):
        super().__init__(name)
        self.colour = colour

    def speak(self):
        return "Good sound"


class Dog(Bird):
    def __init__(self, name, colour, breed):
        super().__init__(name, colour)
        self.breed = breed

    def speak(self):
        return "Bark"


dog = Dog("Buddy", "Brown", "Golden Retriever")
print(f'{dog.name} is a {dog.breed} with {dog.colour} fur and say {dog.speak()}')
