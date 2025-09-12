import random
import time
print('welcome user to the fun game : save your mom ')
print('here your play against a very high-end cpu to save your ugly mom ')
print('rules are simple choose rock paper scissors and how get\'s 3 points saves his ugly mom ')
print('1: rock , 2: paper ,3: scissors')
xxpc = 0
xxusr = 0
usrx = None
while xxpc < 3 and xxusr < 3:
    x = int(input('so 1/2/3 ? : '))
    if x == 1:
        usrx = 'rock'
    elif x == 2:
        usrx = 'paper'
    elif x == 3:
        usrx = 'scissors'
    else:
        exit()
    cho = ['rock', 'paper', 'scissors']
    xy = random.choice(cho)
    time.sleep(1)
    print('pc choose :'+xy)
    if xy == usrx:
        print('DRAW')
    elif xy == 'rock' and usrx == 'paper':
        xxusr += 1
        print('+1 pointe you win this round')
    elif xy == 'rock' and usrx == 'scissors':
        xxpc += 1
        print('+1 to cpu you lose this round')
    elif xy == 'paper' and usrx == 'rock':
        xxpc += 1
        print('+1 to cpu you lose this round')
    elif xy == 'paper' and usrx == 'scissors':
        xxusr += 1
        print('+1 pointe you win this round')
    elif xy == 'scissors' and usrx == 'rock':
        xxusr += 1
        print('+1 pointe you win this round')
    elif xy == 'scissors' and usrx == 'paper':
        xxpc += 1
        print('+1 to cpu you lose this round')
if xxpc == 3:
    print('cpu win your mom cooked')
elif xxusr == 3:
    print('you win cpu\'s mom cooked\n')
