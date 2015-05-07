import random
import math
import sys

if len(sys.argv)<=2 or len(sys.argv)>=5:
    print('Use: estimate_pi.py N L')
elif float(sys.argv[2])<=0:
    print('AssertionError: L should be greater than 0')
else:
    N=int(sys.argv[1])
    L=float(sys.argv[2])
    if len(sys.argv)==4:
        random.seed(sys.argv[3])
        
    def dropneedle(l):
        y0=random.random()
        theta=random.vonmisesvariate(0,0)
        y1=y0+math.sin(theta)*l
        if abs(math.ceil(y1)-math.ceil(y0))>0.01:
            return True
        else: 
            return False
    hits=0
    
    for k in range(N):
        if dropneedle(L)==True:
            hits+=1
    
    if float(sys.argv[2])<=1:
        pi=2*L*N/(hits)
    else:
        pi=2*(math.asin(1/L)+math.sqrt(L**2-1)-L)/(1-hits/N)
    
    print(hits , 'hits in', N , 'tries')
    print('Pi =', pi)