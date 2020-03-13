#script to generate a random sample of 30 / 269 HCM patients for variant interpretation

import glob
import random 

#pull all gene analysis files output from exomiser (named as patient IDs)
exomiser_file_path = glob.glob('/home/ashley/Documents/Exomiser_Project/exomiser_transfer/exomiser_output_files/' + args.run_name + '/*.html')

#create an empty list to store patient IDs
patient_IDs = []

#split the file paths to pull the individual patient IDs from the names and store in created list
for ex in exomiser_file_path:
	exomiser_files.append(ex.split('/')[8])

#create the random sample of 30 patient IDs
sampling = random.choices(exomiser_files, k=20)

#print the sample to the terminal 
print(sampling)
