from lxml import html
# use ElementSoup to deal with really broken pages
# use UnicodeDammit for encoding detection
import re
import io

def htmlFileGetTags(htmlFileName, base_url):

	# def rewriteHrefUrls(link):
	# 	if(link[:4] == "www.") or (link.find('://') != -1) :
	# 		return link
	# 	else:
	# 		return "/".join(base_url.split("/")[:-1])+"/"+link
	htmlFile = html.parse(htmlFileName).getroot()
	if(htmlFile == None):
		return []
	htmlFile.make_links_absolute(base_url)
#	htmlFile.rewrite_links(rewriteHrefUrls, base_href=None)
	links = htmlFile.xpath('//a/@href',smart_strings=False)
#	print links
	return links

#HTML_FOLDER = "/home/siva/w14_inf225/Assignment 3/FinalSet/DocId.tsv"
PROJ_FOLDER = "../"
HTML_FOLDER = PROJ_FOLDER+"FinalSet/Html/"
TESTBED_DOC_ID = PROJ_FOLDER+"FinalSet/DocId.tsv"
	
#htmlFileGetTags("/home/siva/w14_inf225/Assignment 3/FinalSet/Html/access.ics.uci.edupartnerships.html", "http://access.ics.uci.edu/partnerships.html")
#htmlFileGetTags("/home/siva/w14_inf225/Assignment 3/FinalSet/Html/www.ics.uci.edu~ics1chw434.html","http://www.ics.uci.edu/~ics1c/hw4/34.html")
#htmlFileGetTags(HTML_FOLDER+"soc.ics.uci.eduResourcesfileCmd.phpretr2B510","http://soc.ics.uci.edu/Resources/fileCmd.php?retr%2B510")

docIdFile = open(TESTBED_DOC_ID,"r")

docIdMapList = docIdFile.readlines()
docIdFile.close()

docIdUrlMapDict = {}

for line in docIdMapList:
	lineSplits = line.strip('\n').split()
	if(len(lineSplits) > 0):
		docIdUrlMapDict[lineSplits[1]] = (lineSplits[0],HTML_FOLDER+lineSplits[2]) # {url : (doc_id, file_name)}

linkMap = []
externalLinks = []
count = 0

for url in docIdUrlMapDict:
	outLinks = htmlFileGetTags(docIdUrlMapDict[url][1], url)
	if count%1000 == 0:
		print(count)
	count +=1
	for eachLink in outLinks:
		destination = -2
		if eachLink in docIdUrlMapDict:
			destination = docIdUrlMapDict[eachLink][0]  
		else:
			externalLinks.append(eachLink)
			if(eachLink.find(".ics.uci.edu") != -1):
				destination = -1
		linkMap.append((docIdUrlMapDict[url][0],destination))


dotFile = open("pageRankLayout.dot","w")
dotFile.write("digraph PG {\n")
edgesBigString = ''
for nodePair in linkMap:
	edgesBigString += "\t" + str(nodePair[0]) + "->" + str(nodePair[1]) + ";\n"
dotFile.write(edgesBigString + "}")
dotFile.close()	


externalLinksFile = io.open("linksBeyond.txt","w", encoding='utf-8')
externalLinkString = ''
for eachLink in externalLinks:
	externalLinkString += str(str(eachLink).encode('utf-8').strip()) + "\n"
externalLinksFile.write(externalLinkString)
externalLinksFile.close()

print("No. of DocID's : " + str(len(docIdUrlMapDict)))
print("No. of external links : " + str(len(externalLinks)))