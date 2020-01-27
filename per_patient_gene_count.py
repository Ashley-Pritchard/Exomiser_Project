#counts how many genes per patient have a combined exomiser score > cutoff specified by user 

import glob
import pandas as pd
import sys
import csv 
import argparse
import os

#request command line input of the cutoff value for the combined score to be applied and run name 
parser = argparse.ArgumentParser()
parser.add_argument("cutoff", help='state the combined score cutoff to be used when running script')
parser.add_argument("run_name", help='input the name of the run you are analysing')
args = parser.parse_args()

#pull all gene analysis files output from exomiser 
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name + '/*.genes.tsv')

#make a new analysis directory of the run name if one does not exist already
os.makedirs('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/' + args.run_name, exist_ok=True)

#create an empty list for counting the number of genes with a combined score > cutoff for each patient 
number_of = []

for ex_file in exomiser_files:
	df = pd.read_csv(ex_file, sep='\t')
	count = 0
	for index, row in df.iterrows(): 
		if row[4] > float(args.cutoff):
			count +=1

	number_of.append(count)

#make a new dataframe of gene counts
df = pd.DataFrame(number_of, columns=['Number_of_Genes_to_Investigate'])

#save as csv to analysis folder 
df.to_csv('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/' + args.run_name + '/#_Genes_>_' + args.cutoff + '.csv', sep=',', header = True)


