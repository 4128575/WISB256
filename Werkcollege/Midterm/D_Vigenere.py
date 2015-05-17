import math

code=input()
sleutel=input()
bericht=''
for i in range(0,len(code)):
    a=ord(code[i])-97
    b=ord(sleutel[i%len(sleutel)])-97
    if a<b:
        c=a-b+26
        letter=chr(c+97)
        bericht = bericht+letter
    else:
        c=a-b
        letter=chr(c+97)
        bericht = bericht+letter
print(bericht)