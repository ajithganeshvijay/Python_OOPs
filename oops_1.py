# #syntax for class
# #class classname:
#....................static..................
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print('name is:',self.name,' age is:',self.age)
# #object creation
# #objectname+Classname(arguments)
# p=Person('Athulya',23)
# p.display()

#...................dynamic..............
# #define a class name person name and age from the user
#display the details by using show() method.
#create an object and call the method

class Person:
    def __init__(self):
        self.name=input('Enter your name')
        self.age=int(input('Enter your age'))
    def show(self):
        print(self.name,self.age)
p=Person()
p.show()
p1=Person()
p1.show()
