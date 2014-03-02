from __future__ import print_function
import os
from threading import *
import json
import copy
from io import open
import time
import nltk
import sets
from cPickle import *
import gc

import Trie

src = "FinalSet/"
list_of_bad_files = []
picklefile = src + "IndexPickle.lime"
docidfile = src + "DocId.tsv"
pagerankfile = src + "pagerank.tsv"
docdict = {}
stops = {}
stopslist = "a a's	able	about	above	according accordingly	across	actually	after	afterwards again	against	ain't	all	allow allows	almost	alone	along	already also	although	always	am	among amongst	an	and	another	any anybody	anyhow	anyone	anything	anyway anyways	anywhere	apart	appear	appreciate appropriate	are	aren't	around	as aside	ask	asking	associated	at available	away	awfully	be	became because	become	becomes	becoming	been before	beforehand	behind	being	believe below	beside	besides	best	better between	beyond	both	brief	but by	c'mon	c's	came	can can't	cannot	cant	cause	causes certain	certainly	changes	clearly	co com	come	comes	concerning	consequently consider	considering	contain	containing	contains corresponding	could	couldn't	course	currently definitely	described	despite	did	didn't different	do	does	doesn't	doing don't	done	down	downwards	during each	edu	eg	eight	either else	elsewhere	enough	entirely	especially et	etc	even	ever	every everybody	everyone	everything	everywhere	ex exactly	example	except	far	few fifth	first	five	followed	following follows	for	former	formerly	forth four	from	further	furthermore	get gets	getting	given	gives	go goes	going	gone	got	gotten greetings	had	hadn't	happens	hardly has	hasn't	have	haven't	having he	he's	hello	help	hence her	here	here's	hereafter	hereby herein	hereupon	hers	herself	hi him	himself	his	hither	hopefully how	howbeit	however	i'd	i'll i'm	i've	ie	if	ignored immediate	in	inasmuch	inc	indeed indicate	indicated	indicates	inner	insofar instead	into	inward	is	isn't it	it'd	it'll	it's	its itself	just	keep	keeps	kept know	known	knows	last	lately later	latter	latterly	least	less lest	let	let's	like	liked likely	little	look	looking	looks ltd	mainly	many	may	maybe me	mean	meanwhile	merely	might more	moreover	most	mostly	much must	my	myself	name	namely nd	near	nearly	necessary	need needs	neither	never	nevertheless	new next	nine	no	nobody	non none	noone	nor	normally	not nothing	novel	now	nowhere	obviously of	off	often	oh	ok okay	old	on	once	one ones	only	onto	or	other others	otherwise	ought	our	ours ourselves	out	outside	over	overall own	particular	particularly	per	perhaps placed	please	plus	possible	presumably probably	provides	que	quite	qv rather	rd	re	really	reasonably regarding	regardless	regards	relatively	respectively right	said	same	saw	say saying	says	second	secondly	see seeing	seem	seemed	seeming	seems seen	self	selves	sensible	sent serious	seriously	seven	several	shall she	should	shouldn't	since	six so	some	somebody	somehow	someone something	sometime	sometimes	somewhat	somewhere soon	sorry	specified	specify	specifying still	sub	such	sup	sure t's	take	taken	tell	tends th	than	thank	thanks	thanx that	that's	thats	the	their theirs	them	themselves	then	thence there	there's	thereafter	thereby	therefore therein	theres	thereupon	these	they they'd	they'll	they're	they've	think third	this	thorough	thoroughly	those though	three	through	throughout	thru thus	to	together	too	took toward	towards	tried	tries	truly try	trying	twice	two	un under	unfortunately	unless	unlikely	until unto	up	upon	us	use used	useful	uses	using	usually value	various	very	via	viz vs	want	wants	was	wasn't way	we	we'd	we'll	we're we've	welcome	well	went	were weren't	what	what's	whatever	when whence	whenever	where	where's	whereafter whereas	whereby	wherein	whereupon	wherever whether	which	while	whither	who who's	whoever	whole	whom	whose why	will	willing	wish	with within	without	won't	wonder	would wouldn't	yes	yet	you	you'd you'll	you're	you've	your	yours yourself	yourselves	zero".split()

def LoadTrie():
    global src
    global picklefile
    global docidfile
    global pagerankfile
    if "FinalSet" not in os.listdir(os.curdir):
        src = "../" + src
        picklefile = "../" + picklefile
        docidfile = "../" + docidfile
        pagerankfile = "../" + pagerankfile
    for item in stopslist:
        stops[item.strip()] = 1
    
    start = time.clock()
    print ("Loading To memory")
    if os.access(picklefile, os.F_OK):
        preservedjar = open(picklefile, "rb")
        dataDump = json.load(preservedjar)
        Trie.IndexTrie = dataDump["Index"]
        for item in dataDump["Hash"]:
            Trie.FinalMapDict[int(item)] = dataDump["Hash"][item]
        del dataDump
        preservedjar.close()
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
            picklejar = open(picklefile, "wb")
            dataDump = {}
            dataDump["Index"] = Trie.IndexTrie
            dataDump["Hash"] = Trie.FinalMapDict
            json.dump(dataDump, picklejar)
            picklejar.close()
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

def conflatedDocids(result):
    if (len(result) == 1):
        return [(i[0], docdict[i[0]][2], int(i[2])) for i in result[0]]
    starting = True
    interset = 0
    docidtfsum = {}
    for item in result:
        setlist = []
        for i in item:
            setlist.append(i[0])
            if i[0] not in docidtfsum:
                docidtfsum[i[0]] = 0
            docidtfsum[i[0]] += int(i[2])
        if starting:
            starting = False
            interset = sets.Set(setlist)
        else:
            interset = interset.intersection(sets.Set(setlist))

    return [(i, docdict[i][2], docidtfsum[i]) for i in list(interset)]

def rankresult(result):
    return sorted(sorted(result, key = lambda x:x[1], reverse = True), key = lambda x: x[2], reverse = True)
    #return result

def docidLoader():
    docidreader = open(docidfile, "r")
    pagerankreader = open(pagerankfile, "r")
    pgrank = {}
    for pg in pagerankreader:
        pgparts = pg.split()
        pgrank[pgparts[0]] = float(pgparts[1])
    for line in docidreader:
        parts = line.split("\t")
        p = 0.0
        if parts[0] in pgrank:
            p = pgrank[parts[0]]
        docdict[parts[0]] = (parts[1], parts[2], p)
    docidreader.close()
    print("Collected: ", gc.collect())

def urllist(result):
    urls = {}
    count = 0
    for item in result:
        if item[0] in docdict and "http://luci.ics.uci.edu/blog/" not in docdict[item[0]][0]:
            d = {}
            d["title"] = ""
            d["url"] = docdict[item[0]][0]
            urls[item[0]] = d
            count +=1
        if count == 10:
            break
    return urls



def GetResult(query):
    start = time.clock()
    tokens = nltk.word_tokenize(query)
    result = []
    for token in tokens:
        data = Trie.GetNearestMatchFromTrie(token)
        if (data[0]):
            result.append(data[1][1])
    if result != []:
        finalresult = urllist(rankresult(conflatedDocids(result)))
        timetaken = time.clock() - start
        print("Fetched in ", timetaken, " secs")
        return(finalresult)
        
    timetaken = time.clock() - start
    print("Fetched in ", timetaken, " secs")
    print("No results")

def GetASResult(query):
    start = time.clock()
    tokens = nltk.word_tokenize(query)
    result = [""]
    for token in tokens:
        token = token.lower()
        if token not in stops:
            data = Trie.GetNearestMatchFromTrie(token)
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