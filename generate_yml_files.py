import ruamel.yaml
import argparse
import os

#pull vcf names from previously derived text file 
vcf_files = [line.rstrip('\n') for line in open('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/vcf_names/vcfs.txt')]

#make use of the ruamel yaml file parser
yaml = ruamel.yaml.YAML()

#request two command line arguments - the version number of the yaml template to run and a name for the run
parser = argparse.ArgumentParser()
parser.add_argument("version", help='state yaml template version in number format when running script')
parser.add_argument("run_name", help='provide a run name')
args = parser.parse_args()

#use the yaml version input to find the resepctive yaml file template 
template = '/home/ashley/Documents/Exomiser_Project/exomiser_transfer/yml_files/yml_templates/yaml_template_v' + args.version + '.yml'

#make a new directory of the run name if one does not exist already - inform user and exit if the run name have already been used
if os.path.exists('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/yml_files/' + args.run_name):
	print('a file with that run name already exists')
	exit()
else: 
	os.mkdir('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/yml_files/' + args.run_name)

#itterate through the vcf file names to create a new yaml anlysis file based on the selected template for each
for vcf in vcf_files:
	with open(template) as f:
		script = yaml.load(f)
	script['analysis']['vcf'] = '/home/hpcprit1/rds/rds-who1000-wgs10k/WGS10K/data/release/20180228-A/vcf/HCM/' + vcf + '_A.vcf.gz'
	script['outputOptions']['outputPrefix'] = '/home/hpcprit1/Documents/Exomiser_Project/results/' + vcf

#save the new yaml files in the directory created above
	with open('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/yml_files/' + args.run_name + '/' + vcf + '.yml', 'w') as nf:
		yaml.dump(script, nf)
		
