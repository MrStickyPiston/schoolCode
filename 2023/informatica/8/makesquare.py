from graphics import *
import random
import time

win = GraphWin("RandomSquare", 400, 400)
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

corners = [
    [Point(0, 0), 0],
    [Point(40, 0), 4],
    [Point(40, 40), 8],
    [Point(0, 40), 12],
    [Point(0, 0), 16]
]


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


def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i][1] - K))]


def get_corner(p):
    return closest(corners, p[1])

def square(x, y):
    p1 = random.choice(Points)
    p2 = random.choice(Points)
    print(p1 + p2)

    while not allowed(p1[1], p2[1]):
        print("Recalculating " + str(p1) + str(p2))
        p2 = random.choice(Points)

    p1 = [Point(p1[0].getX() + x, p1[0].getY() + y), p1[1]]
    p2 = [Point(p2[0].getX() + x, p2[0].getY() + y), p2[1]]

    Rectangle(Point(0 + x, 0 + y), Point(40 + x, 40 + y))#.draw(win)
    Line(p1[0], p2[0])#.draw(win)

    print(p1[0])
    corner = get_corner(p1)
    p = []

    for i in corners:
        if i[1] == corner[1]:
            pass
        elif i[1] == 16:
            pass
        else:
            print(i + corner)
            p.append(i)

    print(p)

    polygon = Polygon(p1[0], Point(p[0][0].getX() + x, p[0][0].getY() + y), Point(p[1][0].getX() + x, p[1][0].getY() + y), Point(p[2][0].getX() + x, p[2][0].getY() + y), p2[0])
    polygon.setFill("black")
    polygon.draw(win)

x = 0
y = 0
for i in range(11):
    for i2 in range(10):
        time.sleep(0.1)
        square(x, y)
        x += 40
    y += 40
    x = 0

input()
