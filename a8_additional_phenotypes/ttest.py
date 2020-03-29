#script to run ttests between general analysis vs familial and those cases with additional phenotype data
import glob
import pandas as pd 
import statistics
from scipy.stats import ttest_ind 
import matplotlib.pyplot as plt

#add the three analysis variant outputs to list
general = glob.glob('general/*variants.tsv')
family = glob.glob('family/*csv')
pheno = glob.glob('pheno/*tsv')

#concatenate all variant files for each sample into pandas dataframes
df_general = pd.concat((pd.read_csv(g_file, sep='\t') for g_file in general), ignore_index=True)
df_family = pd.concat((pd.read_csv(f_file, sep=',') for f_file in family), ignore_index=True)
df_pheno = pd.concat((pd.read_csv(p_file, sep='\t') for p_file in pheno), ignore_index=True)

################################
### exomiser combined scores ###
################################

#save combined exomiser scores for each to list 
combined_score_general = df_general['EXOMISER_GENE_COMBINED_SCORE'].tolist()
combined_score_family = df_family['Combined_Score_Exomiser'].tolist()
combined_score_pheno = df_pheno['EXOMISER_GENE_COMBINED_SCORE'].tolist()

#calculate the mean value for each combined exomiser scores 
mean_combined_score_general = statistics.mean(combined_score_general)
mean_combined_score_family = statistics.mean(combined_score_family)
mean_combined_score_pheno = statistics.mean(combined_score_pheno)

#assign the x and y values for plotting the mean combined score for the general vs familiar exomiser analyses as a barchart 
x = ('General', 'Familial')
y = (mean_combined_score_general, mean_combined_score_family)
#plot the barchart
plt.bar(x, y, color = 'orangered', edgecolor = 'black')
plt.xticks(rotation=30)
plt.xlabel('Analysis Type',labelpad=10)
plt.ylabel('Average Exomiser Combined Score', labelpad=10)
plt.ylim((0, 0.335)) 
plt.title('Average Exomiser Combined Score for General and \n Familial Analysis', pad=10)
plt.show()

#assign the x and y values for plotting the mean combined score for the general vs personalised exomiser analyses as a barchart 
x = ('General', 'Personalised')
y = (mean_combined_score_general, mean_combined_score_pheno)
#plot the barchart
plt.bar(x, y, color = 'orangered', edgecolor = 'black')
plt.xticks(rotation=30)
plt.xlabel('Analysis Type',labelpad=10)
plt.ylabel('Average Exomiser Combined Score', labelpad=10)
plt.ylim((0, 0.335)) 
plt.title('Average Exomiser Combined Score for General and \n Personalised Analysis', pad=10)
plt.show()

#calculate ttests 
ttest_cs_general_family = ttest_ind(combined_score_general, combined_score_family, equal_var=False, nan_policy='omit')
ttest_cs_general_pheno = ttest_ind(combined_score_general, combined_score_pheno, equal_var=False, nan_policy='omit')

####################
## variant counts ##
####################

#create an exmpty list to append general variant count  
general_variant_count = []

#iterate through files and append the count of variants >0.8 per patient to empty list 
for g in general:
	df = pd.read_csv(g, sep='\t')
	count = 0
	for index, row in df.iterrows():
		if row[31] >= 0.8 and 'HLA-B' not in str(row[9]) and '2814_2816del' not in str(row[9]):
			count += 1			
	if count > 0:
		general_variant_count.append(count)
	else:
		general_variant_count.append(0)

#create an exmpty list to append general variant count  
family_variant_count = []

#iterate through files and append the count of variants >0.8 per patient to empty list 
for f in family:
	df = pd.read_csv(f, sep=',')
	count = 0
	for index, row in df.iterrows():
		if row[9] >= 0.8 and 'HLA-B' not in str(row[0]) and '2814_2816del' not in str(row[0]):
			count += 1			
	if count > 0:
		family_variant_count.append(count)
	else:
		family_variant_count.append(0)

#create an exmpty list to append general variant count  
pheno_variant_count = []

#iterate through files and append the count of variants >0.8 per patient to empty list 
for p in pheno:
	df = pd.read_csv(p, sep='\t')
	count = 0
	for index, row in df.iterrows():
		if row[31] >= 0.8 and 'HLA-B' not in str(row[9]) and '2814_2816del' not in str(row[9]):
			count += 1			
	if count > 0:
		pheno_variant_count.append(count)
	else:
		pheno_variant_count.append(0)

##calculate the mean values of variants over 0.8 per patient 
mean_general_variant_count = statistics.mean(general_variant_count)
mean_family_variant_count = statistics.mean(family_variant_count)
mean_pheno_variant_count = statistics.mean(pheno_variant_count)

#assign the x and y values for plotting the mean variant count for the general vs familiar exomiser analyses as a barchart 
x = ('General', 'Familial')
y = (mean_general_variant_count, mean_family_variant_count)
#plot the barchart
plt.bar(x, y, color = 'orangered', edgecolor = 'black')
plt.xticks(rotation=30)
plt.xlabel('Analysis Type',labelpad=10)
plt.ylabel('Average Variant Count', labelpad=10)
plt.ylim((0, 2.5)) 
plt.title('Average Count of Variants with a Combined Score of more \n than 0.8 for General and Familial Analysis', pad=10)
plt.show()

#assign the x and y values for plotting the mean variant count for the general vs personalised exomiser analyses as a barchart 
x = ('General', 'Personalised')
y = (mean_general_variant_count, mean_pheno_variant_count)
#plot the barchart
plt.bar(x, y, color = 'orangered', edgecolor = 'black')
plt.xticks(rotation=30)
plt.xlabel('Analysis Type',labelpad=10)
plt.ylabel('Average Exomiser Combined Score', labelpad=10)
plt.ylim((0, 2.75)) 
plt.title('Average Count of Variants with a Combined Score of more \n than 0.8 for General and Personalised Analysis', pad=10)
plt.show()

#ttests comparing the variant counts 
ttest_count_general_family = ttest_ind(general_variant_count, family_variant_count, equal_var=False, nan_policy='omit')
ttest_count_general_pheno = ttest_ind(general_variant_count, pheno_variant_count, equal_var=False, nan_policy='omit')

#################################################################################################################################################################


#print the results of the ttests to the terminal 
print('mean combined score for general analysis = ', mean_combined_score_general)
print('mean combined score for familial analysis = ', mean_combined_score_family)
print('mean combined score for personalised analysis = ', mean_combined_score_pheno)
print('ttest results combined score general vs family: ', ttest_cs_general_family)
print('ttest results combined score general vs pheno: ', ttest_cs_general_pheno)
print('ttest results variant count general vs family: ', ttest_count_general_family)
print('ttest results variant count general vs pheno: ', ttest_count_general_pheno)

