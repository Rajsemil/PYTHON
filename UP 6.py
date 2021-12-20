import pickle
class Student:
    def __init__(self,name,roll):
        self.name = name
        self.rol = roll

    def disp(self):
        print(self.name,self.roll)
with open('student.dat',mode+'rb') as f:
    stu1 = Student("Amit",100)
    stu2 = Student("Zack",101)
    pickle.dump(stu1.f)
    pickle.dump(stu2.f)
with open('student.dat', mode='rb') as f:
    obj1 = pickle.load(f)
    obj2 = pickle.load(f)
print("Unpickling success")