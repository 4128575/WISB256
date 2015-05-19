import math

rpn = input()
lijst = rpn.split()
def repn(lijst):
    operand=0
    for k in range(0,len(lijst)):
        if lijst[k]=='+':
            operand=float(lijst[k-2])+float(lijst[k-1])
            lijst[k]=operand
            lijst.pop(k-1)
            lijst.pop(k-2)
            break
        elif lijst[k]=='-':
            operand=float(lijst[k-2])-float(lijst[k-1])
            lijst[k]=operand
            lijst.pop(k-1)
            lijst.pop(k-2)
            break
        elif lijst[k]=='*':
            operand=float(lijst[k-2])*float(lijst[k-1])
            lijst[k]=operand
            lijst.pop(k-1)
            lijst.pop(k-2)
            break
        elif lijst[k]=='/':
            operand=float(lijst[k-2])/float(lijst[k-1])
            lijst[k]=operand
            lijst.pop(k-1)
            lijst.pop(k-2)
            break
    return lijst

while len(lijst)!=1:
    lijst=repn(lijst)
getal=lijst[0]
getal ="{0:.3f}".format(getal)
print(getal)