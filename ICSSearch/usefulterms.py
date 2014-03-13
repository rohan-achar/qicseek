import json
from pylab import *
import string, os
count = 1
plot_list = []
tflist = []
for file in os.listdir("../FinalSet/Index/"):
    data = json.load(open("../FinalSet/Index/" + file, "r"))
    for word in data:
        #if data[word][0] > 2000:
        #    continue
        s = sum([i[1] for i in data[word][1]])
        
        plot_list.append((word, s/len(data[word][1]), data[word][0]))
        if (count%1000 == 0):
            print(count)
        count+= 1

plot_list.sort(key = lambda x: x[2])
print("copying")
totaltfidf = sum([plot_list[i][1] for i in range(len(plot_list))])
totaltf = sum([plot_list[i][2] for i in range(len(plot_list))])
newlist = [(i, (plot_list[i][1]*1000000/totaltfidf) + 10) for i in range(len(plot_list))]
newlist1 = [(i, plot_list[i][2]*1000000/totaltf) for i in range(len(plot_list))]

file = open("hightf.txt", "w")
for i in range(len(plot_list)): 
    if plot_list[i][1] <= 1 and plot_list[i][2] > 1000:
        file.write(plot_list[i][0] + ",\t" + str(plot_list[i][2]) + "\n")
file.close()
print(len(newlist))
plt.plot(*zip(*newlist))
plt.plot(*zip(*newlist1))
print(plot_list[-10:])
plt.show()