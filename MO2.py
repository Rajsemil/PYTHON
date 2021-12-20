class Myclass:
    def sum(self, a, b, c):
        s = a+b+c
        return s

obj = Myclass()
print(obj.sum(int(input("Enter A First Number: ")),int(input("Enter A Second Number: ")),int(input("Enter A Third Number: "))))