import math

#A-Lorre
#n = int(input())
#for i in range(1,n+1):
#    invoer=input()
#    lijst=invoer.split()
#    if len(lijst)>4:
#        print('Crackers!')
#    else:
#        print(invoer+' krAh!')

#B-RPN
#rpn = input()
#lijst = rpn.split()
#if lijst[2]=='+':
#    a=int(lijst[0])+int(lijst[1])
#    a ="{0:.3f}".format(a)
#    print(a)
#elif lijst[2]=='-':
#    b=int(lijst[0])-int(lijst[1])
#    b ="{0:.3f}".format(b)
#    print(b)
#elif lijst[2]=='*':
#    c=int(lijst[0])*int(lijst[1])
#    c ="{0:.3f}".format(c)
#    print(c)
#elif lijst[2]=='/':
#    d = int(lijst[0])/int(lijst[1])
#    d ="{0:.3f}".format(d)
#    print(d)

#C-Nerfgun
#vuurkracht = int(input())
#zwaartekracht = int(input())
#afstand = int(input())
#waarde=(afstand*zwaartekracht)/(vuurkracht*vuurkracht)
#hoek = (1/2)*math.asin(waarde)
#hoek ="{0:.2f}".format(hoek)
#print(hoek)

#D-Vigenerecijfer
code=input()
sleutel=input()
bericht=''
for i in range(0,len(code)):
    a=ord(code[i])-97
    b=ord(sleutel[i%len(sleutel)])-97
    c=(a+b)%26
    letter=chr(c+97)