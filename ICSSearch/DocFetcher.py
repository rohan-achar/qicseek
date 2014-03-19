from __future__ import print_function
import os
import json
from io import open
import time
import nltk
import sets
import Trie
import copy
import math
from math import log10
from sets import Set

src = "../FinalSet/"
htmlPath = src + "Html/"
list_of_bad_files = []
picklefile = src + "IndexPickle.json"
docidfile = src + "DocId.tsv"
pagerankfile = src + "pagerank.tsv"
docidjson = src + "docIdLoaded.json"
hashfile = src + "HashFile.json"
oraclefile = src + "google-oracle-filtered.json"
formulafile = src + "secretingredient.txt"
docdict = {}
stops = {}
ndcgDict = {}
snippetDict = {}
MAX_NUM_RESULTS = 10
RELEVANCE_SPREAD = 2.0 # For 10 terms => google relevance scores = [5,5,4,4,3,3,2,2,1,1]
SIZE_TO_CHECK = 30
wnl = nltk.WordNetLemmatizer()

def LoadTrie():
    stops = dict([(i , 1) for i in "a a's   able    about   above   according accordingly   across  actually    after   afterwards again    against ain't   all allow allows    almost  alone   along   already also    although    always  am  among amongst   an  and another any anybody anyhow  anyone  anything    anyway anyways  anywhere    apart   appear  appreciate appropriate  are aren't  around  as aside    ask asking  associated  at available    away    awfully be  became because  become  becomes becoming    been before beforehand  behind  being   believe below   beside  besides best    better between  beyond  both    brief   but by  c'mon   c's came    can can't   cannot  cant    cause   causes certain  certainly   changes clearly co com  come    comes   concerning  consequently consider   considering contain containing  contains corresponding  could   couldn't    course  currently definitely    described   despite did didn't different    do  does    doesn't doing don't done    down    downwards   during each edu eg  eight   either else elsewhere   enough  entirely    especially et   etc even    ever    every everybody everyone    everything  everywhere  ex exactly  example except  far few fifth   first   five    followed    following follows   for former  formerly    forth four  from    further furthermore get gets    getting given   gives   go goes going   gone    got gotten greetings    had hadn't  happens hardly has  hasn't  have    haven't having he   he's    hello   help    hence her   here    here's  hereafter   hereby herein   hereupon    hers    herself hi him  himself his hither  hopefully how   howbeit however i'd i'll i'm    i've    ie  if  ignored immediate   in  inasmuch    inc indeed indicate indicated   indicates   inner   insofar instead into    inward  is  isn't it    it'd    it'll   it's    its itself  just    keep    keeps   kept know   known   knows   last    lately later    latter  latterly    least   less lest   let let's   like    liked likely    little  look    looking looks ltd   mainly  many    may maybe me    mean    meanwhile   merely  might more  moreover    most    mostly  much must   my  myself  name    namely nd   near    nearly  necessary   need needs  neither never   nevertheless    new next    nine    no  nobody  non none    noone   nor normally    not nothing novel   now nowhere obviously of    off often   oh  ok okay old on  once    one ones    only    onto    or  other others    otherwise   ought   our ours ourselves  out outside over    overall own particular  particularly    per perhaps placed  please  plus    possible    presumably probably provides    que quite   qv rather   rd  re  really  reasonably regarding    regardless  regards relatively  respectively right  said    same    saw say saying  says    second  secondly    see seeing  seem    seemed  seeming seems seen  self    selves  sensible    sent serious    seriously   seven   several shall she   should  shouldn't   since   six so  some    somebody    somehow someone something   sometime    sometimes   somewhat    somewhere soon  sorry   specified   specify specifying still    sub such    sup sure t's    take    taken   tell    tends th    than    thank   thanks  thanx that  that's  thats   the their theirs    them    themselves  then    thence there    there's thereafter  thereby therefore therein   theres  thereupon   these   they they'd they'll they're they've think third this    thorough    thoroughly  those though    three   through throughout  thru thus   to  together    too took toward towards tried   tries   truly try   trying  twice   two un under    unfortunately   unless  unlikely    until unto  up  upon    us  use used    useful  uses    using   usually value   various very    via viz vs  want    wants   was wasn't way  we  we'd    we'll   we're we've welcome well    went    were weren't    what    what's  whatever    when whence whenever    where   where's whereafter whereas  whereby wherein whereupon   wherever whether    which   while   whither who who's   whoever whole   whom    whose why   will    willing wish    with within without won't   wonder  would wouldn't  yes yet you you'd you'll    you're  you've  your    yours yourself  yourselves  zero".split()])
    print(len(stops))    
    start = time.clock()
    print ("Loading To memory")
    if os.access(picklefile, os.F_OK) and os.access(hashfile, os.F_OK):
        Trie.IndexTrie = json.load(open(picklefile, "rb"))
        Trie.FinalMapDict = dict([(int(item), value) for item, value in json.load(open(hashfile, "rb")).items()])
        print ("\nLoad Complete in: ", time.clock() - start)
        #Trie.Duplicates(Trie.IndexTrie)
        #Trie.Statistics()
    else:
        print ("                          |\r", end = "")
        def LoadIndex(filename):
            jsonData = json.load(open(filename, "r", encoding="utf8"))
            count = 1
            for i in jsonData:
                Trie.AddKeyToTrie(i, jsonData[i])
                
                #if (count%10 == 0):
                #    print("done with ", count, " terms")
                count += 1
            print ("=", sep="", end="")

        indexsrc = src + "Index/"
        list_threads = []
        for file in os.listdir(indexsrc):
            #list_threads.append(Thread(target = LoadIndex, args = (src + file,)))
            #list_threads[-1].start()
            LoadIndex(indexsrc + file)
        del Trie.IncDict
        #for thread in list_threads:
        #    thread.join()    

        #AddKeyToTrie("abcd", 100)
        #AddKeyToTrie("add", 100)
        #AddKeyToTrie("abc",100)
        #AddKeyToTrie("abcde", 100)
        #AddKeyToTrie("abcdf",100)
        #AddKeyToTrie("abdef", 100)
        #AddKeyToTrie("abcdek", 100)
        print ("\nLoad Complete in: ", time.clock() - start)
        start = time.clock()   
        print ("Verifying Index Sanity")
        print ("                          |\r", end = "")
        bad_values = []
        timing = []
        for file in os.listdir(indexsrc):
            jsonData = json.load(open(indexsrc + file, "r", encoding="utf8"))
            for i in jsonData:
                startword = time.clock()
                result = Trie.GetNearestMatchFromTrie(i)
                timing.append((time.clock() - startword, i))
                if not result[0]:
                    bad_values.append(i)

            print ("=", sep="", end="")
        if (bad_values == []):
            verify = time.clock() - start
            json.dump(Trie.IndexTrie, open(picklefile, "wb"))
            json.dump(Trie.FinalMapDict, open(hashfile, "wb"))
            print ("\nVerified in ", verify, "secs and good to go. (created pickle)")

        else:
            print ("Bad values detected")
            print (bad_values)
        timing.sort(reverse = True)
        sum = 0.0
        for item in timing:
            sum += item[0]
        avg = sum / len(timing)
        print("Worst lookup: ", timing[0][1], " ", timing[0][0], " secs")
        print("Best lookup: ", timing[-1][1], " ", timing[-1][0], " secs")
        print("Avg lookup: ", avg, " secs")

def conflatedDocids(result,rankingType): # Ranking based on TF-IDF
    if (len(result) == 1):
            return [(i[0], docdict[i[0]][2], int(i[2])) for i in result[0][1]]
    interset = 0
    docidtfsum = {}
    for item in result:
        for i in item[1]:
            if i[0] not in docidtfsum:
                docidtfsum[i[0]] = 0
            docidtfsum[i[0]] += int(i[2])

    if(rankingType == 'tf-idf'):
        starting = True
        for item in result:
            setlist = []
            for i in item[1]:
                setlist.append(i[0])
            if starting:
                starting = False
                interset = sets.Set(setlist)
            else:
                #interset = interset.intersection(sets.Set(setlist))
                interset = interset.union(sets.Set(setlist))
        return [(i, docdict[i][2], docidtfsum[i]) for i in list(interset)]
    elif(rankingType == 'cosine'):
        return cosineSimilarDocs(result, {})
    elif(rankingType == 'cosine-pg-tf-idf'):
        return cosineSimilarDocs(result, docidtfsum)
    elif(rankingType == 'cosine-position-pg-tf-idf'):
        return cosineSimilarDocs(result, docidtfsum, len(result[0][1][0]) == 4)

def cosineSimilarDocs(indexPostingList, docidtfsum, usePositions = False):
    global snippetDict
    queryVector = {}
    docVectors = {}
    docTermPosMap = {} 
    queryTermTfDict = {}
        
    docTermPos = {}
    shouldCheck = True and usePositions
    docLeastDiff = {}
    termList = []
    for term,posting,position in indexPostingList:
        if(term in queryTermTfDict):
            queryTermTfDict[term][0] += 1
            continue
        else:
            queryTermTfDict[term] = [1,1] #[TF,DF] #DF initialized to 1 to denote query as a doc #TF counts no.of times term occurs within query
        for doc in posting:
            if shouldCheck:
                if doc[0] not in docTermPos:
                    docTermPos[doc[0]] = []
                    docTermPosMap[doc[0]] = {}
                docTermPos[doc[0]] += [(i, position) for i in doc[3]]
                docTermPosMap[doc[0]][term] = doc[3]
            queryTermTfDict[term][1] += 1
            if(doc[0] in docVectors):
                docVectors[doc[0]][term] = doc[2]
            else:
                docVectors[doc[0]] = {term: doc[2]}
        termList.append(term)
    snippetDict[Set(termList)] = docTermPosMap

    if shouldCheck:
        for doc in docTermPos:
            docLeastDiff[doc] = 0
            docTermPos[doc].sort(key = lambda x: x[0])
            prevTPos = docTermPos[doc][0]
            for i in xrange(1, len(docTermPos[doc])):
                if abs(docTermPos[doc][i][1] - prevTPos[1]) == 1:
                    diff = docTermPos[doc][i][0] - prevTPos[0]
                    if docLeastDiff[doc] == 0 or diff < docLeastDiff[doc]:
                        docLeastDiff[doc] = diff
                prevTPos = docTermPos[doc][i]
        bigDiff = 0
        for doc in docLeastDiff:
            if docLeastDiff[doc] > bigDiff:
                bigDiff = docLeastDiff[doc]

        for doc in docLeastDiff:
            if docLeastDiff[doc] == 0:
                docLeastDiff[doc] = bigDiff +1
    else:
        for doc in docVectors:
            docLeastDiff[doc] = 1


    for term in queryTermTfDict:
        queryVector[term] = round((1+math.log(queryTermTfDict[term][0],10)) * math.log(len(docdict)/queryTermTfDict[term][1],10),1)

    # Sample vectors
    # queryVector = {'sivabalan': 4.0, 'rohan': 3.7}
    # docVectors = {u'20689': {'rohan': 4.1}, u'41463': {'rohan': 5.4}, u'23940': {'rohan': 4.1}, , u'41456': {'rohan': 5.4}, u'41460': {'sivabalan': 5.9, 'rohan': 5.4}, 
    # u'41475': {'sivabalan': 5.9, 'rohan': 5.4}, u'41449': {'rohan': 5.4}, u'41464': {'sivabalan': 5.9, 'rohan': 5.4}, u'20464': {'sivabalan': 4.5, 'rohan': 5.4}}

    if docidtfsum == {}:
        return [(i, docdict[i][2], docLeastDiff[i], calculateCosineSimilarity(queryVector, docVectors[i])) for i in docVectors if len(docVectors[i]) == len(queryVector)]
    return [(i, docdict[i][2], docidtfsum[i], docLeastDiff[i], calculateCosineSimilarity(queryVector, docVectors[i])) for i in docVectors if len(docVectors[i]) == len(queryVector)]

def calculateCosineSimilarity(vector1, vector2):
    dotProduct = 0
    euclideanDistProduct = [0,0]
    for dimension in vector1:
        euclideanDistProduct[0] += vector1[dimension] ** 2
        if(dimension in vector2):
            dotProduct += vector1[dimension] * vector2[dimension]
            euclideanDistProduct[1] += vector2[dimension] ** 2
    euclideanDist = (euclideanDistProduct[0] * euclideanDistProduct[1]) ** 0.5
    
    return round(dotProduct/euclideanDist,2)

def normalize(result):
    mean = [0]*(len(result[0])-1)
    sd = [0]*(len(result[0])-1)
    for i in range(1,len(result[0])):
        mean[i-1] = sum([j[i] for j in result])/len(result)
        sd[i-1] = math.sqrt(sum([(j[i]-mean[i-1])*(j[i]-mean[i-1]) for j in result])/len(result))
    for i in range(len(result)):
        newtup = [result[i][0]]
        for j in range(1, len(result[i])):
            if sd[j-1] != 0:
                newtup.append(((result[i][j] - mean[j-1])/sd[j-1]) + 100)
            else:
                newtup.append(1)
        result[i] = tuple(newtup)
    return result


#tf-idf
def sort2level(x):
    return x[2]
#cosine, cosine and position
def sort4level(x):
    return x[1]*x[2]
def sort5level(x):
    file = open(formulafile, "r")
    list_of_lines = file.readlines()
    file.close()
    for line in list_of_lines:
        line = line.strip()
        if line != "" and line[0]!='#':
            try:
                num = eval(line)
                return num
            except ValueError:
                print(x)

sortChooser = {3: sort2level, 4: sort4level, 5:sort5level}
def rankResults(result):
    if len(result) > 0:
        return sorted(result, key = sortChooser[len(result[0])], reverse = True)
    else:
        return result
    #return sorted(sorted(result, key = lambda x:x[1], reverse = True), key = lambda x:x[2], reverse = True)
    #return result

def docidLoader():
    global docdict
    if os.access(docidjson, os.F_OK):
        docdict = json.load(open(docidjson, "rb"))
        return
    pagerankreader = open(pagerankfile, "r")
    pgrank = {}
    for pg in pagerankreader:
        pgparts = pg.split()
        pgrank[pgparts[0]] = float(pgparts[1])
    for line in open(docidfile, "r"):
        parts = line.split("\t")
        p = 0.0
        if parts[0] in pgrank:
            p = pgrank[parts[0]]
        docdict[parts[0]] = (parts[1], parts[2], p)
    json.dump(docdict, open(docidjson, "wb"))
    print(len(docdict))

def ndcgLoader():
    global ndcgDict
    if os.access(oraclefile, os.F_OK):
        ndcgDict = json.load(open(oraclefile, "rb"))
        return
    return False

def getResultsWithNDCG(result,qText): # Assumption: qText is present in NDCG Dict
    dcgValue = -1
    idealDCGValue = 0
    
    for i in range(MAX_NUM_RESULTS):
        relevance = 0
        rank = i+1
        if(result["results"][i]["url"] in ndcgDict[qText]):
            relevance = math.ceil((MAX_NUM_RESULTS - ndcgDict[qText].index(result["results"][i]["url"]))/RELEVANCE_SPREAD) 
        if rank == 1:
            dcgValue = relevance
        else:
            dcgValue += relevance/math.log(rank,2)
        idealDCGValue += math.ceil((MAX_NUM_RESULTS - i)/RELEVANCE_SPREAD)
        result["ndcg_values"].append(round(dcgValue/idealDCGValue,2))
    
    return result


def resultsList(result):
    urls = {"results":[],"ndcg_values":[]}
    count = 0
    for item in result:
        if item[0] in docdict and "http://vcp.ics.uci.edu" not in docdict[item[0]][0]:
            d = {}
            d["docid"] = item[0]
            d["title"] = ""
            d["url"] = docdict[item[0]][0]
            d["snippet"] = ""
            d["score"] = item[2]
            d["pagerank"] = item[1]
            d["sortscore"] = list(item)
            urls["results"].append(d)
            count +=1
        if count == MAX_NUM_RESULTS: # Limit number of results to return
            break
    return urls

def addPageSnippets(queryTermSet,urlObjects) {
    ## 
    for urlObj in urlObjects:
        tempHtml = open(htmlPath + docdict[urlObj[docid]][2]).read()
        
}


def GetResult(query,rankingType):
    start = time.clock()
    query = query.strip().lower()
    tokens = nltk.word_tokenize(query)
    tokenSet = Set(tokens)
    result = []
    global snippetDict
    snippetDict[tokenSet] = {}
    for i in range(len(tokens)):
        word = wnl.lemmatize(tokens[i])
        data = Trie.GetNearestMatchFromTrie(word)
        if (data[0]):
            result.append((word, data[1][1], i))

    if result != []:
        finalresult = resultsList(rankResults(normalize(conflatedDocids(result,rankingType)))) # Ranking based on TF-IDF/Cosine similarity
        timetaken = time.clock() - start
        if(query in ndcgDict):
            finalresult = getResultsWithNDCG(finalresult,query)
        if(len(snippetDict[tokenSet]) > 0):
            finalresult = addPageSnippets(tokenSet,finalresult)
        print("Fetched in ", timetaken, " secs")
        return(finalresult)
        
    timetaken = time.clock() - start
    print("Fetched in ", timetaken, " secs")
    print("No results")

def GetASResult(query):
    start = time.clock()
    query = query.strip().lower()
    tokens = nltk.word_tokenize(query)
    result = [""]
    for token in tokens:
        token = token.lower()
        if token not in stops:
            data = Trie.GetNearestMatchFromTrie(wnl.lemmatize(token))
            if not data[0]:
                 possiblewords = sorted(Trie.GetListofWords(data[4], 0, 3), key = lambda x: len(x[0]))[:5]
                 newresult = []
                 for item in result:
                     for word in possiblewords:
                         newresult.append(item + " " + word[0])
                 result = newresult[:]
            else:
                for i in range(len(result)):
                    result[i] += " " + token
        else:
            for i in range(len(result)):
                result[i] += " " + token
    for i in range(len(result)):
        result[i] = result[i].lstrip()

    timetaken = time.clock() - start
    print("Fetched in ", timetaken, " secs")
    return result[:5]