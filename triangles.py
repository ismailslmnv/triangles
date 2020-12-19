import math

def init(tipAngle, radius):
    equalAngle = calcEqualAngles(tipAngle)
    hipotenus = calcHipotenus(equalAngle, radius)
    root = calcRoot(tipAngle, hipotenus)
    area = calcArea(root,radius)
    print("Equal angles of triangle:",equalAngle)
    print("Hipotenus of triangele:",hipotenus)
    print("Root of triangle:",root)
    print("Area of triangle:",area)
    return area
def calcEqualAngles(tipAngle):
    return (180 -tipAngle)/2
def calcHipotenus(equalAngle, radius):
    return radius/math.sin(math.radians(equalAngle))
def calcRoot(tipAngle, hipotenus):
    halfTipAngle = tipAngle/2
    return math.sin(math.radians(halfTipAngle))*2*hipotenus
def calcArea(root,radius):
    return root*radius/2
#init(50,9.06362924)