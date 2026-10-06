class Company:
    def __init__(self):
        self.name=input('Enter the company')
    def showdetails(self):
        print('Company Name:',self.name)
class Employee(Company):
    def __init__(self):
        super().__init__()
        self.ename=input('Enter the employee name')
        self.empid=int(input('Enter your EMPID:'))
        self.designation=input('Enter your designation:')
        self.salary=int(input('Enter your salary:'))
    def getsalary(self):
        print('Salary:',self.salary)
    def showemployeedetails(self):
        super().showdetails()
        print('Employee Name:',self.ename)
        self.getsalary()
        print('Designation:',self.designation)
e=Employee()
e.showemployeedetails()

