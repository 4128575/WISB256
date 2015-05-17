import math

N=int(input())
commandos=[]
positie=[6,5,1,2,3,4]

for i in range(1,N+1):
    a=input()
    commandos.append(a)

for k in range(0,N):
    if commandos[k]=='rechts':
        positie=[positie[3],positie[0],positie[1],positie[2],positie[4],positie[5]]
    elif commandos[k]=='links':
        positie=[positie[1],positie[2],positie[3],positie[0],positie[4],positie[5]]
    elif commandos[k]=='omhoog':
        positie=[positie[5],positie[1],positie[4],positie[3],positie[0],positie[2]]
    elif commandos[k]=='omlaag':
        positie=[positie[4],positie[1],positie[5],positie[3],positie[2],positie[0]]
print(positie[0])