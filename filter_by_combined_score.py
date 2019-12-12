import glob
import pandas as pd
import sys

exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/20191211/*.genes.tsv')

gene = []

for ex_file in exomiser_files:
	df = pd.read_csv(ex_file, sep='\t')
	for index, row in df.iterrows(): 
		if row[4] > 0.9:
			gene.append(row[0])

df2 = pd.DataFrame(gene, columns=['Gene'])

df2 = df2.groupby(['Gene']).size().sort_values(ascending=False)

df2.to_csv('20191211_gene_list_combined_score_>_0.9.csv', sep=',', header=True)

