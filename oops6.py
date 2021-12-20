class Animal:
    def speak(self):
        print("Animall Speaking")

class Dog(Animal):
    def bark(self):
        print("Dog Barking")

class Dogchild(Dog):
    def eat(self):
        print("Eating bread....")

x = Dogchild()
x.bark()
x.speak()
x.eat()