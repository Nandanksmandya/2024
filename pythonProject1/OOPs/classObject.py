class Dobber:
    att1 = "Pappiii"

    def __init__(self, name):
        self.name = name


# diver code
# Object instantiation
Rodger = Dobber("Rodgerr")
Tommy = Dobber("Tommyyy")

# Accessing class attribute
print(f"{Dobber.att1}")
print(f"{Rodger.__class__.att1}")
print(f'{Tommy.__class__.att1}')

#  accessing instance attributes
print(f'My name is {Rodger.name}')
print(f'My name is {Tommy.name}')
