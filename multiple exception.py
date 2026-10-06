
#1
# try:
#     import math
#     n1=int(input('Entre the number'))
#     print(math.factorial(n1))
# except ValueError:
#     print('ValueError')
# else:
#     print('There is no Exception')
#
# finally:
#     print('Finished')

#2
# try:
#     n1=input('Enter the number')
#     n2=input('Enter the number')
#     operator=input('Enter the operator')
#
#     if operator=="+":
#         print(n1+n2)
#     elif operator=="-":
#         print(n1-n2)
#     elif operator=="*":
#         print(n1*n2)
#     elif operator=="/":
#         print(n1/n2)
#     else:
#         print('Invalid operator')
#
# except ValueError:
#     print('input error')
# except ZeroDivisionError:
#     print('Zero divison error')
#
# finally:
#     print('Finished')

#3.
# try:
#     file_name=input('Enter the filename')
#     f=open('file_name','r')
#     f.read()


#
try:
    import math
    n1=int(input('Entre the number'))
    print(math.factorial(n1))
except Exception as x:
    print(x)
else:
    print('There is no Exception')

finally:
    print('Finished')