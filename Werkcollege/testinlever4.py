import bisection
import math

root = bisection.findRoot(lambda x:math.cos(x),0,2,0.001)
print(root)
root2 = bisection.findAllRoots(lambda x:math.cos(x),0,2,0.001)
print(root2)
root3 = bisection.findAllRoots(lambda x:x**2-2,-2,2,0.001)
print(root3)
root4 = bisection.findAllRoots(lambda x:math.sin(x),0,9,0.001)
print(root4)