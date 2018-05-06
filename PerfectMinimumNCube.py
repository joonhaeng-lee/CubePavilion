"""
Perfect Minimum N Cube

Joonhaeng Lee

"Perfect Minimum N Cube" concept was developed during pavilion design project on yonsei university architectural design studio 3, 2010.
Initially, possible combination of Perfect Minimum N cube (n = 4) were hand calculated with help of Kangdacool.
2016, development of code started to generate possible combination of Perfect Minimum N Cube.

"""

"""

N : integer

Cube: Cube which edges length are 1. Cube exist on 3 dimentional space and all of it's edges are on X = c,y = c ,or Z = c. 

NCube: Group of Cubes, contains N*N*N Cubes. length of each edge on NCube are N.

SubNCube: subgroup of NCube.

Perfect: let's difine SubNCube is "PERFECT" When projected SubNCube on Xy, yZ, XZ plane makes full N*N size square without empty space.

Perfect Minimum N Cube: SubNCube which is Perfect and have N*N Cubes.

Perfect Minimum N Cube representation: 
Perfect Minimum N Cube is reperesented by nested List Z. 
Z = [ y0,y1,y2,...,y(N-1) ]

Each List yk have N unique numbers in range of (0, n-1) 

"""



"""
## SET INPUT PARAMETER
"""
n=5

"""
##  Scenario 1 : initialize Z[0] layer, by shuffling y
##  Scenario 2 : from Z[1] to Z[n] do insert or pull out by checking yBelow,yBlackList and tempZ   
"""

"""
## Initialize lists
"""

import random

## set empty list for single layer(XY plane) of cubes
y=[]

## set empty list for first layer(XY plane) of Perfect Minimum N Cubes
yBottom= []

## set empty list for already occupied y values of Perfect Minimum N Cubes
yBelow = []

## set empty list for y value which cannot be placed even if y is not already occupied.
yBlackList=[]

Z=[]
tempZ =[]
log=[0]

 
"""
##  Scenario 1
"""
print "\nScenario 1" 

##initial Z[],yBottom[],yBelow[],yBlackList[]

for i in range(0,int(n)):
    Z.append([])
    yBelow.append([])
    yBlackList.append([])
    yBottom.append(i)
    y.append(i)


##insert y to Z[0]
random.shuffle(y)
Z[0]=y

for i in range(0,int(n)):
    yBelow[i].append(y[i])

y = []
print "\nZ[0] is " +str(Z)


"""
doPlacing(c) insert or pull out layer y on existing Z.
"""

def doPlacing(c) :
    x=int(n-c)


    y= yBottom
    y= list (set(y)- set(tempZ))
    y= list (set(y)- set(yBelow[x]))
    y= list (set(y)- set(yBlackList[x]))
    print "\n\nwhen x is " + str(x)+"\nyBelow : "+str(yBelow[x]) +"\nyBlackList : " +  str(yBlackList) +"\nLog : "+str(log)+"\navilable y : " + str(y)
    
    if int(len(y))==0:
        
        print "'****PULL OUT CASE****' "
        if log[-1] == 1 :
            for h in range(int(x),int(n)):
                yBlackList[h][:]=[]
            print"repeated pop number, yBlackList Empty"
            print "yBlackList : " + str(yBlackList)
        print "tempZ : "+ str(tempZ)
        sy = tempZ.pop()
        yBelow[x-1].pop()
        yBlackList[x-1].append(sy)
        print "yBlackList update:"+str(yBlackList)
        log.append(1)
        c=int(c+1)


    else:
        print "'++++INSERT CASE++++' "
        randomtemp = random.choice(y)
        tempZ.append(randomtemp)
        print "random selected y is " +str(randomtemp)
        print "tempZ is "+ str(tempZ)
        yBelow[x].append(randomtemp)
        print "yBelow "+str(x)+" is " + str(yBelow[x])
        c=int(c-1)
        log.append(0)

    if c is not 0 :
        doPlacing(c)


        
"""
##  Scenario 2
"""
print "\nSenario 2"

for i in range(1,int(n)):

    
    doPlacing(n)

    Z[i]= tempZ
    tempZ=[]
    log = []
    print "!!!Placing finished, Z["+str(i)+"] inseted!!!"
    print "\nZ : "+str(Z)

    for h in range(0,int(n)):
        yBlackList[h][:]=[]


print "\n\nCOMPLETE : Perfect Minimum N Cube combination \n " +str(Z)


"""
Perfect Minimun N Cube example:

N = 1
[[0]]

N = 2
[[0, 1], [1, 0]]

N = 3
[[0, 2, 1], [2, 1, 0], [1, 0, 2]]

N = 4
[[3, 0, 1, 2], [1, 2, 0, 3], [0, 3, 2, 1], [2, 1, 3, 0]]

N = 5
[[0, 2, 3, 1, 4], [3, 1, 4, 0, 2], [2, 4, 0, 3, 1], [4, 3, 1, 2, 0], [1, 0, 2, 4, 3]]

...
"""