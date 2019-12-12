import glob
import re
import sys
import csv

vcf_paths = glob.glob('/home/hpcprit1/rds/rds-who1000-wgs10k/WGS10K/data/release/20180228-A/vcf/HCM/*.vcf.gz')

vcf_files = []
for vcf in vcf_paths:
        vcf_file = re.split('/|_', vcf)[11]
        vcf_files.append(vcf_file)

with open('vcfs.txt', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for vcf in vcf_files:
                writer.writerow([vcf])

