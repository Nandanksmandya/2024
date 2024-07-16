# Parent class
class Person(object):

    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum

    def display(self):
        print(self.name)
        print(self.idnum)

    def details(self):
        print(f"My Name is {self.name}")
        print(f"My Name is {self.idnum}")


class Employee(Person):
    def __init__(self, name, idnum, sal, post):
        self.sal = sal
        self.post = post
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnum)

    def details(self):
        print(f'My name is {self.name}')
        print(f'ID number is {self.idnum}')
        print(f'Post : {self.post}')

# Creating Parent class object in child class
a = Person('Arun', '008')
a.display()
#  Creating Child class object in the same class
e = Employee('Nandan', '007', '400000', 'Associate')
e.details()
e.display()




