class Dog:
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner

class Person:
    def __init__(self,name):
        self.name=name

person = Person("Mike Pompe")
dog = Dog("Stanley", "Bulldog", person)
print(dog.owner.name)