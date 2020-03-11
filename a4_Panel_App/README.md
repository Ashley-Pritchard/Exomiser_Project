----------------------
-- Exomiser Project --
----------------------

Ashley Pritchard <br>
Last Updated: 11/03/2020 <br><br>

A4_PANEL_APP DIRECTORY<br>
The scripts in this directory align to the fourth section of the results in the project write up - PanelApp Correlation:<br><br>
<strong>count_patients_red_amber_PanelApp_variants.py:</strong> counts the number of patients who have variants with an Exomiser combined score of >0.9 in red or amber HCM PanelApp genes.<br><br>
<strong>PanelApp_genes_pheno_scores.py</strong> takes in a csv file of the genes found to harbour at least one passed variant based on Exomiser analysis of the 269 HCM patient VCFs. The file details the Exomiser assigned gene score for each gene, whether it is present on the HCM PanelApp gene panel, and, if so, whether it is classified as red, amber or green. The script calculates the mean gene score for each the non, red, amber and green catagories and plots findings as a bar plot. Student's ttests are also performed between all possible catagories to assess whether differences are statistically significant. 
