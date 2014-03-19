import io
infile = io.open("../FinalSet/DocIdNew.tsv","r", encoding="utf-8")
ofile = io.open("../FinalSet/listDocid.tsv","w", encoding="utf-8")
for line in infile:
	ofile.write(unicode(str([line]) + "\n"))
infile.close()
ofile.close()