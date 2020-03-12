#script to pull data for variants with a combined Exomiser score of more than 0.9 for patient cases with additional phenotype data 

import glob
import pandas as pd
import argparse
import os
import re 

#request command line input of the run name
parser = argparse.ArgumentParser()
parser.add_argument("run_name", help='input the name of the run you are analysing')
args = parser.parse_args()

#output files from each Exomiser run were transferred from the CSD3 server to a 'exomiser_output_files' directory on the local machine
#pull variant analysis files for specified run
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name + '/*.variants.tsv')

#make directory to store analysis files if one does not exist 
os.makedirs(args.run_name, exist_ok=True)

#iterate through the variant files and save each as a pandas dataframe
for ex in exomiser_files:
	df = pd.read_csv(ex, sep='\t')

	#drop variants with a combined Exomiser Score of less than 0.9
	df = df[df['EXOMISER_GENE_COMBINED_SCORE'] > 0.9]

	#drop columns not required 
	df = df.drop(columns=['#CHROM', 'POS', 'REF', 'ALT', 'COVERAGE', 'QUAL', 'FILTER', 'GENOTYPE', 'POLYPHEN(>0.956|>0.446)', 'MUTATIONTASTER(>0.94)', 'SIFT(<0.06)', 'REMM', 'DBSNP_FREQUENCY', 'EVS_EA_FREQUENCY', 'EVS_AA_FREQUENCY', 'EXAC_AFR_FREQ', 'EXAC_AMR_FREQ', 'EXAC_EAS_FREQ', 'EXAC_FIN_FREQ', 'EXAC_NFE_FREQ', 'EXAC_SAS_FREQ', 'EXAC_OTH_FREQ', 'CONTRIBUTING_VARIANT'])

	#rename remaining columns 
	df = df.rename(columns={'FUNCTIONAL_CLASS': 'Class', 'EXOMISER_GENE': 'Gene', 'CADD(>0.483)': 'CADD', 'DBSNP_ID':'dbSNP', 'MAX_FREQUENCY': 'Max_Allel_Freq', 'EXOMISER_VARIANT_SCORE': 'Variant_Score_Exomiser', 'EXOMISER_GENE_PHENO_SCORE': 'Gene_Pheno_Score_Exomiser', 'EXOMISER_GENE_VARIANT_SCORE': 'Gene_Variant_Score_Exomiser', 'EXOMISER_GENE_COMBINED_SCORE': 'Combined_Score_Exomiser'})

	#sort variants by combined exomiser score 
	df = df.sort_values(by=['Combined_Score_Exomiser'], ascending=False)

	#reorder columns of dataframe 
	df = df[['HGVS', 'Gene', 'Class', 'dbSNP', 'Max_Allel_Freq', 'CADD', 'Variant_Score_Exomiser', 'Gene_Pheno_Score_Exomiser', 'Gene_Variant_Score_Exomiser', 'Combined_Score_Exomiser']]
	
	#set the file name by splitting the path to get patient ID 
	name = re.split('/|_', ex)[15]

	#save dataframe as csv to relevant analysis directory 
	df.to_csv(args.run_name + '/' + name + '.csv', sep=',', index=False)

