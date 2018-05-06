"""
Perfect Minimum N Cube
Joonhaeng Lee
2018-05
"""


## SET INPUT PARAMETER
n = int(raw_input("\n\n###Perfect Minimum N Cube Generator Start!!###\n\nPlease enter integer smaller than 20: "))

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


"""
doPlacing(c) insert or pull out layer y on existing Z.
"""

def doPlacing(c) :
    x=int(n-c)


    y= yBottom
    y= list (set(y)- set(tempZ))
    y= list (set(y)- set(yBelow[x]))
    y= list (set(y)- set(yBlackList[x]))

    if int(len(y))==0:
        
        ## print "'****PULL OUT CASE****' "
        if log[-1] == 1 :
            for h in range(int(x),int(n)):
                yBlackList[h][:]=[]

        sy = tempZ.pop()
        yBelow[x-1].pop()
        yBlackList[x-1].append(sy)
        log.append(1)
        c=int(c+1)


    else:
        ## print "'++++INSERT CASE++++' "
        randomtemp = random.choice(y)
        tempZ.append(randomtemp)
        yBelow[x].append(randomtemp)
        c=int(c-1)
        log.append(0)

    if c is not 0 :
        doPlacing(c)


        
"""
##  Scenario 2
"""

for i in range(1,int(n)):

    
    doPlacing(n)

    Z[i]= tempZ
    tempZ=[]
    log = []

    for h in range(0,int(n)):
        yBlackList[h][:]=[]


print "\nPerfect Minimum N Cube combination sample (N ="+str(n)+") :\n " +str(Z) +"\n\n"


