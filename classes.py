class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printValues(self):
        print("The name of the person is " + self.name)
        print("The age of the person is " , self.age)
        print("The age of the person is " + str(self.age))

myPerson = Person("Maggie", 89)
print(myPerson.name)
print(myPerson.age)
myPerson.printValues()


