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

    def __str__(self):
        return repr(self.n)

u=Vector(3,1)
print(u)