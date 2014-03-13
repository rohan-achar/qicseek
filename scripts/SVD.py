import json
import string
from time import sleep
import numpy as np
from scipy.sparse import linalg

PROJ_FOLDER = "../FinalSet/"
TESTBED_DOC_ID = PROJ_FOLDER+"DocId.tsv"
INDEX_FOLDER = PROJ_FOLDER+"Index/"
NUM_OF_DOCIDS = 46911 # Ideally read from DocId.tsv

tempDict = {}
totalIndexCount = 0 

for char in string.ascii_lowercase:
	fileObj = open(INDEX_FOLDER+'indexDump-'+char+'.json')
	tempDict[char] = json.load(fileObj)
	totalIndexCount += len(tempDict[char])
	fileObj.close()

print "Total no. of terms : "+str(totalIndexCount)

tdMatrix = [[0.0]*NUM_OF_DOCIDS]*totalIndexCount

termId = 0
for char in string.ascii_lowercase:
	for key in tempDict[char]:
		for postId in range(tempDict[char][key][0]):
			tdMatrix[termId][int(tempDict[char][key][1][postId][0])] = float(tempDict[char][key][1][postId][2]) 
		termId += 1
		if(termId%1000 == 0):
			print termId
while True:
	sleep(100)
file = open("svd.txt", "w")
v = 1
for i in tdMatrix:
	file.write(str(i)[1:-1] + "\n")
	if (v%1000 == 0):
		print(v)
	v +=1
file.close()
print(len(tdMatrix))

		 


