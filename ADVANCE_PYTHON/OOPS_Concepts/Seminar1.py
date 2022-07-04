

#person [private]

#employee [person]

class Person:
    def __init__(self):
        self.name="vishnu"
        self.age=24
        self.__accesscode="abc123"
class Employee(Person):
    def __init__(self):
        self.occupation="pilot"
        self.id=123

ob=Employee()
