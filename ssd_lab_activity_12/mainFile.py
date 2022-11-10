from math import sqrt
from datetime import datetime
import sys
def readingInputFromTxt(quesNum):
    # store row and column of non zero values
    footMatrix=[]  
    #  median time at which mat contains non zero values
    matrixOfTime=[]
    f = open("data.txt", "r")
    rowMat=[]
    countRow=0
    ct=0
    for ptr in f:
        length=len(ptr)
        if(length!=1):
            intermediate=(ptr.strip()).split('\t')
            time=intermediate[0]
            b=intermediate[1:]
            for index, value in enumerate(b):
                ct=0
                if(value=='0'):
                    ct+=1
                else:    
                    rowMat.append((countRow,index))

            if(countRow==20):
                matrixOfTime.append(time)

            countRow=countRow+1     
        else:
            # this means one matrix over and store non zero values into footmatrix
            footMatrix.append(rowMat)
            rowMat=[]
            countRow=0; 
    f.close()
    if(quesNum==2):
        matIndex=[8,9,16]
        matrix=[]
        timeMat=[]
        for ind,value in enumerate(footMatrix):
            if(ind in matIndex):
                matrix.append(value)
        for ind, value in enumerate(matrixOfTime):
            if(ind in matIndex):
                timeMat.append(value)

        footMatrix=matrix
        matrixOfTime=timeMat

    return footMatrix,matrixOfTime            
    # till now store all the non zero values and time

def printingDesiredOutput(leftDistance,startingTime,endTime):
    print("Stride"+" length is:" +" {}".format(leftDistance))
    final=datetime.strptime(endTime,'%H:%M:%S.%f')
    start=datetime.strptime(startingTime,'%H:%M:%S.%f')

    totalTime=(final-start).total_seconds()

    print("Stride"+" Velocity is: "+"{}".format(leftDistance/totalTime),"units")
    print("Cadence is:"+" (steps / minute) "+"{}".format(120/totalTime))

def mainlogic(footMatrix,matrixOfTime): 
    rowPtr=colPtr=0
    leftMove=()
    rightMove=()

    initialLeftMove=()
    initialRightMove=()

    startingTime=endTime=leftDistance=rightDistance=status=0
    for (p,rowPtr) in enumerate(footMatrix):
        for (q,colPtr) in enumerate(rowPtr):
            if(len(leftMove)!=status and len(rightMove)==status and colPtr[status]!=leftMove[status]):
                rightMove=colPtr
                initialRightMove=colPtr
                break
                
            elif(len(leftMove)==status and len(rightMove)==status and len(rowPtr)!=status):
                leftMove=colPtr
                initialLeftMove=colPtr
                startingTime=matrixOfTime[p]
                break

            else:
                if (len(rightMove)):
                    if colPtr[status] not in range(rightMove[status]-3,rightMove[status]+4):
                        leftDistance=leftDistance+sqrt(((colPtr[status]-leftMove[status])**2)+((colPtr[1]-leftMove[1])**2))
                        leftMove=colPtr
                        if(endTime==status):
                            endTime=matrixOfTime[p]
                    else:
                        rightMove=colPtr
                    break

                elif(len(leftMove)):
                    if colPtr[status] not in range(leftMove[status]-3,leftMove[status]+4):
                        rightDistance=rightDistance+sqrt(((colPtr[status]-rightMove[status])**2)+((colPtr[1]-rightMove[1])**2))
                        rightMove=colPtr
                    else:
                        leftMove=colPtr
                    break

                elif colPtr[status]!=status:
                    break

    printingDesiredOutput(leftDistance,startingTime,endTime)

if __name__=="__main__":
    length=len(sys.argv)
    if length==2:
        typeOfQues=sys.argv[1]
        footMatrix=[]
        matrixOfTime=[]
        if typeOfQues=="q2":
            footMatrix,matrixOfTime=readingInputFromTxt(2)

        elif typeOfQues=="q1":
            footMatrix,matrixOfTime=readingInputFromTxt(1) 

        else:
            raise ValueError('Incorrect question number')

        mainlogic(footMatrix,matrixOfTime)
    else:
        raise ValueError('Incorrect number of arguments')
        