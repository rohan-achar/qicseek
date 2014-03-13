import copy
IndexTrie = {} #! -> closest matching node, #->possiblematch, $->node of the document
IncDict = {}
FinalMapDict = {}
IncCountMap = {}
IncCount = 1
free_num = []

def GetValue(key):
    global IncCount
    v = 0
    if key in IncDict:
        IncCountMap[IncDict[key]] += 1
        return IncDict[key]
    if (free_num != []):
        v = free_num.pop()
    else:
        v = IncCount
        IncCount += 1
    IncDict[key] = v
    FinalMapDict[v] = key
    if v not in IncCountMap:
        IncCountMap[v] = 0
    IncCountMap[v] += 1
    return v

def RemoveKey(value):
    if value in FinalMapDict:
        key = FinalMapDict[value]
        IncCountMap[value] -= 1
        if IncCountMap[value] == 0:
            free_num.append(value)
            del IncDict[key]
            del FinalMapDict[value]
    elif value not in FinalMapDict:
        print("Waaaaait")
            

def getFromTrie(list_indices):
    try:
        evalstring = "IndexTrie"
        for item in list_indices:
            evalstring += "[\'" + item + "\']"
        return eval(evalstring)
    except KeyError:
        print(evalstring, list_indices)
        return False

def addToTrie(list_indices, key, object):
    evalstring = "IndexTrie"
    for item in list_indices:
        evalstring += "[\'" + item + "\']"
    temp = eval(evalstring)
    temp[key] = object

#def GetNearestMatchFromTrie(key):
#    if key in IndexTrie:
#        return (True, IndexTrie[key])
#    else:
#        return (False, "")
def GetNearestMatchFromTrie(key):
    key = key + "$"
    i = 0
    j = 0
    possiblematch = ""
    localDict = IndexTrie
    list_indices = []
    while True:
        if i == len(possiblematch):
            i = 0
            if key[j] in localDict:
                if key[j] == "$":
                    return True, localDict["$"]
                list_indices.append(key[j])
                localDict = getFromTrie(list_indices)
                if (localDict == False):
                    return False,
                possiblematch = key[j] + FinalMapDict[localDict["#"]]
            else:
                return False, key[j:-1], i, j, list_indices, possiblematch, True
        elif possiblematch[i] == key[j]:
            i += 1
            j += 1
        else:
            return False, key[j:-1], i, j, list_indices, possiblematch, False

        #d["cat"] : {A} -> d["c"] : {"at" : {A}},{"ot": {B}}

#def AddKeyToTrie(key, value):
#    IndexTrie[key] = value
def AddKeyToTrie(key, value):
    
    key = key + "$"
    if (IndexTrie == {}):
        IndexTrie[key[0]] = {}
        IndexTrie[key[0]]["#"] = GetValue(key[1:-1])
        IndexTrie[key[0]]["$"] = value
        return
    match = GetNearestMatchFromTrie(key[:-1])
    if match[0]:
        print ("Rehashed value: " + key)
        print (value, match[1])
    else:
        #possiblematch = cat
        #key = cot
        # i = 1
        # j = 1
        oldnode = {}
        dict = getFromTrie(match[4])
        i = match[2]
        j = match[3]
        possiblematch = match[5]
        if (match[6]):
            if (j<len(key)-1):
                node = {}
                node["#"] = GetValue(key[j+1:-1])
                node["$"] = value
                addToTrie(match[4], key[j], node)
            else:
                addToTrie(match[4], "$", value)
        else:
            RemoveKey(dict["#"])
            oldnode[possiblematch[i]] = copy.deepcopy(dict)
            oldnode[possiblematch[i]]["#"] = GetValue(possiblematch[i+1:])
            oldnode["#"] = GetValue(possiblematch[1:i])
            if j==len(key) -1:
                oldnode["$"] = value
            else:
                node = {}
                node["#"] = GetValue(key[j+1:-1])
                node["$"] = value
                oldnode[key[j]] = node
            addToTrie(match[4][:-1], possiblematch[0], oldnode)

def GetWholeWord(list_indices):
    if (len(list_indices) == 0):
        return u""
    return GetWholeWord(list_indices[:-1]) + list_indices[-1] + FinalMapDict[getFromTrie(list_indices)["#"]]

def GetListofWords(list_indices, depth, max_depth):
    # get nearest till depth is max_depth
    newlist = list_indices[:]
    dict = getFromTrie(list_indices)
    result = []
    if ("$" in dict):
        result.append((GetWholeWord(list_indices), depth))
    if (depth == max_depth):
        return result
    for index in dict:
        if index != "#" and index != "$":
            result.extend(GetListofWords(list_indices + [index], depth + 1, max_depth))
    return result

#compressabilty = {}
#def Duplicates(dict):
#    if "#" in dict:
#        if dict["#"] not in compressabilty:
#            compressabilty[dict["#"]] = 0
#        compressabilty[dict["#"]] += 1
#    for item in dict:
#        if item != "$" and item != "#":
#            Duplicates(dict[item])


#def Statistics():
#    result = []
#    total = 0
#    totalwc = 0
#    excess = 0
#    excesswc = 0
#    manyletterexcess = 0
#    manyletterwc = 0
#    for item in compressabilty:
#        if compressabilty[item] > 1:
#            excess += compressabilty[item] - 1
#            excesswc += compressabilty[item] * len(item)
#            if len(item) > 2:
#                manyletterexcess += compressabilty[item] - 1
#                manyletterwc += compressabilty[item] * len(item)
#        total += compressabilty[item]
#        totalwc += compressabilty[item] * len(item)
#    print("totalwc: ", totalwc)
#    print("excesswc: ", excesswc)
#    print("manyletterexcesswc: ", manyletterwc)
#    print("total: ", total)
#    print("excess: ", excess)
#    print("manyletterexcess: ", manyletterexcess)
#    print("dictlength: ", len(compressabilty))