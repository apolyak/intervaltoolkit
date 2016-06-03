# interval toolkit
import sys
import csv
import intervaltoolkit
'''
def getOverlap(start1,end1,start2,end2): #returns reciprocol overlap if overlap, else returns 0
	recip = 0
	bp_start=0
	bp_end=0
	if int(start1) >= int(start2) and int(end1) >= int(end2):
		recip = int(end2)-int(start1)
		bp_start = int(start1)
		bp_end= recip+int(start1)
	if int(start1) <= int(start2) and int(end1) <= int(end2):
		recip = int(end1)-int(start2)
		bp_start=int(start2)
		bp_end=recip + int(start2)
	if int(start1) <= int(start2) and int(end1) >= int(end2):
		recip = int(end2)-int(start2)
		bp_start=int(start2)
		bp_end=int(start2)+recip
	if int(start1) >= int(start2) and int(end1) <= int(end2):
		recip = int(end1)-int(start1)
		bp_start = int(start1)
		bp_end = recip+int(start1)
	return [bp_start,bp_end]

with open("testsheet.txt","r") as infiledata:
	infilereader=csv.reader(infiledata,delimiter=" ")
	for i in infilereader:
		print i
		chromosome1 = i[0]
		start1 = i[1]
		end1 = i[2]
		start2 = i[3]
		end2 = i[4]

		print getOverlap(start1,end1,start2,end2)
'''
infile = sys.argv[1]
refgenefile = sys.argv[2]
#outfile = sys.argv[3]

infilereader = csv.reader(open(infile),delimiter="\t")
#refgenereader = read.csv(open(refgenefile),delimiter="\t")
outarray = []
for row in infilereader:
	#print "RUN:", intervaltoolkit.getGenesFromInterval(row[0],row[1],row[2],refgenefile)
	outarray.extend(intervaltoolkit.getGenesFromInterval(row[0],row[1],row[2],refgenefile))
#print "-------------------"
#print outarray

for i in outarray:
	print i
'''
for i in range(0,len(outarray)):
	print outarray[1]
'''
#print "DONE!"
