import os
import math
from io import open
src = "../FinalSet/pageRankLayout.dot"
graph = open(src, "r")
edges = graph.readlines()[1:-1]
outdict = {}
indict = {}
pgrank = {}
dict = {}
for edge in edges:
    parts = edge.split("->")
    fnode = parts[0].strip()
    tnode = parts[1].rstrip(";\n")
    if (fnode not in dict):
        dict[fnode] = 1
    if (tnode not in dict):
        dict[tnode] = 1

    if fnode not in outdict:
        outdict[fnode] = []
    if fnode not in indict:
        indict[fnode] = []
    outdict[fnode].append(tnode)
    if tnode not in indict:
        indict[tnode] = []
    if tnode not in outdict:
        outdict[tnode] = []
    indict[tnode].append(fnode)

d = 0.85
m = 0.001

i = 0

while True:
    maxm = 0
    for node in indict:
        if i == 0:
            pgrank[node] = 1
            continue
        oldvalue = pgrank[node]
        pgrank[node] = ((1-0.85)/46911) - (0.85*(sum([pgrank[j]/len(outdict[j]) for j in indict[node]])))
        diff = oldvalue - pgrank[node] 
        if diff > maxm:
            maxm = diff
    i += 1
    if i == 1:
        continue
    print(maxm)
    if maxm < m:
        break

outfile = open("../FinalSet/pagerank.tsv", "w", encoding = "utf8")
print(i)
for item in pgrank:
    outfile.write(item + "\t" + str(pgrank[item]) + "\n")