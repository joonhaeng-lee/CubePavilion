print "\nstart!!!!!"
import itertools

n=4
sampleList = ((0, 1, 2, 3), (1, 0, 3, 2), (2, 3, 1, 0), (3, 2, 0, 1))
count = 0
def rotate(sampleList):
	temp = []
	for i in range(0,n):
		temp.append([])
		for j in range(0,n):
			temp[i].append(sampleList[j][(n-1)-i])
	return temp ;
def vrotate(sampleList):
	temp= []
	for i in range (0, n):
		temp.append([])
		for j in range(0,n):
			temp[i].append(sampleList[i].index(n-1-j))
	return temp ;
def Mrotate(sampleList,k):
	for x in range(0,k):
		sampleList = rotate(sampleList)
	return sampleList
def Mvrotate(sampleList,k):
	for x in range(0,k):
		sampleList = vrotate(sampleList)
	return sampleList
def getallrotate(sampleList):
	
	temp=[]
	for i in range(1,n+1):
		for j in range(1,n+1):
			temp.append(Mvrotate(Mrotate(sampleList,j),i))
	
	temp2=[]

	##to much calculation here
	for i in range(0, len(temp)):

		test =0
		for j in range (0,len(temp2)):

			if (temp[j]==temp[i]):test = test+1

		if(test==0):temp2.append(temp[i])

	return temp2

toprint = getallrotate(sampleList)
print "all combinations: \n", toprint, "\ntotal length of list is ", len(toprint) ,"\n"

print "\n\nMain Job"
n=4
cube = []
cubesum = 0 
numcheck = 0
test = 0
allcombination = []

for i in range (0,n):
	cube.append(i)
	cubesum = cubesum+i

print "Cube:",cube

nList = list(itertools.permutations(cube, n))
print "nList: \n" ,nList , "\nnList count : ", len(nList)

cList = list(itertools.permutations(nList, n))
print "combinationList count ",len(nList),"C",n,"=",len(cList)

pList = []
for i in range(0,len(cList)):

	for j in range (0,n):
		temp = []
		for k in range(0,n):
			temp.append(cList[i][k][j])
		uniq = []
		for x in temp:
		    if x not in uniq:
		        uniq.append(x)
		

		if (len(uniq)==n):
			test = test+1


	if (test == n ): 
		allcombination.append(cList[i])
		##print pList
		##print cList[i]

	test = 0
	pList = []
print "all possible combinations are ", len(allcombination)
##print allcombination

allCoExRo = []

for i in range (0,len(allcombination)):
	'''
	print rotate(allcombination[i])
	print rotate(rotate(allcombination[i]))
	print rotate(rotate(rotate(allcombination[i])))
	print rotate(rotate(rotate(rotate(allcombination[i]))))
	'''
	test2 =0;
	for j in range ( 0,len(allCoExRo)):
		##print "current com is ",allCoExRo[j]
		
		if ( rotate(allCoExRo[j])== rotate(allcombination[i]) or rotate(allCoExRo[j])== rotate(rotate(allcombination[i])) or rotate(allCoExRo[j])==rotate(rotate(rotate(allcombination[i]))) or rotate(allCoExRo[j])==rotate(rotate(rotate(rotate(allcombination[i])))) ):
			test2 = test2+1
		"""		
		testlist =  getallrotate(allcombination[i])
		for x in range(0,len(testlist)):
			if (Mrotate(allCoExRo[j],4)==testlist[x]):
				test2 = test2+1
		"""

	if (test2==0): 
		
		count =count+1
		##print "I found one " ,count
		allCoExRo.append(allcombination[i])

print allCoExRo
print "all possible combinations except duplicated rotation are " , len(allCoExRo)




