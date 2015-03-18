#! /Users/orteegaabboud/anaconda/bin/python
# Mon May 19 15:53:46 CEST 2014


###################################
### Test:the creation of a class

class Student:
	def __init__(self, name):
		self.name = name
		self.attend = 0
		self.grades = []
		print("Hi! My name is {0}".format(self.name))
		print("My grades are: {0}".format(self.grades))
		print("My attendance is: {0}".format(self.attend))

	def addGrade(self, grade):
		self.grades.append(grade)
	def attendDay(self):
		self.attend += 1
	def getAverage(self):
		return sum(self.grades / len(self.grades))
	def recall(self):
		print("Hi! My name is {0}".format(self.name))
		print("My grades are: {0}".format(self.grades))
		print("My attendance is: {0}".format(self.attend))



###################################
### MY CLASS. IMPORT DATA AND CREATE THE OBJECT
### WITH ASSOCIATED FUNCTIONS THAT WILL ALLOW TO ANALYZE
### DISTANCE DATA

class DistanceR3:
	'''Class that allows to treat and filter the distance between genes and TE
	From the third version of that table.
	'''
	def __init__(self, input_file):

		## INITIATE CLASS, CREATE SELF
		## IMPORT GFF FILE


		sf = open(input_file, 'r')
		truc = sf.readlines()
		sf.close()
		del(sf)
		print("{0} file loaded".format(input_file))

		self.header = truc[0].replace('\n', '')
		truc.remove(truc[0])
		print("Header removed")

		## RETURN values that contain the information
		## of the table on a dictionary format

		self.name = []
		self.chrom = {}
		self.size = {}
		self.strand = {}
		self.distance = {}
		self.tag = {}
		self.position = {}
		self.fastaSize = {}
		for i in truc :
			i=i.replace('\n','')
			i=i.split('\t')
			self.name.append(i[0])
			self.chrom[i[0]] = i[1]
			self.size[i[0]] = int(i[2])
			self.strand[i[0]] = i[3]
			self.distance[i[0]] = int(i[4])
			self.tag[i[0]] = i[5]
			self.position[i[0]] = i[6]
			self.fastaSize[i[0]] = int(i[7])
		print("dictionaries have been created")



	def geneInfo(self, name):
		'''Requires a gene name, will return all the information
			for that gene. It can be used to check the integrity of the data
			once loaded.
		'''
		## METHOD USED TO CHECK THE INTEGRITY OF THE DATA LOAD
		print(name, self.chrom[name], self.size[name], self.strand[name],\
			self.distance[name], self.tag[name], self.position[name], \
			self.fastaSize[name])



	def byChrom(self):
		'''Will return a LIST: self.ch#
			It will contain the names of the genes contained in each chromosome
		'''
		## RETURNS LIST OF GENE NAMES BY CHROMOSOMES
		## Also returns a list of all the chromosomes
		self.ch1, self.ch2, self.ch3, self.ch4, \
		self.ch5, self.ch6, self.ch7, self.ch8 = \
		[], [], [], [], [], [], [], []

		for k,v in self.chrom.iteritems():
			if v == "CH1":
				self.ch1.append(k)
			elif v == "CH2":
				self.ch2.append(k)
			elif v == "CH3":
				self.ch3.append(k)
			elif v == "CH4":
				self.ch4.append(k)
			elif v == "CH5":
				self.ch5.append(k)
			elif v == "CH6":
				self.ch6.append(k)
			elif v == "CH7":
				self.ch7.append(k)
			elif v == "CH8":
				self.ch8.append(k)

		self.chromList = [self.ch1, self.ch2, self.ch3, self.ch4, \
			self.ch5, self.ch6, self.ch7, self.ch8 ]



	def getFromDico(self, chromosome, dico):
		'''Give it a LIST of genes, and the name of the DICTIONARY
			It will return a shorter dictionary composed of only the KEYS contained in the LIST
		'''
		## exports a new dico that only contains info from
		## certain genes.
		truc = {}
		for i in chromosome :
			truc[i] = dico[i]
		return truc



	def filterDistance(self, dico):
		'''Give a DICTIONARY containing the list of KEYS you require
			the VALUES must be numeric.
			It will return a dictionary with the list of keys for which the value is different than 0
			I use it to remove the distances between TE and genes that are equal to zero.
		'''
		## Method to filter data and output absolute values for te distance
		## outputs a dictionary
		foo = {}
		for k, v in dico.iteritems():
			if v != 0:
				foo[k] = abs(v)
		return foo


	def limitMaxAbsoluteValue(self, dico, max_value):
		'''Give a DICTIONARY containing the list of KEYS you require the VALUES must be numeric.
			It will return a dictionary with the list of keys for which the value is LESS or EQUAL to <max_value>
		'''
		## Method to filter data and output absolute values for te distance
		## outputs a dictionary
		foo = {}
		for k, v in dico.iteritems():
			if v <= max_value:
				foo[k] = abs(v)
		return foo



	def getDistanceFiltered(self, chromosome, dico):
		'''It will filter out KEYS if the VALUES equal zero.
			It will work with a list of genes (like a chromosome list)
			It requires a LIST and a DICTIONARY with integer VALUES.
		'''
		## this method will use the methods:
		## self.getFromDico
		## self.filterDistance
		## It will output a dictionary with the filtered distances
#		print("\t"+"truc 1")
		foo = {}
		for i in chromosome :
			if dico[i] != 0 :
				foo[i] = abs(dico[i])
	#	for k, v in dico2.iteritems()


#		print("truc 2")
	#	luc = self.filterDistance(bar)
#		print("truc 3")
		return foo

############ load program and check if it works

print('\n')

##libraries:
# import pylab
# from scipy.stats import *

## Libraries to make plots
print("loading libraries to make graphics")
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp, wilcoxon, ttest_ind, mannwhitneyu, shapiro


test = DistanceR3("Mg7015_polypeptide_vs_Mg7015.Mg7015_filter_refTEs_match_for_R3nuc")
print("Test data creation, check this genes in the gff file")
test.geneInfo('MGG_16750')
test.geneInfo('MGG_15987')
test.byChrom()
#send to bin##test.chromosomeDistance('CH5')

#ch5Distance = test.getFromDico(test.ch5, test.distance)
#ch5DistanceFilter = test.filterDistance(ch5Distance)
ch5DistanceFilter = test.getDistanceFiltered(test.ch5, test.distance)

print("data treatment/filter is done")

######################################
## MAKE ONE SET OF GRAPHICS
######################################
#plt.ion()
#
##a, b, c = plt.hist(ch5DistanceFilter.values(),  bins=250, range=(0,2000))
#
#
##plt.show()
#
### to clean display:
#plt.clf()
#
#vector = [300, 250, 200, 180, 150, 130, 110, 100, 80, 60, 40, 30, 20, 10]
#counter = 0
#
#for i in vector:
#	a, b, c = plt.hist(ch5DistanceFilter.values(),  bins = i, range=(0,2000), histtype='step')
#	counter +=1
#	plt.savefig('ch5Distance_' + str("%02d" % counter) +'.png')
#
######################################
### MAKE GRAPHS FOR EVERY CHROMOSOME
######################################


## Interactive plots
#plt.ion()

## Variables
#min_range = 0
# max_range = 2000
#plotrange=(0, 1000)
#chrom_counter = 0

## Number of classes for each histogram
#vector = [300, 250, 200, 180, 150, 130, 110, 100, 80, 60, 40, 30, 20, 10]
## Max Y coordinate for each graphic
# max_y = [7, 8, 9, 9, 12, 12, 12, 16, 18, 20, 30, 40, 60, 100, 140, 200]
#max_y = 200


## Create SP and noSP lists
#sp = [k for k, value in test.tag.iteritems() if value == 'SP']
#nosp = [k for k, value in test.tag.iteritems() if value == 'other']


## Parse the list of chromosomes (1 to 8)
#for j in test.chromList:
#	chrom_counter +=1
#	print('Making graphs for chromosome: ' +str(chrom_counter))
#	chnDistanceFilter = test.getDistanceFiltered(j, test.distance)
#	plt.clf()
#	counter = 0

	## start making the graphics for all genes
# 	for i, k in zip(vector, max_y) :
#	for i in vector :
#		plt.clf()
#		a, b, c = plt.hist(chnDistanceFilter.values(),  bins = i, range=plotrange, histtype='step'
#				, color=['red'], label=['All genes']
#				, cumulative = True
#				)
#		counter +=1
#		plt.title('Ch ' + str(chrom_counter) + \
#			'- from ' + str(min_range) + ' to ' + str(plotrange[1]) + ' nuc (' +\
#			str(i) + ' classes - ' + str(plotrange[1]/i) + ' nuc each)')
## 		plt.ylim(0, k)
## 		plt.ylim(0)
#		plt.ylim(0, max_y)

	## add graphics for only SP
#		temp_sp = []
#		for l in sp :
#			if l in j:
#				temp_sp.append(l)
#		toPlotSp = test.getDistanceFiltered(temp_sp, test.distance)
#		a, b, c = plt.hist( toPlotSp.values(), bins = i\
#			, range=plotrange, histtype='step'\
#			, color=['cyan'], label=['SP']
#			, cumulative = True
#			)

	## add graphics for only noSP
#		temp_nosp = []
#		for l in nosp :
#			if l in j:
#				temp_nosp.append(l)
#		toPlotNosp = test.getDistanceFiltered(temp_nosp, test.distance)
#		a, b, c = plt.hist( toPlotNosp.values(), bins = i\
#			, range=plotrange, histtype='step'\
#			, color=['blue'], label=['noSP']
#			, cumulative = True
#			)


	## plot the legend
#		plt.legend()
#
	## execute plot and save it to file
#		plt.savefig('ch'+ str(chrom_counter) + \
#		'/ch' + str(chrom_counter) + 'Distance_' + str("%02d" % counter) +'.png')

## Clear any graphic on the memory
#plt.clf()


######################################
### Make vectors for proportion graphs
######################################


## Interactive plots
plt.ion()

## Variables
min_range = 0
max_distance = 1000
# max_range = 2000
plotrange=(0, 1000)
chrom_counter = 0

## Number of classes for each histogram
vector = [300, 250, 200, 180, 150, 130, 110, 100, 80, 60, 40, 30, 20, 10]
## Max Y coordinate for each graphic
# max_y = [7, 8, 9, 9, 12, 12, 12, 16, 18, 20, 30, 40, 60, 100, 140, 200]
max_y = 200


## Create SP and noSP lists
sp = [k for k, value in test.tag.iteritems() if value == 'SP']
nosp = [k for k, value in test.tag.iteritems() if value == 'other']


## Parse the list of chromosomes (1 to 8)
for j in test.chromList:
	chrom_counter +=1
	print('Making graphs for chromosome: ' +str(chrom_counter))
	chnDistanceFilter = test.getDistanceFiltered(j, test.distance)
	plt.clf()
	counter = 0

	## start making the graphics for all genes
# 	for i, k in zip(vector, max_y) :
	for i in vector :
		plt.clf()
		toPlotFull = dict((k, v) for (k, v) in chnDistanceFilter.iteritems() if v < max_distance)
		a, b, c = plt.hist(toPlotFull.values(),  bins = i, range=plotrange, histtype='step'
				, color=['red'], label=['All genes']
				, cumulative = True
				)
		counter +=1
		plt.title('Ch ' + str(chrom_counter) + \
			'- from ' + str(min_range) + ' to ' + str(plotrange[1]) + ' nuc (' +\
			str(i) + ' classes - ' + str(plotrange[1]/i) + ' nuc each)')
# 		plt.ylim(0, k)
# 		plt.ylim(0)
		plt.ylim(0, max_y)

	## add graphics for only SP
		temp_sp = []
		for l in sp :
			if l in j:
				temp_sp.append(l)
		patate = test.getDistanceFiltered(temp_sp, test.distance)
		toPlotSp = dict((k, v) for (k, v) in patate.iteritems() if v < max_distance)
		a, b, c = plt.hist( toPlotSp.values(), bins = i\
			, range=plotrange, histtype='step'\
			, color=['cyan'], label=['SP']
			, cumulative = True
			)

	## add graphics for only noSP
		temp_nosp = []
		for l in nosp :
			if l in j:
				temp_nosp.append(l)
		patate = test.getDistanceFiltered(temp_nosp, test.distance)
		toPlotNosp = dict((k, v) for (k, v) in patate.iteritems() if v < max_distance)
		a, b, c = plt.hist( toPlotNosp.values(), bins = i\
			, range=plotrange, histtype='step'\
			, color=['blue'], label=['noSP']
			, cumulative = True
			)


	## plot the legend
		plt.legend()

	## execute plot and save it to file
		plt.savefig('ch'+ str(chrom_counter) + \
		'/ch' + str(chrom_counter) + 'Distance_' + str("%02d" % counter) +'.png')

## Clear any graphic on the memory
plt.clf()
