# 1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# class Circle:
#     def __init__(self):
#         self.r=int(input('Enter the radius'))
#     def getarea(self):
#         self.area=3.14*self.r**2
#         print('Area of the circle=',self.area)
#     def getperimeter(self):
#         self.perimeter=2*3.14*self.r
#         print('Perimeter of the circle=',self.perimeter)

c=Circle()
c.getarea()
c.getperimeter()
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.
#
# 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:

# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.
#
# class Account:
#     def __init__(self):
#         self.accntnumber=int(input('Enter the account number'))
#         self.accntname=input('Enter the account name')
#         self.balance=int(input('Enter the balance amount'))
#
#     def withdraw(self):
#         self.amount=int(input('Enter the amount to be withdraw'))
#         self.balance-= self.amount

#     def deposit(self):
#         self.amount = int(input('Enter the amount to be deposit'))
#         self.balance += self.amount
#     def showbalance(self):
#         print('balance=',self.balance)
# a=Account()
# # a.withdraw()
# # a.deposit()
# # a.showbalance()
# b=Account()
# # b.withdraw()
# # b.deposit()
# # b.showbalance()

# l=[a,b]
# number=input('Enter the account number')
# for i in l:
#     if i.accntname==number:
#         print('balance amount=',i.balance)
#         print(f"Account number:{i.accntnumber} Account name:{i.accntname} Balance:{i.balance}")




