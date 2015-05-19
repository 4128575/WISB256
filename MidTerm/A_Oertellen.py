invoer=input()
if invoer[0]=='U':
    lijst=invoer.split()
    k=len(lijst)
    print(k)
else:
    getal='Ug'
    for i in range(1,int(invoer)):
        getal=getal+' ug'
    getal=getal+'!'
    print(getal)