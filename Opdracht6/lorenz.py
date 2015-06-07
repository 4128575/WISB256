import numpy as np
from scipy.integrate import odeint
from scipy import linalg
import math

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
    
    def df(self,u):
        x=np.matrix([[-self.sigma,self.sigma,0],[self.rho-u[2],-1,-u[0]],[u[1],u[0],-self.beta]])
        return x
    
    def isStable(self,u):
        jac=self.df(u)
        eigen=linalg.eig(jac)[0]
        self.eigen=eigen
        if eigen[2]<0 and eigen[1]<0 and eigen[2]<0:
            return True
        else:
            return False