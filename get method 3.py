class Employee:
    def __init__(self, postname, idnumber, salary):
        self.postname = postname
        self.idnumber = idnumber
        self.salary = salary

    def get_data(self):
        print("Post Name: ",self,postname)
        print("Post Id Number: ",self,self,idnumber)
        print("Post Salary: ",self,slary)

e = Employee(input("Enter Post Name: "),input("Enter Id Number: "),int(input("Enter Salary: ")))
e.get_data()