from Vector import Vector

u=Vector(3,[1,2,3])
v=Vector(3,3.5)
w=u.lincomb(v,10,1)
print(w)
w=w.scalar(2)
print(w)
print(w.norm())
print(w.inner(u))