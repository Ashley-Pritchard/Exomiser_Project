----------------------
-- Exomiser Project --
----------------------

Ashley Pritchard <br>
Last Updated: 10/03/2020 <br><br>

A1_DATA_DISTRIBUTION DIRECTORY<br>
The scripts in this directory align to the first section of the results in the project write up - data distribution.<br><br>
<strong>variant_count.py:</strong> following analysis using the exomiser tool, provides a count of the number of autosomal dominant and autosomal recessive variants that passed filtering per patient and displays data as a boxplot. Prints the median to the terminal. <br><br>
<strong>gene_count.py:</strong> provides a count of the number of genes which harbour autosomal dominant and autosomal recessive variants that passed Exomiser filtering and displays results as a boxplot. Meidan values printed tp the terminal. <br><br>
<strong>histogram_variant_score:</strong> generates a histogram to show the distribution of variant scores calculated for all autosomal dominant and autosomal recessive variants that passed Exomiser filtering for all 269 patient VCFs analysed. <br><br>
<strong>histogram_gene_score:</strong> generates a histogram to show the distribution of gene scores calculated for genes found to harbour an autosomal dominant or autosomal recessive variant that passed Exomiser filtering for all 269 patient VCFs analysed. <br><br>
<strong>histogram_combined_score:</strong> generates a histogram to show the distribution of combined scores calculated for all autosomal dominant and autosomal recessive variants that passed Exomiser filtering for all 269 patient VCFs analysed. This score is calulated from the respecitve variant and gene scores. <br><br>
