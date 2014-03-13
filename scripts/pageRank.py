from graph_tool.all import *

g = load_graph("../FinalSet/pageRankLayout.dot")
pr = graph_tool.centrality.pagerank(g)
result = []
for item in g.vertices():
	 result.append((item, pr[item]))
result.sort(key = lambda x: x[1], reverse = True)
outfile = open("../FinalSet/pagerank.tsv", "w")
for item in result:
	outfile.write(str(item[0]) + "\t" + str(item[1]) + "\n")
outfile.close()
