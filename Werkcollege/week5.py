import copy
import math
import datetime

class Point(object):
    """Represents a point in 2-D space."""
testp1=Point()
testp2=Point()
testp1.x=1.0
testp1.y=1.0
testp2.x=0.0
testp2.y=4.0

def distance_between_points(p,q):
    distance = math.sqrt((p.x-q.x)**2+(p.y-q.y)**2)
    return distance

#print(distance_between_points(testp1,testp2))

class Rectangle(object):
    """Represents a rectangle.
    
    attributes: width, height, corner.
    """
box=Rectangle()
box.width=100.0
box.height=200.0
box.corner=Point()
box.corner.x=0.0
box.corner.y=0.0

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

#move_rectangle(box, 1.0, 2.0)
#print(box.corner.x)
#print(box.corner.y)

def move_rectangle2(rect, dx, dy):
    newrect=Rectangle()
    newrect.width=rect.width
    newrect.height=rect.height
    newrect.corner=Point()
    newrect.corner.x=rect.corner.x+dx
    newrect.corner.y=rect.corner.y+dy
    return newrect

#print(move_rectangle2(box, 1.0, 2.0).width, move_rectangle2(box, 1.0, 2.0).height, move_rectangle2(box, 1.0, 2.0).corner.x, move_rectangle2(box, 1.0, 2.0).corner.y)

def move_rectangle3(rect, dx, dy):
    newrect=copy.deepcopy(rect)
    newrect.corner.x += dx
    newrect.corner.y += dy
    return newrect

#print(move_rectangle3(box, 1.0, 2.0).width, move_rectangle3(box, 1.0, 2.0).height, move_rectangle3(box, 1.0, 2.0).corner.x, move_rectangle3(box, 1.0, 2.0).corner.y)

def dayofweek():
    today=datetime.date.today()
    n = today.weekday()
    week =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    print(week[n])

#dayofweek()

testbir=datetime.date(1995,7,23)

def birthday(dag):
    today=datetime.date.today()
    todaytoor=datetime.date(today.year,7,23)
    age=today.year-dag.year
    if today.month<=dag.month:
        if today.day<dag.day:
            age=age-1
    print(age,abs(today.toordinal()-todaytoor.toordinal()))

#birthday(testbir)