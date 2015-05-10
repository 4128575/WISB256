import math
def square_root(a):
    x=a+0.01
    while True:
        epsilon=0.000000000001
        y=(x+a/x)/2
        if abs(y-x)<epsilon:
            return y
            break
        x=y

def test_square_root(n):
    for k in range(1,n+1):
        x=square_root(k)
        y=math.sqrt(k)
        z=abs(x-y)
        print(k,x,y,z)

def estimate_pi():
    k=0
    s=0
    a=2*math.sqrt(2)*1103/9801
    while a>1e-15:
        s+=a
        k+=1
        a=(2*math.sqrt(2)*math.factorial(4*k)*(1103+26390*k))/(9801*(math.factorial(k)**4)*(396**(4*k)))
    return 1/s

def bisection(l,a):
    k=0
    if l[math.floor(len(l)/2):][0]<a:
        print(math.floor(len(l)/2))
        k=k+math.floor(len(l)/2)
        print(k)
        print(l[math.floor(len(l)/2):])
        bisection(l[math.floor(len(l)/2):],a)
    elif l[math.floor(len(l)/2):][0]==a:
        print(k)
    else:
        bisection(l[:math.ceil(len(l)/2)],a)

testlijst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#bisection(testlijst,10)
#bisection(testlijst[:math.ceil(len(testlijst)/2)],10)
print(testlijst[math.floor(len(testlijst)/2):])
