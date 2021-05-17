from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt1 = Point(1, 2)
pt2 = Point(3, 4)
dot = (pt1.x * pt2.x) + (pt1.y * pt2.y)
print(dot)

# This is very useful then normal tuple and dict as we can access from boht index and key.
Color = namedtuple('Color', 'red green blue ')
red = Color(red=255, green=0, blue=0)
print(red.red)
print(red[0])
print(red[1])
print(red[2])
