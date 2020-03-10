#script to pull gene score data for all genes found to harbour autosomal dominant or autosomal recessive variants in the 269 HCM patient cohort. Outputs data as csv files ordered by gene score descending. 

import argparse
import glob
import os
import pandas as pd
import sys

#request command line input of the run name for analysis 
parser = argparse.ArgumentParser()
parser.add_argument("run_name", help='input the name of the run you are analysing')
args = parser.parse_args()

#output files from each Exomiser run were transferred from the CSD3 server to a 'exomiser_output_files' directory on the local machine
#pull all gene analysis files for specified run
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name + '/*.genes.tsv')

#create a single dataframe by concatenating the gene files 
df = pd.concat((pd.read_csv(ex_file, sep='\t') for ex_file in exomiser_files), ignore_index=True)

#drop columns not required 
df = df.drop(columns=['ENTREZ_GENE_ID', 'MATCHES_CANDIDATE_GENE', 'MATCHES_CANDIDATE_GENE', 'EXOMISER_GENE_VARIANT_SCORE', 'EXOMISER_GENE_COMBINED_SCORE'])

#drop the duplicate genes so there is one record for each
df = df.drop_duplicates(keep='first')

#sort genes by combined exomiser score 
df = df.sort_values(by=['EXOMISER_GENE_PHENO_SCORE'], ascending=False)

#save dataframe as csv to relevant analysis directory 
df.to_csv(args.run_name + '_ranked_genes.csv', sep=',', header=True)
