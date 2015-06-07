import numpy as np
from scipy.integrate import odeint

class Lorenz(object):
    def __init__(self,startstate,sigma=10,rho=28,beta=8/3):
        self.sigma=sigma
        self.rho=rho
        self.beta=beta
        self.a0=startstate
        
    def solve(self,T,dt):
        def func(f,t):
            return [self.sigma*(f[1]-f[0]),f[0]*(self.rho-f[2])-f[1],f[0]*f[1]-self.beta*f[2]]
        tlijst=np.arange(0,T,dt)
        opl=odeint(func,self.a0,tlijst)
        return opl

L1=Lorenz([-1,1,0])
L2=Lorenz([-1.001,1.001,0.001])
u1=L1.solve(50,0.01)
u2=L2.solve(50,0.01)
print(u1[0,0],u2[0,0])
print(u1[-1,0],u2[-1,0])