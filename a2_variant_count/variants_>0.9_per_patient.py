#script to count the number of autosomal dominant (AD) and autosomal recessive (AR) variants with a combined score >0.9 per patient and output findings as box plots.

import argparse
import glob
import os
import pandas as pd
import sys
import matplotlib.pyplot as plt
from operator import add 

#request command line input of the AD and AR run names for analysis
parser = argparse.ArgumentParser()
parser.add_argument("run_name_AD", help='input the name of the run you are analysing')
parser.add_argument("run_name_AR", help='input the name of the run you are analysing')
args = parser.parse_args()

#output files from each Exomiser run were transferred from the CSD3 server to a 'exomiser_output_files' directory on the local machine
#pull all AD variant analysis files for specified run
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name_AD + '/*.variants.tsv')

#create an exmpty list to append AD variant count  
AD = []

#iterate through files and append the count of AD variants >0.9 per patient to empty list 
for ex in exomiser_files:
	df = pd.read_csv(ex, sep='\t')
	count = 0
	for index, row in df.iterrows():
		if row[31] >= 0.9:
			count += 1			
	if count > 0:
		AD.append(count)
	else:
		AD.append(0)

#pull all AR variant analysis files for specified run
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name_AR + '/*.variants.tsv')

#create an exmpty list to append AR variant count 
AR = []

#iterate through files and append the count of AR variants >0.9 per patient to empty list 
for ex in exomiser_files:
	df = pd.read_csv(ex, sep='\t')
	count = 0
	for index, row in df.iterrows():
		if row[31] >= 0.9:
			count += 1
	if count > 0:	
		AR.append(count)
	else:
		AR.append(0)

#set data to plot as the calculated AD and AR variant counts per patient 
data_to_plot = [AD, AR]

#plot boxplot for the count of AD and AR variants with a combined score >0.9 per patient
plt.boxplot(data_to_plot, vert=True)
plt.xticks([1, 2], ['AD', 'AR'])
plt.xlabel('Inheritance Pattern', labelpad=10)
plt.ylabel('Number of Variants', labelpad=10)
plt.title('Number of Variants per Patient with a Combined Score >0.9', pad=10)
plt.show()

