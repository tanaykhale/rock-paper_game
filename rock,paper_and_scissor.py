# Rock ,Paper and Scissor GAME

import random

def gameWin( Comp , you):
    if Comp == you:
        return "None"
    elif Comp == 'r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif Comp == 'p':
        if you=='s':
            return True
        elif you=='r':
            return False
    elif Comp == 's':
        if you=='p':
            return False
        elif you=='r':
            return True
    elif you!=s and you!=r and you!=p :
        return ('error')
  


print('Comp turn : rock(r) , paper(p) and scissors(s)')
you = input('Your turn : rock(r) , paper(p) and scissors(s) ')
randNo = random.randint(1,3)
if randNo ==1:
    Comp='r'
elif randNo==2:
    Comp='p'
elif randNo==3:
    Comp='s'

a = gameWin( Comp , you)

print(f'Computer choice {Comp}')
print(f'Your choice {you}')

if a == "None":
    print('Game tie')
elif a==True:
    print('YOU WIN')
elif a==False:
    print('you lose')
else  :
    print("Please enter only the given characters(p,r and s)")