----------------------
-- Exomiser Project --
----------------------

Ashley Pritchard <br>
Last Updated: 09/03/2020 <br><br>

RUN EXOMISER DIRECTORY<br>

Exome data for the 269 HCM patients included in this study was provided by the NIHR BioResource and stored on the CSD3 Cambridge server. In line with regulations, the VCFs were not removed from the server and all analysis was performed remotely over an ssh client. The resultant exomiser output files were then transferred for local analysis using rsync. The scripts in this directory were ran in the following order in the workflow: <br><br> 
<strong>pull_vcfs_patient_IDs.py:</strong> pulls the 269 hypertrophic cardiomyopathy patient IDs from the CSD3 and saves them as a text file for reference in later analysis <br><br>
<strong>yml_template.yml:</strong> an individual yml file is required for each of the patient VCFs for analysis; this file provides the template settings for each <br><br>
<strong>generate_yml_files.py:</strong> uses the text file of VCF IDs and yml template to generate an individual yml file for each patient VCF to be analysed <br><br>
