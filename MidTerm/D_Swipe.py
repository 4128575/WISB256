k=int(input())
woorden=[]

for i in range(1,k+1):
    invoer=input()
    woorden.append(invoer)

n=int(input())

swipe=[]
for j in range(1,n+1):
    swip=input()
    swipe.append(swip)

for l in range(0,n):
    getal=0
    for p in range(0,k):
        if swipe[l][0]==woorden[p][0]:
            if swipe[l][-1]==woorden[p][-1]:
                posities=[]
                h=0
                for d in range(0,len(woorden[p])):
                    for i in range(h,len(swipe[l])):
                        if woorden[p][d]==swipe[l][i]:
                            posities.append(i)
                            h=i
                            break
                posities3=[]
                for g in range(0,len(posities)):
                    if posities[g] in posities3:
                        break
                    else:
                        posities3.append(posities[g])
                posities2=posities3[:]
                posities2.sort()
                if posities3==posities2:
                    if len(posities3)==len(woorden[p]):
                        print(woorden[p])
                        getal=1
                        break
    if getal==0:
        print('?')