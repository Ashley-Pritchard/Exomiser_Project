#create a csv file for a single case analysis for each of the cases with additional phenotype data 

import glob 
import csv 
import pandas as pd
import re
import os

#pull the exomiser files for the patient cases
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/20191213_pheno_cases/*.variants.tsv')

#make a new analysis directory of the run name if one does not exist already
os.makedirs('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/20191213_pheno_cases', exist_ok=True)

#iterate though patient cases 
for ex_file in exomiser_files:
	#create a new dataframe from the variant output file 
	df = pd.read_csv(ex_file, sep='\t')

	#drop columns not required 
	df = df.drop(columns=['#CHROM', 'POS', 'REF', 'ALT', 'COVERAGE', 'QUAL', 'FILTER', 'POLYPHEN(>0.956|>0.446)', 'MUTATIONTASTER(>0.94)', 'SIFT(<0.06)', 'REMM', 'DBSNP_FREQUENCY', 'EVS_EA_FREQUENCY', 'EVS_AA_FREQUENCY', 'EXAC_AFR_FREQ', 'EXAC_AMR_FREQ', 'EXAC_EAS_FREQ', 'EXAC_FIN_FREQ', 'EXAC_NFE_FREQ', 'EXAC_SAS_FREQ', 'EXAC_OTH_FREQ', 'CONTRIBUTING_VARIANT'])

	#rename remaining columns 
	df = df.rename(columns={'FUNCTIONAL_CLASS': 'Class', 'GENOTYPE': 'Genotype', 'EXOMISER_GENE': 'Gene', 'CADD(>0.483)': 'CADD', 'DBSNP_ID':'dbSNP', 'MAX_FREQUENCY': 'Max_Allel_Freq', 'EXOMISER_VARIANT_SCORE': 'Variant_Score_Exomiser', 'EXOMISER_GENE_PHENO_SCORE': 'Gene_Pheno_Score_Exomiser', 'EXOMISER_GENE_VARIANT_SCORE': 'Gene_Variant_Score_Exomiser', 'EXOMISER_GENE_COMBINED_SCORE': 'Combined_Score_Exomiser'})

	#order the variants by combined exomiser score and HGVS name 
	df = df.sort_values(by=['Combined_Score_Exomiser', 'HGVS'], ascending=False)

	#reorder columns 
	df = df[['HGVS', 'Genotype', 'Gene', 'Class', 'dbSNP', 'Max_Allel_Freq', 'CADD', 'Variant_Score_Exomiser', 'Gene_Pheno_Score_Exomiser', 'Gene_Variant_Score_Exomiser', 'Combined_Score_Exomiser']]

	#generate a file name 
	name_1 = re.split('_|/|\.', ex_file)[14]
	name_2 = re.split('_|/|\.', ex_file)[15]
	name = name_1 + '_' + name_2

	#save as csv to appropriate analysis directory 
	df.to_csv('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/20191213_pheno_cases/' + name + '.csv', sep=',', index=False)
