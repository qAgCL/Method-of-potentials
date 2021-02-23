import numpy as np
import matplotlib.pyplot as plt
import random


class Point:
    def __init__(self, x,y, cl):
        self.x1 = x
        self.x2 = y
        self.cl = cl

class Func:
    c = 1
    x1 = 4
    x2 = 4
    x1x2 = 16


    def __add__(self, other):
        self.c = self.c + other.c
        self.x1 = self.x1 + other.x1
        self.x2 = self.x2 + other.x2
        self.x1x2 = self.x1x2 + other.x1x2
        return self
    def __sub__(self, other):
        self.c = self.c - other.c
        self.x1 = self.x1 - other.x1
        self.x2 = self.x2 - other.x2
        self.x1x2 = self.x1x2 - other.x1x2
        return self
    def NewFactor(self, point):
        self.x1 *= point.x1
        self.x2 *= point.x2
        self.x1x2 *= point.x1*point.x2
        return self
    def SetZero(self):
        self.c = 0
        self.x1 = 0
        self.x2 = 0
        self.x1x2 = 0
    def GetValue(self, point):
        return self.c + point.x1*self.x1 + point.x2*self.x2 + point.x1*point.x2*self.x1x2

points = []
points.append(Point(-1, 0, 1))
points.append(Point(1, 1, 1))
points.append(Point(2, 0, 2))
points.append(Point(1, -2, 2))

mainFunc = Func()
mainFunc.SetZero()


flag = True
operation = True
while flag:
    i = 1
    for point in points:
        if (flag):
            if (operation):
                mainFunc = mainFunc + Func().NewFactor(point)
            else:
                mainFunc = mainFunc - Func().NewFactor(point)
        val = mainFunc.GetValue(points[i])
        if (val <= 0 and points[i].cl == 1):
            operation = True
        if (val > 0 and points[i].cl == 2):
            operation = False
        if (val > 0 and points[i].cl == 1) or (val < 0 and points[i].cl == 2):
            flag = False
        print(val)
        i += 1
        if (i == len(points)):
            i = 0

print(mainFunc.__dict__)
fig, ax = plt.subplots()
minX = -5.0
maxX = 5.0
x = np.linspace(minX,maxX,200)
y = (-mainFunc.c - mainFunc.x1 * x)/(mainFunc.x2 + mainFunc.x1x2*x)
y = np.ma.array(y)


flag = True;
i = 0
maxIn = 0
minIn = 0
for el in y:
    if (el == y.max()):
        maxIn = i
    if (el == y.min()):
        minIn = i
    i += 1
if (minIn > maxIn):
    maxEl = x[maxIn]
    minEl = x[minIn]
else:
    maxEl = x[minIn]
    minEl = x[maxIn]
ax.plot(x[x <= maxEl], y[x <= maxEl], c = "#FF00FF", linewidth = 2)
ax.plot(x[x >= minEl], y[x >= minEl], c = "#FF00FF", linewidth = 2)
for i in range(150):
    randY = random.uniform(int(y.min()),int(y.max()))
    randX = random.uniform(int(minX),int(maxX))
    points.append(Point(randX,randY,0))
for point in points:
    if (mainFunc.GetValue(point) > 0):
        ax.scatter(point.x1,point.x2,s=50, c='#2EF011', linewidths = 1,
                       edgecolors = 'black')
    if (mainFunc.GetValue(point) < 0):
        ax.scatter(point.x1,point.x2,s=50, c='#25DCEA', linewidths = 1,
                       edgecolors = 'black')
    if (mainFunc.GetValue(point) == 0):
        ax.scatter(point.x1,point.x2,s=50, c='#FF00FF', linewidths = 1,
                       edgecolors = 'black')
plt.show()

