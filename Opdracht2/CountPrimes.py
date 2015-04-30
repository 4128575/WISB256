import sys
import math

file = open(str(sys.argv[1]), 'r')

lijstpi = []

for item in file:
    lijstpi.append(int(item))

lijstpi.sort()
piN = len(lijstpi)
lijst2pi = []

for k in range(1,piN):
    if lijstpi[k]-lijstpi[k-1]==2:
        lijst2pi.append(lijstpi[k-1])

pi2N = len(lijst2pi)
y = 10
n = lijstpi[piN-1]
getal = n/math.log(n)
cons2 = 0.6601618
getal2 = (2*cons2*n)/(math.log(n)**2)

print('Largest Prime = ', n)
print('-------------------------------------')
print('pi(N)         = ', piN)
print('N/log(N)      = ', getal)
print('ratio         = ', piN/getal)
print('-------------------------------------')
print('pi_2(N)       = ', pi2N)
print('2CN/log(N)^2  = ', getal2)
print('ratio         = ', pi2N/getal2)