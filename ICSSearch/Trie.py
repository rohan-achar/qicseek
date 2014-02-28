import copy
IndexTrie = {} #! -> closest matching node, #->possiblematch, $->node of the document

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

def GetNearestMatchFromTrie(key):
    key = key + "$"
    i = 0
    j = 0
    possiblematch = ""
    dict = IndexTrie
    list_indices = []
    while True:
        if i == len(possiblematch):
            i = 0
            if key[j] in dict:
                if key[j] == "$":
                    return True, dict["$"]
                list_indices.append(key[j])
                dict = getFromTrie(list_indices)
                if (dict == False):
                    return False,
                possiblematch = dict["#"]
            else:
                return False, key[j:-1], i, j, list_indices, possiblematch, True
        elif possiblematch[i] == key[j]:
            i += 1
            j += 1
        else:
            return False, key[j:-1], i, j, list_indices, possiblematch, False

        #d["cat"] : {A} -> d["c"] : {"at" : {A}},{"ot": {B}}
def AddKeyToTrie(key, value):
    
    key = key + "$"
    if (IndexTrie == {}):
        IndexTrie[key[0]] = {}
        IndexTrie[key[0]]["#"] = key[:-1]
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
                node["#"] = key[j:-1]
                node["$"] = value
                addToTrie(match[4], key[j], node)
            else:
                addToTrie(match[4], "$", value)
        else:
            oldnode[possiblematch[i]] = copy.deepcopy(dict)
            oldnode[possiblematch[i]]["#"] = possiblematch[i:]
            oldnode["#"] = possiblematch[:i]
            if j==len(key) -1:
                oldnode["$"] = value
            else:
                node = {}
                node["#"] = key[j:-1]
                node["$"] = value
                oldnode[key[j]] = node
            addToTrie(match[4][:-1], possiblematch[0], oldnode)

def GetWholeWord(list_indices):
    if (len(list_indices) == 0):
        return u""
    return GetWholeWord(list_indices[:-1]) + getFromTrie(list_indices)["#"]

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