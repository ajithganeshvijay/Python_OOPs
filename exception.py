#try except block
try:
    n1=int(input('Enter a number'))
    n2=int(input('Enter a number'))
    r=n1/n2
    print(r)

except:
    print('Zero division error')

else:
    print('No exception ocuured')

finally:
    print('finished')