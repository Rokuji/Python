import re
import math
import statistics
import numpy



def calculateMean():
	lis=[]
	with open ('friendcount.txt ','r') as nc:
		total = sum(int(x)
		for line in nc
		for x in line.split())
	mean = total /99 
	print ("Mean = ",mean)
	return mean



def calculateMedian():
	ls=[]
	with open ('friendcount.txt ','r') as n:
		for line in n:
			ls.append(line.strip('\n'+''))
		ls =list(map(int, ls))
		median = statistics.median(ls)
		print ("Median = ",median)

calculateMean()
calculateMedian()