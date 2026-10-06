#write a menu_driven python program for banking sustem using a class
#Account to perform the following operations:


#1.create an account
#2.Withdrawn money
#3.Deposit money
#4.Display balance
#5.Exit

#store account details in a list and search accounts using the account number
#Display "Account Not Found" if the account does not exist.
class Account:
    def __init__(self):
        self.accntnumber=int(input('Enter the account number'))
        self.accntname=input('Enter the account name')
        self.balance=int(input('Enter the balance amount'))

    def withdraw(self):
        self.amount=int(input('Enter the amount to be withdraw'))
        self.balance-= self.amount
        print('balance=', self.balance)
    def deposit(self):
        self.amount = int(input('Enter the amount to be deposit'))
        self.balance += self.amount
        print('balance=', self.balance)
    def showbalance(self):
        print('balance=',self.balance)
l=[]
while(1):
    print('Menu Driven Program')
    print('1.Create an account')
    print('2.Withdraw money')
    print('3.Deposit money')
    print('4.Display balance')
    print('5.Exit')

    ch=int(input('Enter your choice'))
    if ch==1:
        a=Account()
        l.append(a)
        # print(l)
    elif ch==2:
        num=int(input('Enter your account number'))
        for i  in l:
            if i.accntnumber==num:
                i.withdraw()
                break
        else:
            print('account not found')
    elif ch==3:
        num=int(input('Enter your account number'))
        for i  in l:
            if i.accntnumber==num:
                i.deposit()
                break
        else:
            print('account not found')
    elif ch==4:
        num = int(input('Enter your account number'))
        for i in l:
            if i.accntnumber == num:
                i.showbalance()
                break
        else:
            print('account not found')
    else:
        exit()