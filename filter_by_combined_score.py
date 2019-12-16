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
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name + '/*.genes.tsv')

#make a new analysis directory of the run name if one does not exist already
os.makedirs('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/' + args.run_name, exist_ok=True)

#create an empty list for counting the number of times a variant was seen in the genes 
gene = []

#iterate through the exomiser files and append genes over the applied combined score cutoff to the empty gene list 
for ex_file in exomiser_files:
	df = pd.read_csv(ex_file, sep='\t')
	for index, row in df.iterrows(): 
		if row[4] > float(args.cutoff):
			gene.append(row[0])

#create a dataframe from the gene list
df2 = pd.DataFrame(gene, columns=['Gene'])

#group and count repeated genes - order descending based on those with the most variants 
df2 = df2.groupby(['Gene']).size().sort_values(ascending=False)

#save results as csv file to the analysis folder for that run
df2.to_csv('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/' + args.run_name + '/gene_list_combined_score_>_' + args.cutoff + '.csv', sep=',', header=True)

