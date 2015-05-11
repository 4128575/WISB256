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