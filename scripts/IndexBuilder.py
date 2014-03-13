import json
import math
import re
from collections import OrderedDict

PROJ_FOLDER = "../FinalSet/"
TESTBED_DOC_ID = PROJ_FOLDER+"DocId.tsv"
PFQ_FOLDER = PROJ_FOLDER+"Pfq/"
INDEX_FOLDER = PROJ_FOLDER+"Index/"

indexDict = {}

def getFileLines(fileName):
	tempFile = open(fileName, "r")
	tempLines = tempFile.readlines()
	tempFile.close()
	return tempLines

def deltaEncode(numList):
	tempList = []
	prevItem = 0
	for n in numList:
		tempList.append(int(n)-prevItem)
		prevItem = int(n)
	return tempList

def mergeIndicesToDict(pfqFileName, docId):
	pfqLines = getFileLines(PFQ_FOLDER+pfqFileName+".pfq")
	for line in pfqLines:
		lineSplits = line.strip().split(",\t")
		if(len(lineSplits) > 0):
			term = lineSplits[0].lower()

			if('a' <= term[0] <= 'z') and re.match("^[A-Za-z0-9_@.-]+$", term):
				# termFreq,posList = int(lineSplits[1]),deltaEncode(lineSplits[2].split("|"))
				#termFreq,posList = int(lineSplits[1]),[int(i) for i in lineSplits[2].split("|")]
				#posting = [docId,termFreq,0,posList]
				termFreq = int(lineSplits[1])
				posting = [docId,termFreq,0]
				if(term in indexDict):
					indexDict[term][1].append(posting)
				else:
					indexDict[term] = [0,[posting]]

def updateTfIdf():
	docFreq = 0
	N = len(indexDict)
	for term in indexDict:
		docFreq = len(indexDict[term][1])
		indexDict[term][0] = docFreq
		for i in range(docFreq):
			indexDict[term][1][i][2] = round((1+math.log(indexDict[term][1][i][1],10)) * math.log(N/docFreq,10),1) 

docIdFile = open(TESTBED_DOC_ID,"r")
docIdMapList = docIdFile.readlines()
docIdFile.close()

count = 0
for line in docIdMapList:
	lineSplits = line.strip('\n').split()
	if(len(lineSplits) > 0):
		mergeIndicesToDict(lineSplits[2],lineSplits[0])
	if(count%1000 == 0):
		print(count)
	count += 1

updateTfIdf()

charChunkedDict = {}

for term in indexDict:
	if(term[0] in charChunkedDict):
		charChunkedDict[term[0]][term] = indexDict[term]
	else:
		charChunkedDict[term[0]] = {}

def sortByDocFreq(termItem):
	keys = list(termItem.keys())
	return termItem[keys[0]][0]

print(len(charChunkedDict))

for alpha in charChunkedDict:
	charChunkedDict[alpha] = OrderedDict(sorted(charChunkedDict[alpha].items(), key=lambda t: t[1][0], reverse=True))
	if('a' <= alpha <= 'z'):
		indexFileSuffix = alpha	
	else:
		indexFileSuffix = 'special'
	print(alpha)
	json.dump(charChunkedDict[alpha], open(INDEX_FOLDER+'indexDump-'+indexFileSuffix+'.json','w'))


#json.dump(indexDict, open('indexDump.json','w'))

print(len(indexDict))
