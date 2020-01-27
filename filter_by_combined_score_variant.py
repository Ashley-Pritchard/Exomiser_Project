#script to pull all variants with a combined exomiser score over a defined cutoff and provide a count of how many times the variant was seen in the patient cohort 

import argparse
import glob
import os
import pandas as pd
import sys

#request command line input of the cutoff value for the combined score to be applied
parser = argparse.ArgumentParser()
parser.add_argument("cutoff", help='state the combined score cutoff to be used when running script')
parser.add_argument("run_name", help='input the name of the run you are analysing')
args = parser.parse_args()

#pull all variant analysis files output from exomiser 
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name + '/*.variants.tsv')

#make a new analysis directory of the run name if one does not exist already
os.makedirs('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/' + args.run_name, exist_ok=True)

#create an empty list for appending variants with a combined exomiser score > cutoff value specified by user 
variant = []

#iterate through the exomiser files and append variants over the exomiser score cutoff to the empty variant list 
for ex_file in exomiser_files:
	df = pd.read_csv(ex_file, sep='\t')
	for index, row in df.iterrows(): 
		if row[31] > float(args.cutoff):
			variant.append(row[9])

#create a dataframe from the variant list
df2 = pd.DataFrame(variant, columns=['Variant'])

#group and count repeated variants - order descending 
df2 = df2.groupby(['Variant']).size().sort_values(ascending=False)

#save results as csv file to the analysis folder for that run
df2.to_csv('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/' + args.run_name + '/variant_list_combined_score_>_' + args.cutoff + '.csv', sep=',', header=True)

