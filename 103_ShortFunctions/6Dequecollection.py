from collections import deque

d = deque()
d.append(1)
print(d)
d.appendleft(2)
print(d)
d.clear()
d.extend('1')
d.extendleft('234')
print(d)
d.count('1')
d.pop()
d.popleft()
d.extend('7896')
d.reverse()
d.rotate(3)
print(d)
