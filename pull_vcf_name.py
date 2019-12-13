import glob
import re
import sys
import csv

#select all vcf files
vcf_paths = glob.glob('/home/hpcprit1/rds/rds-who1000-wgs10k/WGS10K/data/release/20180228-A/vcf/HCM/*.vcf.gz')

#make empty list for vcf names 
vcf_files = []

#iterate through file names and split on '/' and '_' to pull out the vcf id - append to the empty list  
for vcf in vcf_paths:
        vcf_file = re.split('/|_', vcf)[11]
        vcf_files.append(vcf_file)

#write the list of vcf names to a text file with each name on a new line
with open('vcfs.txt', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for vcf in vcf_files:
                writer.writerow([vcf])

