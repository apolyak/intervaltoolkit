__author__ = 'AndrewPolyak'
__date__ = '01-07-2015'
__description__ = 'Interval toolkit'

import csv

def getOverlap(start1,end1,start2,end2): #returns reciprocol overlap if overlap, else returns 0
	recip = 0
	if int(start1) >= int(start2) and int(end1) >= int(end2):
		recip = int(end2)-int(start1)
	if int(start1) <= int(start2) and int(end1) <= int(end2):
		recip = int(end1)-int(start2)
	if int(start1) <= int(start2) and int(end1) >= int(end2):
		recip = int(end2)-int(start2)
	if int(start1) >= int(start2) and int(end1) <= int(end2):
		recip = int(end1)-int(start1)
	return recip

def getOverlapCoordinates(start1,end1,start2,end2):
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
    
def getScoreFromGene(genename,scorelist,genenamecol):
    scorelistreader = csv.reader(open(scorelist,'r'),delimiter="\t")
    for row in scorelistreader:
        if row[genenamecol] == genename:
            return row

def getSize(start,end): #returns interval size
	return int(end)-int(start)

def getGenesFromInterval(inchr,instart,inend,inrefgene): #refgene must be in UCSC format and sorted by chr and start
	output = []
	chrom = inchr
	start = instart
	end = inend
	refgenereader = csv.reader(open(inrefgene,"r"), delimiter="\t")

	for row in refgenereader:
		if row[2] == chrom and getOverlap(start,end,int(row[4]),int(row[5])) > 0:
			output.append(row[12])

	return output

def getGeneCountFromInterval(inchr,instart,inend,inrefgene):
	return length(getGenesFromInterval(inchr,instart,inend,inrefgene))