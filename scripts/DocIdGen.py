import os
from threading import *
table = str.maketrans("/\\?%*:|\"<>\"","___________")
src = "d:/ir_project_2_data/bigsetFinal"
table = str.maketrans("/\\?%*:|\"<>\"","___________")

docIdFiles = "d:/ir_project_2_data/bigsetFinal"
list_of_files = ["d:/ir_project_2_data/craw_logs/log_2014-02-02_18_17_complete.txt",
                 "d:/ir_project_2_data/craw_logs/log_2014-02-02_19_46_complete.txt",
                 "d:/ir_project_2_data/craw_logs/log_2014-02-05_00_21_complete.txt",
                 "d:/ir_project_2_data/craw_logs/log_2014-02-05_02_12_complete.txt",
                 "d:/ir_project_2_data/craw_logs/log_2014-02-05_19_42_complete.txt"]

FileNameToUrlMap = {}
UrlsThatHaveOnlyFiles = []
DocIdUrls = []
for item in list_of_files:
    file = open(item, "r")
    for line in file.readlines():
        url = line.strip().split()[1]
        fileName = url.translate(table)
        FileNameToUrlMap[fileName] = url

list_of_files = os.listdir(src)

for eachFile in list_of_files:
    if not eachFile.endswith(".frq_1") and not eachFile.endswith(".frq_2") and not eachFile.endswith(".result"):
        element = eachFile.rstrip(".txt")
        if element not in FileNameToUrlMap:
            UrlsThatHaveOnlyFiles.append(element)
        else:
            DocIdUrls.append((element, FileNameToUrlMap[element]))

onlyUrlFile = open("d:/ir_project_2_data/onlyUrl.txt", "w")

for item in UrlsThatHaveOnlyFiles:
    onlyUrlFile.write(item + "\n")
onlyUrlFile.close()
docIdFile = open("d:/ir_project_2_data/DocId.tsv", "w")
for i in range(len(DocIdUrls)):
    docIdFile.write(str(i) + "\t" + DocIdUrls[i][1] + "\t" + DocIdUrls[i][0] + "\n")
docIdFile.close()



