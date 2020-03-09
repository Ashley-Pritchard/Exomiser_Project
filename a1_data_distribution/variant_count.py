#script to count autosomal dominant (AD), autosomal recessive (AR) and the total number of variants per patient and output findings as box plots.

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
#pull all AD variant analysis files for specified run
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name_AD + '/*.variants.tsv')

#create an exmpty list to append AD variant count  
AD = []

#iterate through files and append the count of AD variants >0.9 per patient to empty list 
for ex in exomiser_files:
	df = pd.read_csv(ex, sep='\t')
	count = len(df)			
	AD.append(count)

#pull all AR variant analysis files for specified run
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name_AR + '/*.variants.tsv')

#create an exmpty list to append AR variant count 
AR = []

#iterate through files and append the count of AR variants >0.9 per patient to empty list 
for ex in exomiser_files:
	df = pd.read_csv(ex, sep='\t')
	count = len(df)			
	AR.append(count)

print('The median AD variant count is:' + str(statistics.median(AD)))
print('The median AR variant count is:' + str(statistics.median(AR)))

#set data to plot as the calculated AD and AR variant counts per patient 
data_to_plot = [AD, AR]

#plot boxplot for the count of AD and AR variants per patient
plt.boxplot(data_to_plot, vert=True)
plt.xticks([1, 2], ['AD', 'AR'])
plt.xlabel('Inheritance Pattern', labelpad=10)
plt.ylabel('Number of Variants', labelpad=10)
plt.title('Number of Variants per Patient', pad=10)
plt.show()

#set data to plot as the total number of AD and AR variants per patient 
total = list(map(add, AD, AR))

#plot boxplot for the total count of AD and AR variants per patient 
plt.boxplot(total, vert=True)
plt.xticks([1], [''])
plt.xlabel('Total AD and AR', labelpad=10)
plt.ylabel('Number of Variants', labelpad=10)
plt.title('Number of Variants per Patient', pad=10)
plt.show()
