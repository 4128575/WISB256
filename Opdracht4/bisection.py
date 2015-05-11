import math

def findRoot(f,a,b,epsilon):
    m=(a+b)/2
    if f(a)==0:
        return a
    elif f(b)==0:
        return b
    elif abs(b-a) < epsilon:
        return m
    elif f(m) == 0:
        return m
    elif f(a)*f(m) < 0:
        return findRoot(f,a,m,epsilon)
    else :
        return findRoot(f,m,b,epsilon)

def findAllRoots(f,a,b,epsilon):
    rootlist=[]
    p=1000
    q=abs(b-a)/p
    for k in range(0,p):
        if f(a+k*q)*f(a+(k+1)*q)<0:
            rootlist.append(findRoot(f,a+k*q,a+(k+1)*q,epsilon))
        if f(a+k*q)==0:
            rootlist.append(a+k*q)
    return rootlist