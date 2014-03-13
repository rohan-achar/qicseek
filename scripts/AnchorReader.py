from lxml import html
# use ElementSoup to deal with really broken pages
# use UnicodeDammit for encoding detection
import re,json

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
	links = {'a': htmlFile.xpath('//a',smart_strings=False), 
		'title': htmlFile.xpath('//title',smart_strings=False), 
		'h1': htmlFile.xpath('//h1',smart_strings=False), 
		'h2': htmlFile.xpath('//h2',smart_strings=False), 
		'h3': htmlFile.xpath('//h3',smart_strings=False), 
		'h4': htmlFile.xpath('//h4',smart_strings=False), 
		'h5': htmlFile.xpath('//h5',smart_strings=False), 
		'h6': htmlFile.xpath('//h6',smart_strings=False), 
		'u': htmlFile.xpath('//u',smart_strings=False), 
		'b': htmlFile.xpath('//b',smart_strings=False), 
		'i': htmlFile.xpath('//i',smart_strings=False)}
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

linkinkMap = []
externalLinks = []
count = 0

docIdTitle = {}


count = 1
for url in docIdUrlMapDict:
	outLinks = htmlFileGetTags(docIdUrlMapDict[url][1], url)
	if count % 1000 == 0:
		print(count)
	count += 1
	for item in outLinks:
		if item == 'a':
			for link in outLinks[item]:
				linkdict = dict(link.items())
				if 'href' in linkdict:
					urlgot = linkdict['href']
				else:
					continue
				if urlgot in docIdUrlMapDict:
					docid = docIdUrlMapDict[urlgot][0]
					if docid not in docIdTitle:
						docIdTitle[docid] = {}
						docIdTitle[docid][item] = []
					elif item not in docIdTitle[docid]:
						docIdTitle[docid][item] = []
					docIdTitle[docid][item].append(link.text_content())
			continue

		for link in outLinks[item]:
			docid = docIdUrlMapDict[url][0]
			if docid not in docIdTitle:
				docIdTitle[docid] = {}
				docIdTitle[docid][item] = []
			elif item not in docIdTitle[docid]:
				docIdTitle[docid][item] = []
			docIdTitle[docid][item].append(link.text_content())



docidtitles = open(PROJ_FOLDER + "docidtitle.json", "w")
json.dump(docIdTitle, docidtitles, indent=4, separators=(',', ': '))
	#print(outLinks[0].xpath('//a', smart_strings = False))
	# if count%1000 == 0:
	# 	print(count)
	# count +=1
	# for eachLink in outLinks:
	# 	destination = -2
	# 	if eachLink in docIdUrlMapDict:
	# 		destination = docIdUrlMapDict[eachLink][0]  
	# 	else:
	# 		externalLinks.append(eachLink)
	# 		if(eachLink.find(".ics.uci.edu") != -1):
	# 			destination = -1
	# 	linkMap.append((docIdUrlMapDict[url][0],destination))


# dotFile = open("pageRankLayout.dot","w")
# dotFile.write("digraph PG {\n")
# edgesBigString = ''
# for nodePair in linkMap:
# 	edgesBigString += "\t" + str(nodePair[0]) + "->" + str(nodePair[1]) + ";\n"
# dotFile.write(edgesBigString + "}")
# dotFile.close()	


# externalLinksFile = open("linksBeyond.txt","w", encoding='utf-8')
# externalLinkString = ''
# for eachLink in externalLinks:
# 	externalLinkString += str(str(eachLink).encode('utf-8').strip()) + "\n"
# externalLinksFile.write(externalLinkString)
# externalLinksFile.close()

# print("No. of DocID's : " + str(len(docIdUrlMapDict)))
# print("No. of external links : " + str(len(externalLinks)))