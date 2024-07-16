class Dogs:
    # class attribute
    att1 = "nanda"

    #     Instance Attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'My Name is {self.name}')
        print(f"My Name is {Dogs.att1}")


# Object Instantiation
CallMyMethod = Dogs('Pappi')
CallMethod = Dogs("Tommy")

# accessing class method
CallMyMethod.speak()
CallMethod.speak()
