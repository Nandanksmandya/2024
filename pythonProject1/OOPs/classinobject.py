class Dogs:
    def __init__(self, name, breed, age, colour):
        self.name = name
        self.breed = breed
        self.age = age
        self.colour = colour

    #Behaviors
    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleepinggg')

    def bark(self):
        print(f'{self.name} is barking')


dog1 = Dogs("Buddy", "Labrador", 3, "black")
dog2 = Dogs("Max", "Beagle", 2, "brown")

print(f"{dog1.name} is a {dog1.age} year old {dog1.colour} {dog1.breed}.")
print(f"{dog2.name} is a {dog2.age} year old {dog2.colour} {dog2.breed}.")
dog1.eat()
dog2.sleep()
