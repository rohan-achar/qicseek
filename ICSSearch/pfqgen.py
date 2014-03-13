import os
from io import open
from threading import *
import nltk
import string
import re, json, copy
from sets import Set
src = "../FinalSet/Html/"
dst = "../FinalSet/Pfq/"
files = os.listdir(src)
stops = {}
stopslist = "a a's	able	about	above	according accordingly	across	actually	after	afterwards again	against	ain't	all	allow allows	almost	alone	along	already also	although	always	am	among amongst	an	and	another	any anybody	anyhow	anyone	anything	anyway anyways	anywhere	apart	appear	appreciate appropriate	are	aren't	around	as aside	ask	asking	associated	at available	away	awfully	be	became because	become	becomes	becoming	been before	beforehand	behind	being	believe below	beside	besides	best	better between	beyond	both	brief	but by	c'mon	c's	came	can can't	cannot	cant	cause	causes certain	certainly	changes	clearly	co com	come	comes	concerning	consequently consider	considering	contain	containing	contains corresponding	could	couldn't	course	currently definitely	described	despite	did	didn't different	do	does	doesn't	doing don't	done	down	downwards	during each	edu	eg	eight	either else	elsewhere	enough	entirely	especially et	etc	even	ever	every everybody	everyone	everything	everywhere	ex exactly	example	except	far	few fifth	first	five	followed	following follows	for	former	formerly	forth four	from	further	furthermore	get gets	getting	given	gives	go goes	going	gone	got	gotten greetings	had	hadn't	happens	hardly has	hasn't	have	haven't	having he	he's	hello	help	hence her	here	here's	hereafter	hereby herein	hereupon	hers	herself	hi him	himself	his	hither	hopefully how	howbeit	however	i'd	i'll i'm	i've	ie	if	ignored immediate	in	inasmuch	inc	indeed indicate	indicated	indicates	inner	insofar instead	into	inward	is	isn't it	it'd	it'll	it's	its itself	just	keep	keeps	kept know	known	knows	last	lately later	latter	latterly	least	less lest	let	let's	like	liked likely	little	look	looking	looks ltd	mainly	many	may	maybe me	mean	meanwhile	merely	might more	moreover	most	mostly	much must	my	myself	name	namely nd	near	nearly	necessary	need needs	neither	never	nevertheless	new next	nine	no	nobody	non none	noone	nor	normally	not nothing	novel	now	nowhere	obviously of	off	often	oh	ok okay	old	on	once	one ones	only	onto	or	other others	otherwise	ought	our	ours ourselves	out	outside	over	overall own	particular	particularly	per	perhaps placed	please	plus	possible	presumably probably	provides	que	quite	qv rather	rd	re	really	reasonably regarding	regardless	regards	relatively	respectively right	said	same	saw	say saying	says	second	secondly	see seeing	seem	seemed	seeming	seems seen	self	selves	sensible	sent serious	seriously	seven	several	shall she	should	shouldn't	since	six so	some	somebody	somehow	someone something	sometime	sometimes	somewhat	somewhere soon	sorry	specified	specify	specifying still	sub	such	sup	sure t's	take	taken	tell	tends th	than	thank	thanks	thanx that	that's	thats	the	their theirs	them	themselves	then	thence there	there's	thereafter	thereby	therefore therein	theres	thereupon	these	they they'd	they'll	they're	they've	think third	this	thorough	thoroughly	those though	three	through	throughout	thru thus	to	together	too	took toward	towards	tried	tries	truly try	trying	twice	two	un under	unfortunately	unless	unlikely	until unto	up	upon	us	use used	useful	uses	using	usually value	various	very	via	viz vs	want	wants	was	wasn't way	we	we'd	we'll	we're we've	welcome	well	went	were weren't	what	what's	whatever	when whence	whenever	where	where's	whereafter whereas	whereby	wherein	whereupon	wherever whether	which	while	whither	who who's	whoever	whole	whom	whose why	will	willing	wish	with within	without	won't	wonder	would wouldn't	yes	yet	you	you'd you'll	you're	you've	your	yours yourself	yourselves	zero next prev previous".split()
for item in stopslist:
    stops[item.strip()] = 1
wnl = nltk.WordNetLemmatizer()
        
docidextras = json.load(open("../FinalSet/docidtitle.json", "r"))
didextrascomplete = copy.deepcopy(docidextras)
print("loaded from file")
mn = 1
for docid in docidextras:
    if (mn % 1000 == 0):
        print (mn)
    mn += 1
    for types in docidextras[docid]:
        stringlists = Set()
        for strings in docidextras[docid][types]:
            tokens = nltk.word_tokenize(strings)
            newtokens = []
            emailFlag = False
            for i in range(len(tokens)):
                tokens[i] = wnl.lemmatize(tokens[i])
                if emailFlag:
                    emailFlag = False
                    continue
                if re.match(".*[\d+|\W+].*", tokens[i]) == None and tokens[i].lower() not in stops and len(tokens[i]) > 1:
                    newtokens.append(tokens[i].lower())
                elif tokens[i] == "@" and i > 0 and i < len(tokens) - 1 and "." in tokens[i + 1]:
                    newword = tokens[i-1] + tokens[i] + tokens[i+1]
                    emailFlag = True
                    newtokens.append(newword.lower())
            stringlists.union_update(Set(newtokens))
        docidextras[docid][types] = stringlists

print("loading from file and creating sets done")

weightvalue = {"title": 1024, "a":512, "h1":256, "h2":128, "h3":64, "h4":32, "h5":16, "h6":8, "b":4, "i":2}




fileToDocId = {}
for line in open("../FinalSet/DocId.tsv", "r"):
    docid, url, file = line.split()
    fileToDocId[file] = docid

def  sumTypes(docid, word):
    sum = 0
    for types in docidextras[docid]:
        if word.lower() in docidextras[docid][types]:
            sum += weightvalue[types]
    return sum

def getExtraLines(docid):
    if "a" in didextrascomplete[docid]:
        return " " + " ".join(didextrascomplete[docid]["a"])
    return ""

def pfqGen(filenames, id):
    count = 1
    for filename in filenames:
        if (count%100 == 0):
            print("Thread: ", id, " count: ", count)
        count += 1
        if os.access(dst + filename + ".pfq", os.F_OK):
            continue
        file = open(src + filename, "r", encoding="utf8")
        string = nltk.util.clean_html(file.read()) + getExtraLines(fileToDocId[filename])
        tokens = nltk.word_tokenize(string)
        words = {}
        emailFlag = False
        for i in range(len(tokens)):
            tokens[i] = wnl.lemmatize(tokens[i])
            if emailFlag:
                emailFlag = False
                continue
            if re.match(".*[\d+|\W+].*", tokens[i]) == None and tokens[i].lower() not in stops and len(tokens[i]) > 1:
                if tokens[i].lower() not in words:
                    words[tokens[i].lower()] = []
                words[tokens[i].lower()].append(i)
            elif tokens[i] == "@" and i > 0 and i < len(tokens) - 1 and "." in tokens[i + 1]:
                newword = tokens[i-1] + tokens[i] + tokens[i+1]
                emailFlag = True
                if newword.lower() not in words:
                    words[newword.lower()] = []
                words[newword.lower()].append(i)
        outfile = open(dst + filename + ".pfq", "w", encoding = "utf8")
        dict_list = []
        for word in words:
            dict_list.append((word, len(words[word]), sumTypes(fileToDocId[filename], word)))
        dict_list.sort(key = lambda x: x[1], reverse = True)
        writestr = ""
        for item in dict_list:
            writestr += item[0] + ",\t" + str(item[1]) + ",\t" + str(item[2]) + "\n"
            
        outfile.write(unicode(writestr))
        outfile.close()

for i in range(64):
    Thread(target = pfqGen, args=(files[i::64], i)).start() 
