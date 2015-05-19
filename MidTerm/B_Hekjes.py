N=int(input())
hekjes=0
for i in range(1,N+1):
    invoer=input()
    for k in range(0,len(invoer)):
        if invoer[k]=='#':
            hekjes+=1
print('Om de hekjes in dit weiland te verven heb je',hekjes*5,'liter verf nodig')