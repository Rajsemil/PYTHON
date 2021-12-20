class Car:
    def __init__(self, carname):
        self.__make = carname
    def set_make(self, carname):
        self.__make = carname
    def get_make(self):
        return self.__make
myCar = Car(input("Enter A Car Name: "));
print(myCar.get_make())
myCar.set_make('Porche')
print(myCar.get_make())