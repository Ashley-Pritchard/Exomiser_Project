import pandas as pd 
from scipy.stats import ttest_ind 
import matplotlib.pyplot as plt

df = pd.read_csv('gene_score_panel_app_for_ttest.csv', sep=',')

mean_absent = df['absent'].mean()
mean_red = df['red'].mean()
mean_amber = df['amber'].mean()
mean_green = df['green'].mean()

absent = df['absent'].tolist()
red = df['red'].tolist()
amber = df['amber'].tolist()
green = df['green'].tolist()

ttest_absent_red = ttest_ind(absent, red, equal_var=False, nan_policy='omit')
ttest_absent_amber = ttest_ind(absent, amber, equal_var=False, nan_policy='omit')
ttest_absent_green = ttest_ind(absent, green, equal_var=False, nan_policy='omit')
ttest_red_amber = ttest_ind(red, amber, equal_var=False, nan_policy='omit')
ttest_red_green = ttest_ind(red, green, equal_var=False, nan_policy='omit')
ttest_amber_green = ttest_ind(amber, green, equal_var=False, nan_policy='omit')


print(mean_absent, mean_red, mean_amber, mean_green)
print('ttest results \n' 'absent vs red: ', ttest_absent_red, '\n absent vs amber: ', ttest_absent_amber, '\n absent vs green: ', ttest_absent_green, '\n red vs amber: ', ttest_red_amber, '\n red vs green: ', ttest_red_green, '\n amber vs green: ', ttest_amber_green)

x = ('Non PanelApp', 'Red', 'Amber', 'Green')
y = (mean_absent, mean_red, mean_amber, mean_green)

plt.bar(x, y, color = 'orangered', edgecolor = 'black')
plt.xticks(rotation=30)
plt.xlabel('PanelApp Gene Status',labelpad=10)
plt.ylabel('Average Gene Score', labelpad=10)
plt.title('Average Gene Score for Non-, Red-, Amber- \n and Green HCM PanelApp Genes', pad=10)
plt.show()
