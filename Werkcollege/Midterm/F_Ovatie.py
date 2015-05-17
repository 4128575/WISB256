import math

smax=input()
lijst=input()

publiek=0
for i in range(0,len(lijst)):
    publiek+=int(lijst[i])

def staanden(a):
    staan=int(lijst[0])+a
    for i in range(1,len(lijst)):
        if staan>=i:
            staan+=int(lijst[i])
    return staan

def check():
    for k in range(0,9):
        if staanden(k)==publiek+k:
            return k
print(check())