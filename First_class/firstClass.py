from math import *

class Point:
    x = 0
    y = 0

    def __init__(self, xaxis, yaxis):
        self.x = xaxis
        self.y = yaxis
    
    def getTupleOfCoordinates(self):
        return (self.x, self.y)
    
    def setTupleOfCoordinates(self, x, y): # set_location
        self.x = x
        self.y = y

    def translate(self, xAdded, yAdded):
        self.x += xAdded
        self.y += yAdded

    def getPointTranslate(self, xAdd, yAdd):
        return (self.x + xAdd, self.y + yAdd)
    
    def distanceBetweenTwoPoints(p1, p2): # distance
        print("p1( "+str(p1.x)+", "+str(p1.y)+")"+"--p2( "+str(p2.x)+", "+str(p2.y)+")")
        return sqrt( (p1.x - p2.x)**2 + (p1.y - p2.y) )

    def distanceFrom(self, p):
        return self.distanceBetweenTwoPoints(p)

    def distanceFromOrigin(self):
        return self.distanceFrom( Point(0, 0) )