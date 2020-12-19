import math
import triangles
import time

def splitCircle(radius,nNumbers=7):
    internalAngles = 360/nNumbers
    areaOfTriangle =triangles.init(internalAngles,radius)
    sumArea = areaOfTriangle*nNumbers
    print("Calculated Area:",sumArea)
    return sumArea
def calcErrorRate(realValue, calculatedValue):
    return abs(((realValue-calculatedValue)/realValue)*100)
def main():
    realAreaOfCircle = 314.159265359
    realRadius = 10
    errorRate = 1.0
    indexNum = 7
    timeStart = time.time()
    while errorRate > 0.00001:
        print("Split Index:", indexNum)
        calculatedArea = splitCircle(realRadius, indexNum)
        errorRate = calcErrorRate(realAreaOfCircle,calculatedArea)
        print("Error Rate:",errorRate)
        indexNum+=1
    timeEnd = time.time()
    totalTime = timeEnd - timeStart
    print("Total to Calc (sec):",totalTime)
main()