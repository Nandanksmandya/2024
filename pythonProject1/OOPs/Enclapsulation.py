class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_sal(self):
        return self.__salary

    def set_sal(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")


# Example usage
employee = Employee('Jone', 50000)

print(employee.get_name())
print(employee.get_sal())
print(employee.set_name("arun"))
print(employee.get_name())
