#script to pull the 269 hypertrophic cardiomyopathy patient IDs from the CSD3 and save them as a text file for reference in later analysis
import glob
import re
import sys
import csv

#select all vcf files
vcf_file_path = glob.glob('/home/hpcprit1/rds/rds-who1000-wgs10k/WGS10K/data/release/20180228-A/vcf/HCM/*.vcf.gz')

#make empty list for vcf names 
vcf_IDs = []

#iterate through file names and split on '/' and '_' to pull out the vcf id - append to the empty list  
for vcf in vcf_file_path:
        vcf_ID = re.split('/|_', vcf)[11]
        vcf_IDs.append(vcf_ID)

#write the list of vcf names to a text file with each name on a new line
with open('vcf_IDs.txt', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for vcf_ID in vcf_IDs:
                writer.writerow([vcf_ID])

