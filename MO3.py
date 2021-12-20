class Add:
     def result(self,a,b):
         print("Addition: " ,a+b)

class Multi(Add):
    def result(self, a, b):
        print("Multiplication: ", a * b)

m = Multi()
m.result(int(input("Enter first number: ")),int(input("Enter second number: ")))