class Person:
  def __init__(self, fname, lname, mobile, email):
    self.fname = fname
    self.lname = lname
    self.mobile = mobile
    self.email = email

  def printdata(self):
    print("First Name:",self.fname,"\n Last Name;",self.lname,"\n Mobile Number:",self.mobile, "\nYour Email:",self.email)
class Student(Person):
  def __init__(self, fname, lname, mobile, email):
    super().__init__(fname, lname, mobile, email)
x = Person(input("Enter Your First Name: ") , input("Enter Your Last Name: ") , int(input("Enter Your Mobile Number: ")), input("Enter Your Email: "))
x.printdata()