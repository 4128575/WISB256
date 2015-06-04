import math

class Vector:
    """Vector in R^n"""
    def __init__(self,n,m=None):
        if m is None:
            self.n=[float(0)]*n
        elif type(m)==list:
            self.n=list(m)
        elif type(m)==float:
            self.n=[m]*n
        elif type(m)==int:
            self.n=[m]*n

    def __str__(self):
        lijstje=[]
        for i in range(len(self.n)):
            lijstje.append(str(self.n[i]))
        return "\n".join(lijstje)

    def lincomb(self, other,alpha,beta):
        lcom=[]
        for i in range(len(self.n)):
            lcom.append(float(alpha)*float(self.n[i])+float(beta)*float(other.n[i]))
        return Vector(len(other.n),lcom)

    def scalar(self,alpha):
        scal=[]
        for i in range(len(self.n)):
            scal.append(float(alpha)*float(self.n[i]))
        return Vector(len(self.n),scal)

    def norm(self):
        nor=0
        for i in range(len(self.n)):
            nor=nor+float(self.n[i])**2
        return float(math.sqrt(nor))

    def inner(self,other):
        inne=0
        for i in range(len(self.n)):
            inne=inne+float(self.n[i])*float(other.n[i])
        return float(inne)

def GrammSchmidt(V):
    k=len(V)
    for i in range(k):
        V[i]=V[i].scalar(1/(V[i].norm()))
        for j in range(i+1,k):
            V[j]=V[j].lincomb(V[i].scalar(V[j].inner(V[i])/V[i].inner(V[i])),1,-1)
    return V