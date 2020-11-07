import random

name = input("Hello there!, please enter your name.: ")
print(f'Hello, {name}! ')
while True: #continue forever
    n1 = int(input('Enter a number..: '))
    r = random.randint(1, 3)

    if n1 > r :
        print('The number is too high')
        print(f"The number was: {r}.")
    elif n1 < r :
        print('The number is too low')
        print(f"The number was: {r}.")
    elif n1 == r:
        print('You guessed the number!')
        break
    
    
