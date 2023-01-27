from graphics import *
import random


def allowed(p1, p2):
    if p1 in range(0, 5) and p2 in range(0, 5):
        return False
    if p1 in range(4, 9) and p2 in range(4, 9):
        return False
    if p1 in range(8, 13) and p2 in range(8, 13):
        return False
    if p1 in range(12, 16) and p2 in range(12, 16):
        return False
    if p1 == 0 and p2 in range(12, 16):
        return False
    if p1 in range(12, 16) and p2 == 0:
        return False
    return True

win = GraphWin("RandomSquare", 1000, 1000)

Points = [
    [Point(0, 0), 0],
    [Point(10, 0), 1],
    [Point(20, 0), 2],
    [Point(30, 0), 3],
    [Point(40, 0), 4],

    [Point(40, 10), 5],
    [Point(40, 20), 6],
    [Point(40, 30), 7],

    [Point(33, 40), 8],
    [Point(26, 40), 9],
    [Point(20, 40), 10],
    [Point(13, 40), 11],
    [Point(6, 40), 12],

    [Point(0, 30), 13],
    [Point(0, 20), 14],
    [Point(0, 10), 15]
]

p1 = random.choice(Points)
p2 = random.choice(Points)
print(p1 + p2)

while not allowed(p1[1], p2[1]):
    print("Recalculating " + str(p1) + str(p2))
    p2 = random.choice(Points)

Rectangle(Point(0, 0), Point(40, 40)).draw(win)
Line(p1[0], p2[0]).draw(win)

input()