#define a class name employee with the following details.
#data members:
#Empid,name,slary,designation,place
#member methods
#getsalary(),showpersonaldetails()
#create two objects for the employee class and call the above member methods.

class Employee:
    def __init__(self):
        self.Empid=int(input('Enter your Empid'))
        self.name=input('Enter your name')
        self.salary=int(input('Enter your salary'))
        self.designation=input('Enter your designation')
        self.place=input('Enter your place')
    def getsalary(self):
        print(self.Empid,self.salary,)
    def showpersondetails(self):
        print(self.name,self.designation,self.place)
e=Employee()
e.getsalary()
e.showpersondetails()
e1=Employee()
e1.getsalary()
e1.showpersondetails()
