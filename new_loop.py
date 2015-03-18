#! /Users/orteegaabboud/anaconda/bin/python
import pickle as pic

toPlotFull = pic.load(open("toPlotFull.dico", "rb"))
toPlotNosp = pic.load(open("toPlotNosp.dico", "rb"))
toPlotSp = pic.load(open("toPlotSp.dico", "rb"))



# max distance to make plot
max_distance = 1000

# shorten dictionary to the max size we want to plot
dico_to_treat = dict((k,v) for k,v if v <= max_distance)

# number of bins requested to be plotted
bin_num = 10

# treat the dictionary for a given number of expected bins
def patate(self, dico_to_treat, bins_num)
	
	# create list to be returned, the lenght equals the number of bins
	# it contains integers of the number of genes contained in each bin
	list_GenesPerClass = []

	# for each bin from 1 to the last bin requested
	for i in range(1,( bin_num + 1 )):
		# calculate the min and max values for the bin
		bin_val_r = ( max_distance/bin_num) * i
		bin_val_l = (max_distance/bin_num) * (i-1)
		# from the dictionary get only the keys/values from
		# genes who's distance is encompassed between the interval [bin_val_l; bin_val_r]
		bin_dico = dict((k,v) for (k,v) in dico_to_read if (v < bin_val_r) and (v > bin_val_l))
		# lenght of the dictionary == number of genes in that bin
		# add this value to the list of genes per class
		list_GenesPerClass.append(len(bin_dico)

	# return list don't forget to unpack it to a variable !
	return list_GenesPerClass

