# Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.
class Student:
    def __init__(self):
        self.name=input('Enter the name')
        self.rollno = int(input('Enter the roll number'))
        self.mark=int(input('Enter the mark'))
    def updatemarks(self):
        self.mark = int(input('Enter the updated marks'))
    def studentsdetails(self):
        print('Students name:',self.name)
        print('Roll No:', self.rollno)
        print('Marks',self.mark)
l=[]
while(1):
    print('Menu Drvien program')
    print('1.Add Student')
    print('2.update marks')
    print('3.Display ALl students details')
    print('4.Search student by roll number')
    print('5.delete student')
    print('6.Exit')

    ch=input('Enter your choice')
    if ch==1:
        s=Student()
        l.append(s)
    elif ch==2:
        new=int(input('enter the roll number'))
        for i in l:
            if i.rollno==new:
                i.update()
        else:
            print('student noy found')
    elif ch==3:
        for i in l:
            i.studentsdetails()
    elif ch==4:
        num=int(input('enter the roll number'))
        for i in l:
            if i.rollno==num:
                i.studentsdetails()
        else:
            print('student not found')

    elif ch==5:
        num = int(input('enter the roll number'))
        for i in l:
            if i.rollno == num:
                l.remove(i)
    else:
        exit()

