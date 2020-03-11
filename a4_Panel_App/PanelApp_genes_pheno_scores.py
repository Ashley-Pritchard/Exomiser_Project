#script to calculated the mean Exomiser gene score for the following catagories of genes found to harbour at least one variant in the 269 HCM patient cohort: (1) those not part of the HCM PanelApp gene panel, (2) red HCM PanelApp genes, (3) amber PanelApp genes and (4) green PanelApp genes; and plot findings as a barchart. A ttest is also performed for all possible combinations of gene catagories to assess whether differences in gene scores are statistically significant. 
import pandas as pd 
from scipy.stats import ttest_ind 
import matplotlib.pyplot as plt

#a csv file noting the genes, their gene scores and PanelApp catagories is available and stored in the same directory as the script.
#read csv in as pandas datafram 
df = pd.read_csv('gene_score_panel_app_for_ttest.csv', sep=',')

#calculate the mean value for each of the PanelApp catagories and assign to variables 
mean_absent = df['absent'].mean()
mean_red = df['red'].mean()
mean_amber = df['amber'].mean()
mean_green = df['green'].mean()

#save the individual gene scores for each catagory to lists 
absent = df['absent'].tolist()
red = df['red'].tolist()
amber = df['amber'].tolist()
green = df['green'].tolist()

#perform ttests between the catagories 
ttest_absent_red = ttest_ind(absent, red, equal_var=False, nan_policy='omit')
ttest_absent_amber = ttest_ind(absent, amber, equal_var=False, nan_policy='omit')
ttest_absent_green = ttest_ind(absent, green, equal_var=False, nan_policy='omit')
ttest_red_amber = ttest_ind(red, amber, equal_var=False, nan_policy='omit')
ttest_red_green = ttest_ind(red, green, equal_var=False, nan_policy='omit')
ttest_amber_green = ttest_ind(amber, green, equal_var=False, nan_policy='omit')

#print the results of the ttests to the terminal 
print('ttest results \n' 'absent vs red: ', ttest_absent_red, '\n absent vs amber: ', ttest_absent_amber, '\n absent vs green: ', ttest_absent_green, '\n red vs amber: ', ttest_red_amber, '\n red vs green: ', ttest_red_green, '\n amber vs green: ', ttest_amber_green)

#assign the x and y values for plotting the mean gene score for the PanelApp catagories as a barchart 
x = ('Non PanelApp', 'Red', 'Amber', 'Green')
y = (mean_absent, mean_red, mean_amber, mean_green)

#plot the barchart
plt.bar(x, y, color = 'orangered', edgecolor = 'black')
plt.xticks(rotation=30)
plt.xlabel('PanelApp Gene Status',labelpad=10)
plt.ylabel('Average Gene Score', labelpad=10)
plt.title('Average Gene Score for Non-, Red-, Amber- \n and Green HCM PanelApp Genes', pad=10)
plt.show()
