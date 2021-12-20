# Get method
class Laptop:
    def __init__(self, name, model, ram, rom, price):
        self.name = name
        self.model = model
        self.ram = ram
        self.rom = rom
        self.price = price

    def get_details(self):
        print("Laptop Name: ",self.name)
        print("Laptop Model: ",self.model)
        print("Laptop Ram: ",self.ram)
        print("Laptop Rom: ",self.rom)
        print("Laptop Pricee: ",self.price)

l = Laptop(input("Enter Laptop Name: "),input("Enter Laptop Model: "),input("Enter Laptop Ram: "),input("Enter Laptop Rom: "),int(input("Enter Laptop Price: ")))
l.get_details()