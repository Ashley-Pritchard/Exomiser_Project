----------------------
-- Exomiser Project --
----------------------

Ashley Pritchard <br>
Last Updated: 10/03/2020 <br><br>

A3_RANKED_GENES DIRECTORY<br>
The scripts in this directory align to the third section of the results in the project write up - ranked genes. They were run in the following order:<br><br>
<strong>ranked_gene_list.py:</strong> pulls gene score data for all genes found to harbour automsomal dominant or autosomal recessive variants in the 269 HCM patient cohort. Ouputs data as csv files ordered by gene score descending. <br><br> 
<strong>variants_top_4_genes.py:</strong> findings from the ranked_gene_list.py script showed 4 genes to have notably high gene scores. This script pulls the HGVS name and resepctive patient IDs for all variants occuring in these genes for the 269 patient cohort. Data output as a csv file. 
