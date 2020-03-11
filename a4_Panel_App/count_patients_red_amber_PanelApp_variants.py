#script to count the number of patients who have variants with an Exomiser combined score of more than 0.9 in red or amber HCM PanelApp genes. 

import argparse
import glob
import os
import pandas as pd
import sys
import matplotlib.pyplot as plt
from collections import Counter 

#request command line input of the run name to be analsed 
parser = argparse.ArgumentParser()
parser.add_argument("run_name", help='input the name of the run you are analysing')
args = parser.parse_args()

#output files from each Exomiser run were transferred from the CSD3 server to a 'exomiser_output_files' directory on the local machine
#pull all variant analysis files for specified run
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name + '/*.variants.tsv')

#a csv file listing the current red and amber HCM PanelApp genes was downloaded from the GEL website for use.
#read in file as a pandas dataframe
df = pd.read_csv('PanelApp_HCM_Amber_Red_Genes.csv', sep='\t')

#create an empty list for the gene names 
gene_list = []

#iterate through the PanelApp genes and append them to the empty gene list 
for index, row in df.iterrows():
	gene_list.append(row[0])

#create an exmpty list for counting the number of variants  
count_list = []

#loop through Exomiser variant files, open them as pandas dataframes and set a count to 0
for ex in exomiser_files:
	df = pd.read_csv(ex, sep='\t')
	count=0
	#iterate through the variant dataframes and add one to the count for every variant in a gene named in the gene list and with a combined score of over 0.9 
	for index, row in df.iterrows():
		if row[10] in gene_list and row[31] >=0.9:
			count += 1
	#add the count for each patient to the empty count list 
	count_list.append(count)

#count the counts (i.e. how many patients had 0 / 1 / 2 etc.) and store as dictionary 
count_dictionary = Counter(count_list)

#assign values for plotting 
keys = ('zero', 'one', 'two', 'three')
values = sorted(count_dictionary.values(), reverse=True)

#blot barchart of counts
plt.bar(keys, values, color = 'orangered', edgecolor = 'black')
plt.xlabel('Number of Variants in Red or Amber PanelApp Genes',labelpad=10)
plt.ylabel('Number of Patients', labelpad=10)
plt.title('Patients with Variants in Red or Amber PanelApp Genes', pad=10)
plt.show()

