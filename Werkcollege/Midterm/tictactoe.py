import math

a=input()
b=input()
c=input()
if a[0]==a[1]==a[2]:
    if a[0]!='0':
        print('Player',a[0],'wins')
    else:
        print('No winner')
elif b[0]==b[1]==b[2]:
    if b[0]!='0':
        print('Player',b[0],'wins')
    else:
        print('No winner')
elif c[0]==c[1]==c[2]:
    if c[0]!='0':
        print('Player',c[0],'wins')
    else:
        print('No winner')
elif a[0]==b[0]==c[0]:
    if a[0]!='0':
        print('Player',a[0],'wins')
    else:
        print('No winner')
elif a[1]==b[1]==c[1]:
    if a[1]!='0':
        print('Player',a[1],'wins')
    else:
        print('No winner')
elif a[2]==b[2]==c[2]:
    if a[2]!='0':
        print('Player',a[2],'wins')
    else:
        print('No winner')
elif a[0]==b[1]==c[2]:
    if a[0]!='0':
        print('Player',a[0],'wins')
    else:
        print('No winner')
elif a[2]==b[1]==c[0]:
    if a[2]!='0':
        print('Player',a[2],'wins')
    else:
        print('No winner')
else:
    print('No winner')