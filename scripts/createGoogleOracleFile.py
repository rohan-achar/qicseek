import json
from time import sleep
import pygoogle as pyg

PROJ_FOLDER = "../FinalSet/"
TESTBED_DOC_ID = PROJ_FOLDER+"DocId.tsv"
GOOGLE_ORACLE = PROJ_FOLDER+"google-oracle.json" # Ideally this file would be replaced by real time calls to a Google Search API
GOOGLE_ORACLE_FILTERED = PROJ_FOLDER+"google-oracle-filtered-5.json"
MAX_NUM_RESULTS = 5

docIdFile = open(TESTBED_DOC_ID,"r")
docIdMapList = docIdFile.readlines()
docIdFile.close()

urlDict = {}

count = 0
for line in docIdMapList:
	lineSplits = line.strip('\n').split()
	if(len(lineSplits) > 0):
		urlDict[lineSplits[1]] = lineSplits[0]
	if(count%1000 == 0):
		print(count)
	count += 1

print(len(urlDict))

oracleFile = open(GOOGLE_ORACLE)
queryTestDictInitial = json.load(oracleFile)
oracleFile.close()

queryTestDict = {}

def stripAddSlash(urlText):
	tempList = [urlText]
	if(urlText[-1] == "/"):
		tempList.append(urlText.strip("/"))
	else:
		tempList.append(urlText+"/")
	return tempList

#Conflate Google Results
for term in queryTestDictInitial:
	for url in queryTestDictInitial[term]:
		if term in queryTestDict:
			queryTestDict[term].extend(stripAddSlash(url))
		else:
			queryTestDict[term] = stripAddSlash(url)

oracleFilterDict = {}

for queryTerm in queryTestDict:
	for url in queryTestDict[queryTerm]:
		if(url in urlDict):
			if(queryTerm in oracleFilterDict):
			 	if len(oracleFilterDict[queryTerm]) < MAX_NUM_RESULTS:
					oracleFilterDict[queryTerm].append(url)
			else:
				oracleFilterDict[queryTerm] = [url]

oracleFilteredFile = open(GOOGLE_ORACLE_FILTERED,'w')
json.dump(oracleFilterDict, oracleFilteredFile, indent=4, separators=(',', ': '))
oracleFilteredFile.close()