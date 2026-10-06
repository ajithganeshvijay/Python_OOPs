#define a class named student with the following details:
#data members:
#sname,rollno,class,mark1,mark2,mark3.
#Member methods:
#calculate(),Calculate the total and average
#showdetails()_display the details of student with average mark
#create one object for the class and call the above member methods

class Student:
    def __init__(self):
        self.sname=input('Enter your name')
        self.rollno=int(input('Enter your roll number'))
        self.Class=int(input('Enter your class'))
        self.mark1=int(input('enter your mark'))
        self.mark2 = int(input('enter your mark'))
        self.mark3 = int(input('enter your mark'))
    def calculate(self):
            self.total=self.mark1+self.mark2+self.mark3
            self.average=self.total/3

    def showdetails(self):
            print('Students name:',self.sname)
            print('Class:',self.Class)
            print('roll no:',self.rollno)
            print('Average mark:',self.average)
s=Student()
s.calculate()
s.showdetails()