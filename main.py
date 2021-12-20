class Parent:
    def anything(self):
        print("Function defined in parent class")

class Child(Parent):
    pass

obj = Child()
obj.anything()
