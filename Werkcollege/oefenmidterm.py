n = int(input())
for i in range(1,n+1):
    invoer=input()
    lijst=invoer.split()
    if len(lijst)>4:
        print('Crackers!')
    else:
        print(invoer+' krAh!')
    