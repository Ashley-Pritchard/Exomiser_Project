import glob
import pandas as pd
import sys
import csv 

exomiser_files = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/20191211/*.genes.tsv')

number_of = []

for ex_file in exomiser_files:
	df = pd.read_csv(ex_file, sep='\t')
	count = 0
	for index, row in df.iterrows(): 
		if row[4] > 0.9:
			count +=1

	number_of.append(count)

df = pd.DataFrame(number_of, columns=['Number_of_Variants_to_Investigate'])
df.to_csv('20191211_#_Variants_>_0.9.csv', sep=',', header = True)


