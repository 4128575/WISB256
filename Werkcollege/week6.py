class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self,x=None,y=None):
        if x is None:
            self.x=0.0
            self.y=0.0
        else:
            self.x=x
            self.y=y
    
    def __str__(self):
        return '(%s,%s)' % (self.x,self.y)
    
    def __add__(self,other):
        if isinstance(other, Point):
            return self.add_points(other)
        else:
            return self.add_tuple(other)
    
    def add_points(self,other):
        newpointx=self.x+other.x
        newpointy=self.y+other.y
        return Point(newpointx,newpointy)
    
    def add_tuple(self,other):
        tupx=self.x+other[0]
        tupy=self.y+other[1]
        return Point(tupx,tupy)

class Kangaroo(object):
    def __init__(self):
        self.pouch_contents=[]
    
    def __str__(self):
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

testp1=Point(1,1)
testp2=Point(0,4)
testtuple=(3,3)
#print(testp1+testtuple)
#print(testp1+testp2)