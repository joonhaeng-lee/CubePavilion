print "\nstart!!!!!"
import itertools


sampleList = [[0, 2, 3, 1, 4], [3, 1, 4, 0, 2], [2, 4, 0, 3, 1], [4, 3, 1, 2, 0], [1, 0, 2, 4, 3]]



n=5

print len(sampleList)
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
			##print Mvrotate(Mrotate(sampleList,j),i)

	temp2=[]

	for i in range(0, len(temp)):
		test =0
		for j in range (0,len(temp2)):
			
			if (temp[j]==temp[i]):test = test+1

		if(test==0):temp2.append(temp[i])

	return temp2
##print "\n"
##print Mvrotate(Mrotate(sampleList,1),3)
##print "\n"
toprint = getallrotate(sampleList)
print "all combinations: ", toprint, "\n total length of list is ", len(toprint)




