class Person:
    age = int(input("Enter Number: "))
    if age>=25:
        pass
    else:
        print("Fase")
    def printAge(cls):
        print('The age is:', cls.age)
Person.printAge = classmethod(Person.printAge)
Person.printAge()