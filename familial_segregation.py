#segregation analysis - script to pull data for variants seen in all members of a family 

import glob
import pandas as pd
import argparse
import os

#request command line input of the run name and CAR number for the family 
parser = argparse.ArgumentParser()
parser.add_argument("run_name", help='input the name of the run you are analysing')
parser.add_argument("family", help='input the family reference number you are analysing')
args = parser.parse_args()

#pull variant files for family members 
exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name + '/' + args.family + '/*.variants.tsv')

#make folder in relevant analysis directory if one does not exist 
os.makedirs('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/' + args.run_name + '/' + args.family, exist_ok=True)

#create a single dataframe for the family by concatenating the variant files for family members 
df = pd.concat((pd.read_csv(ex_file, sep='\t') for ex_file in exomiser_files), ignore_index=True)

#calculate the size of the family based on the number of files 
family_size = len(exomiser_files)

#create a new dataframe consisting of only variants seen in all family members
df = pd.concat(g for _, g in df.groupby("HGVS") if len(g) >= family_size)

#drop columns not required 
df = df.drop(columns=['#CHROM', 'POS', 'REF', 'ALT', 'COVERAGE', 'QUAL', 'FILTER', 'GENOTYPE', 'POLYPHEN(>0.956|>0.446)', 'MUTATIONTASTER(>0.94)', 'SIFT(<0.06)', 'REMM', 'DBSNP_FREQUENCY', 'EVS_EA_FREQUENCY', 'EVS_AA_FREQUENCY', 'EXAC_AFR_FREQ', 'EXAC_AMR_FREQ', 'EXAC_EAS_FREQ', 'EXAC_FIN_FREQ', 'EXAC_NFE_FREQ', 'EXAC_SAS_FREQ', 'EXAC_OTH_FREQ', 'CONTRIBUTING_VARIANT'])

#rename remaining columns 
df = df.rename(columns={'FUNCTIONAL_CLASS': 'Class', 'EXOMISER_GENE': 'Gene', 'CADD(>0.483)': 'CADD', 'DBSNP_ID':'dbSNP', 'MAX_FREQUENCY': 'Max_Allel_Freq', 'EXOMISER_VARIANT_SCORE': 'Variant_Score_Exomiser', 'EXOMISER_GENE_PHENO_SCORE': 'Gene_Pheno_Score_Exomiser', 'EXOMISER_GENE_VARIANT_SCORE': 'Gene_Variant_Score_Exomiser', 'EXOMISER_GENE_COMBINED_SCORE': 'Combined_Score_Exomiser'})

#drop the duplicate variants so there is one record for each
df = df.drop_duplicates(keep='first')

#sort variants by combined exomiser score 
df = df.sort_values(by=['Combined_Score_Exomiser'], ascending=False)

#reorder columns of dataframe 
df = df[['HGVS', 'Gene', 'Class', 'dbSNP', 'Max_Allel_Freq', 'CADD', 'Variant_Score_Exomiser', 'Gene_Pheno_Score_Exomiser', 'Gene_Variant_Score_Exomiser', 'Combined_Score_Exomiser']]

#save dataframe as csv to relevant analysis directory 
df.to_csv('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/analysis/' + args.run_name + '/' + args.family + '/familial_variants_' + args.family + '.csv', sep=',', index=False)

