class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = "Provide at least two number"
obj = Myclass()
print(obj.sum(int(input("Enter A First Number: ")),int(input("Enter A Second Number: ")),int(input("Enter A Third Number: "))))