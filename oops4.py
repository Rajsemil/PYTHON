class Person:
  def __init__(self, fname, lname, mobile ):
    self.fname = fname
    self.lname = lname
    self.mobile = mobile

  def printdata(self):
    print("First Name:",self.fname,"\n Last Name;",self.lname,"\n Mobile Number;",self.mobile)

x = Person(input("Enter Your First Name: ") , input("Enter Your Last Name: ") , int(input("Enter Your Mobile Number: ")))
x.printdata()

