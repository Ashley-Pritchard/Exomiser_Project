import glob
import pandas as pd

exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/20191211/s8/*.variants.tsv')

df = pd.concat((pd.read_csv(ex_file, sep='\t') for ex_file in exomiser_files), ignore_index=True)

family_size = len(exomiser_files)
df = pd.concat(g for _, g in df.groupby("HGVS") if len(g) >= family_size)

df = df.drop(columns=['#CHROM', 'POS', 'REF', 'ALT', 'COVERAGE', 'QUAL', 'FILTER', 'GENOTYPE', 'POLYPHEN(>0.956|>0.446)', 'MUTATIONTASTER(>0.94)', 'SIFT(<0.06)', 'REMM', 'DBSNP_FREQUENCY', 'EVS_EA_FREQUENCY', 'EVS_AA_FREQUENCY', 'EXAC_AFR_FREQ', 'EXAC_AMR_FREQ', 'EXAC_EAS_FREQ', 'EXAC_FIN_FREQ', 'EXAC_NFE_FREQ', 'EXAC_SAS_FREQ', 'EXAC_OTH_FREQ', 'CONTRIBUTING_VARIANT'])

df = df.rename(columns={'FUNCTIONAL_CLASS': 'Class', 'EXOMISER_GENE': 'Gene', 'CADD(>0.483)': 'CADD', 'DBSNP_ID':'dbSNP', 'MAX_FREQUENCY': 'Max_Allel_Freq', 'EXOMISER_VARIANT_SCORE': 'Variant_Score_Exomiser', 'EXOMISER_GENE_PHENO_SCORE': 'Gene_Pheno_Score_Exomiser', 'EXOMISER_GENE_VARIANT_SCORE': 'Gene_Variant_Score_Exomiser', 'EXOMISER_GENE_COMBINED_SCORE': 'Combined_Score_Exomiser'})

df = df.drop_duplicates(keep='first')

df = df.sort_values(by=['Combined_Score_Exomiser'], ascending=False)

df = df[['HGVS', 'Gene', 'Class', 'dbSNP', 'Max_Allel_Freq', 'CADD', 'Variant_Score_Exomiser', 'Gene_Pheno_Score_Exomiser', 'Gene_Variant_Score_Exomiser', 'Combined_Score_Exomiser']]

df.to_csv('familial_variants_5038.csv', sep=',')


