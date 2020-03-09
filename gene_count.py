#script to count the number of genes that autosomal dominant (AD) and autosomal recessive (AR) variants presented in per patient and output findings as box plots.

import argparse
import glob
import os
import pandas as pd
import sys
import matplotlib.pyplot as plt
from operator import add 
import statistics

#request command line input of the AD and AR run names for analysis
parser = argparse.ArgumentParser()
parser.add_argument("run_name_AD", help='input the name of the run you are analysing')
parser.add_argument("run_name_AR", help='input the name of the run you are analysing')
args = parser.parse_args()

#output files from each Exomiser run were transferred from the CSD3 server to a 'exomiser_output_files' directory on the local machine
#pull all AD gene analysis files for specified run
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name_AD + '/*.genes.tsv')

#create an exmpty list to append AD variant count  
AD = []

#iterate through files and append the count of genes with AD variants per patient to empty list 
for ex in exomiser_files:
	df = pd.read_csv(ex, sep='\t')
	count = len(df)			
	AD.append(count)

#pull all AR gene analysis files for specified run
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name_AR + '/*.genes.tsv')

#create an exmpty list to append AR variant count 
AR = []

#iterate through files and append the count of genes with AR variants per patient to empty list 
for ex in exomiser_files:
	df = pd.read_csv(ex, sep='\t')
	count = len(df)			
	AR.append(count)

print('The median AD gene count is:' + str(statistics.median(AD)))
print('The median AR gene count is:' + str(statistics.median(AR)))

#set data to plot as the calculated AD and AR gene counts per patient 
data_to_plot = [AD, AR]

#plot boxplot for the count of genes with AD and AR variants per patient
plt.boxplot(data_to_plot, vert=True)
plt.xticks([1, 2], ['AD', 'AR'])
plt.xlabel('Inheritance Pattern', labelpad=10)
plt.ylabel('Number of Genes', labelpad=10)
plt.title('Number of Genes with Variants per Patient', pad=10)
plt.show()
