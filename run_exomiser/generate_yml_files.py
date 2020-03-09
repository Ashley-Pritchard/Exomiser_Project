#script to generate individual yml files for each of the 269 hypertrophic cardiomyopathy variants. 
import ruamel.yaml
import argparse
import os

#pull vcf IDs from previously derived text file 
vcf_IDs = [line.rstrip('\n') for line in open('vcf_IDs.txt')]

#make use of the ruamel yaml file parser
yaml = ruamel.yaml.YAML()

#request a name for the run to be input as a command line argument
parser = argparse.ArgumentParser()
parser.add_argument("run_name", help='provide a run name')
args = parser.parse_args()

#make a new directory of the run name if one does not exist already - inform user and exit if the run name has already been used
if os.path.exists(args.run_name):
	print('a file with that run name already exists')
	exit()
else: 
	os.mkdir(args.run_name)

#select the yml template
yml_template = 'yml_template.yml' 

#itterate through the vcf file names to create a new yaml anlysis file based on the selected template for each. 

for vcf in vcf_IDs:
	with open(yml_template) as f:
		script = yaml.load(f)
	#Exomiser needs to be run within the CSD3, so the absolute file paths are provided.
	script['analysis']['vcf'] = '/home/hpcprit1/rds/rds-who1000-wgs10k/WGS10K/data/release/20180228-A/vcf/HCM/' + vcf + '_A.vcf.gz'
	script['outputOptions']['outputPrefix'] = '/home/hpcprit1/Documents/Exomiser_Project/results/' + vcf

	#save the new yaml files in the directory created above
	with open(args.run_name + '/' + vcf + '.yml', 'w') as nf:
		yaml.dump(script, nf)
		
