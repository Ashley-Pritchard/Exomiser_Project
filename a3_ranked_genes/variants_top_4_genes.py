import argparse
import glob
import os
import re
import pandas as pd
import sys

#request command line input of the cutoff value for the combined score to be applied
parser = argparse.ArgumentParser()
parser.add_argument("run_name", help='input the name of the run you are analysing')
args = parser.parse_args()

#pull all variant analysis files output from exomiser 
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name + '/*.variants.tsv')

patient = []
variant = []

#iterate through files and append combined score to empty list 
for ex in exomiser_files:
	df = pd.read_csv(ex, sep='\t')
	for index, row in df.iterrows():
		if row[10] == 'DES' and row[31] >=0.9:
			variant.append(row[9])
			patient.append(re.split('/', ex)[7])
		elif row[10] == 'NAGLU' and row[31] >=0.9:
			variant.append(row[9])
			patient.append(re.split('/', ex)[7])
		elif row[10] == 'MYH7' and row[31] >=0.9:
			variant.append(row[9])
			patient.append(re.split('/', ex)[7])
		elif row[10] == 'MYOZ2' and row[31] >=0.9:
			variant.append(row[9])
			patient.append(re.split('/', ex)[7])

dict = { 'patient': patient, 'variant' : variant }

#make a new dataframe of variant counts
df = pd.DataFrame(dict)

df.to_csv('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/' + args.run_name + '/_top_4' + '.csv', sep=',', header = True)
