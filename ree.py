import random
n1= int(input('pick a number:'))

n2 = random.randint(1, 100)

if n1 > n2 :
    print('you win'  )
elif n1 < n2 :
    print ('u lose' )
else :
    print('keep trying')
