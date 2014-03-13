dotfile = open("../FinalSet/pageRankLayout.dot", "r")
incdict = {}
outdict = {}
pgrank = {}
for line in dotfile.readlines()[1:-1]:
    parts = line.split("->")
    inc = parts[0].strip()
    out = parts[1].strip().strip(";")
    #print(inc, out)
    if inc not in incdict:
        incdict[inc] = []
    if inc not in outdict:
        outdict[inc] = []
    if out not in outdict:
        outdict[out] = []
    if out not in incdict:
        incdict[out] = []
    if out not in pgrank:
        pgrank[out] = 1.0
    if inc not in pgrank:
        pgrank[inc] = 1.0
    incdict[out].append(inc)
    outdict[inc].append(out)
dotfile.close()
N = len(outdict)
count = 0
while True:
    maxdiff = 0.0
    count += 1
    for node in pgrank:
        oldvalue = pgrank[node]
        pgrank[node] = (0.15/N)+(0.85 * sum([pgrank[i]/len(outdict[i]) for i in incdict[node]]))
        diff = oldvalue - pgrank[node]
        if maxdiff < diff:
            maxdiff = diff
    print (count, maxdiff)
    if maxdiff < 0.0001:
        break
pglist = sorted([(node, pgrank[node]) for node in pgrank], key = lambda x: x[1], reverse = True)
outfile = open("pagerank.tsv", "w")
for item in pglist:
    outfile.write(str(item[0]) + "\t" + str(item[1]) + "\n")
outfile.close()


 
