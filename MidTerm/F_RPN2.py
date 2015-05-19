rpn = input()
lijst = rpn.split()
def repn(lijst):
    for k in range(0,len(lijst)):
        if lijst[k]=='+':
            lijst[k]='('+lijst[k-2]+' + '+lijst[k-1]+')'
            lijst.pop(k-1)
            lijst.pop(k-2)
            break
        elif lijst[k]=='-':
            lijst[k]='('+lijst[k-2]+' - '+lijst[k-1]+')'
            lijst.pop(k-1)
            lijst.pop(k-2)
            break
        elif lijst[k]=='*':
            lijst[k]='('+lijst[k-2]+' * '+lijst[k-1]+')'
            lijst.pop(k-1)
            lijst.pop(k-2)
            break
        elif lijst[k]=='/':
            lijst[k]='('+lijst[k-2]+' / '+lijst[k-1]+')'
            lijst.pop(k-1)
            lijst.pop(k-2)
            break
    return lijst

while len(lijst)!=1:
    lijst=repn(lijst)
print(lijst[0])