from graphics import *
import math
win = GraphWin("circle art", 600, 600, autoflush=False)

a = 2
b = 3
r = 3

stepSize = 0.23
positions = []

t = 0
while t < 2 * math.pi:
    positions.append((r * math.cos(t) + a, r * math.sin(t) + b))
    t += stepSize

print(positions)

for i in positions:
    for ii in positions:
        Line(Point(i[0] * 100 + 99, i[1] * 100), Point(ii[0] * 100 + 99, ii[1] * 100)).draw(win)
win.update()
input()