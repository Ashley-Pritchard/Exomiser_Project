#script to pull HGVS name and respective patient IDs for all variants occuring in the top 4 ranked genes (DES, NAGLU, MYH7 and MYOZ2). Data output as csv files. 

import argparse
import glob
import os
import re
import pandas as pd
import sys

#request command line input of the run name for analysis 
parser = argparse.ArgumentParser()
parser.add_argument("run_name", help='input the name of the run you are analysing')
args = parser.parse_args()

#output files from each Exomiser run were transferred from the CSD3 server to a 'exomiser_output_files' directory on the local machine
#pull all variant analysis files for specified run
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name + '/*.variants.tsv')

#set empty lists for collecting patient and variant data
patient = []
variant = []

#iterate through files and append respective HGVS and patient ID data for variants occuring in genes of interest
for ex in exomiser_files:
	df = pd.read_csv(ex, sep='\t')
	for index, row in df.iterrows():
		if row[10] == 'DES' and row[31] >=0.9:
			variant.append(row[9])
			patient.append(re.split('/|_', ex)[13])
		elif row[10] == 'NAGLU' and row[31] >=0.9:
			variant.append(row[9])
			patient.append(re.split('/|_', ex)[13])
		elif row[10] == 'MYH7' and row[31] >=0.9:
			variant.append(row[9])
			patient.append(re.split('/|_', ex)[13])
		elif row[10] == 'MYOZ2' and row[31] >=0.9:
			variant.append(row[9])
			patient.append(re.split('/|_', ex)[13])

#make dictionary of pulled patient and variant data 
dict = { 'patient': patient, 'variant' : variant }

#make a new dataframe using the dictionary created
df = pd.DataFrame(dict)

#write data to csv file
df.to_csv(args.run_name + '_variants_in_top_genes' + '.csv', sep=',', header = True)
