import ruamel.yaml

vcf_files = [line.rstrip('\n') for line in open('vcfs.txt')]

yaml = ruamel.yaml.YAML()

for vcf in vcf_files:
	with open('R014890.yml') as f:
		script = yaml.load(f)
	script['analysis']['vcf'] = '/home/hpcprit1/rds/rds-who1000-wgs10k/WGS10K/data/release/20180228-A/vcf/HCM/' + vcf + '_A.vcf.gz'
	script['outputOptions']['outputPrefix'] = '/home/hpcprit1/Documents/Exomiser_Project/results/' + vcf
	with open(vcf + '.yml', 'w') as nf:
		yaml.dump(script, nf)
		
