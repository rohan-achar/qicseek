import os
src = "../FinalSet/"

docidfile = open(src + "DocId.tsv", "r")
docidmap = {}
for line in docidfile.readlines():
    parts = line.split()
    if ".ics.uci.edu/" in parts[1] and "calendar.ics.uci.edu" not in parts[1] and "archive.ics.uci.edu" not in parts[1] and "http://drzaius.ics.uci.edu/cgi-bin/cvsweb.cgi/" not in parts[1] and "http://flamingo.ics.uci.edu/releases/" not in parts[1] and "http://fano.ics.uci.edu/ca/" not in parts[1] and "http://ironwood.ics.uci.edu/" not in parts[1] and "https://duttgroup.ics.uci.edu/" not in parts[1] and "http://djp3-pc2.ics.uci.edu/LUCICodeRepository/" not in parts[1] and "http://luci.ics.uci.edu/blog/" not in parts[1]:
        docidmap[parts[2]] = parts[1]

def fileremove(filename):
    if os.access(src + "Html/" + filename, os.F_OK) and os.access(src + "Fq1/" + filename + ".fq1", os.F_OK) and os.access(src + "Text/" + filename + ".txt", os.F_OK) and os.access(src + "Pfq/" + filename + ".pfq", os.F_OK) and os.access(src + "Fq2/" + filename + ".fq2", os.F_OK):
        os.remove(src + "Html/" + filename) 
        os.remove(src + "Fq1/" + filename + ".fq1")
        os.remove(src + "Fq2/" + filename + ".fq2")
        os.remove(src + "Pfq/" + filename + ".pfq")
        os.remove(src + "Text/" + filename + ".txt")
    else:
        print(file)
for file in os.listdir(src + "Html/"):
    if file not in docidmap:
        fileremove(file)

count = 0
newfile = open(src + "NewDocId.tsv", "w")
for file in docidmap:
    newfile.write(str(count) + "\t" + docidmap[file] + "\t" + file + "\n")
    count += 1
newfile.close()
