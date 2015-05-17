import math

rpn = input()
lijst = rpn.split()
if lijst[2]=='+':
    a=int(lijst[0])+int(lijst[1])
    a ="{0:.3f}".format(a)
    print(a)
elif lijst[2]=='-':
    b=int(lijst[0])-int(lijst[1])
    b ="{0:.3f}".format(b)
    print(b)
elif lijst[2]=='*':
    c=int(lijst[0])*int(lijst[1])
    c ="{0:.3f}".format(c)
    print(c)
elif lijst[2]=='/':
    d = int(lijst[0])/int(lijst[1])
    d ="{0:.3f}".format(d)
    print(d)