import math

class Vector:
    """Vector in R^n"""
    def __init__(self,n,m=None):
        if m is None:
            self.n=[0]*n
        elif type(m)==list:
            self.n=m
        elif type(m)==float:
            self.n=[m]*n
        elif type(m)==int:
            self.n=[m]*n
        for i in range(0,n):
            self.n[i]="%f"%self.n[i]


    def __str__(self):
        for k in range(0,len(self.n)):
            self.n[k]=str(self.n[k])
        return "\n".join(self.n)

    def lincomb(self,other,alpha,beta):
        lijst=[]
        for i in range(0,len(other.n)):
            getal= float(alpha)*float(self.n[i])+float(beta)*float(other.n[i])
            lijst.append(getal)
        return Vector(len(other.n),lijst)

    def scalar(self,alpha):
        lijst=[]
        for i in range(0,len(self.n)):
            getal= float(alpha)*float(self.n[i])
            lijst.append(getal)
        return Vector(len(self.n),lijst)

    def norm(self):
        kwad=0.0
        for i in range(0,len(self.n)):
            kwad+=float(self.n[i])**2
        norm=math.sqrt(kwad)
        return norm

    def inner(self,other):
        inner=0.0
        for i in range(0,len(self.n)):
            inner+=float(self.n[i])*float(other.n[i])
        return inner