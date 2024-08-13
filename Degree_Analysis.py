# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

class mybarh(Axes):    # Saving for future development/simplification of adding similar axes.

    def __init__(self, series_one, series_two, title, xlabel, gridline = False, anno = False):
        self.series_one = series_one
        self.series_two = series_two
        self.title = title
        self.xlabel = xlabel
        self.gridline = gridline
        self.anno = anno
    
    

# %%
df = pd.read_csv("https://raw.githubusercontent.com/NewtonBl/Career_Analysis/main/Degree_Data.csv")
df['Future_Jobs'] = round(df.Number_of_Jobs * (1+df.Projected_Growth),0)
df = df.sort_values('Degree')

# %%
fig, ([ax1, ax2], [ax3, ax4]) = plt.subplots(2, 2, figsize=(15,8))
ax1: Axes
ax1.barh(df['Degree'], df['Future_Jobs'], color='#25faa8')
ax1.barh(df['Degree'], df['Number_of_Jobs'], color='#1f0ffc')
ax1.xaxis.set_tick_params(rotation=90)
ax1.set_title('Current and Future Jobs')
ax1.set_xlabel('Number of Jobs (Millions)')
ax1.invert_yaxis()
ax1.grid(True, axis='x', linestyle='dotted')

ax2: Axes
ax2.barh(df['Degree'], df['Projected_Growth'], color='#1f0ffc')
ax2.xaxis.set_tick_params(rotation=90)
ax2.set_xlabel('Predicted Growth by 2032')
ax2.set_title('Predicted Job Growth Rate')
ax2.invert_yaxis()
ax2.grid(True, axis='x', linestyle='dotted')


# %%
ax3: Axes
bar3 = ax3.barh(df['Degree'], df['Median_Pay_BLS'], color='#1f0ffc')
ax3.xaxis.set_tick_params(rotation=90)
ax3.set_title('Median Pay per BLS')
ax3.set_xlabel('Median Pay (USD)')
ax3.invert_yaxis()
ax3.text(5000, 2.1, 'Data Not Available')
ax3.bar_label(bar3)
ax3.set_xbound(0, 160000)

ax4: Axes
bar41 = ax4.barh(df['Degree'], df['Avg_Pay_10'], color='#25faa8')
bar42 = ax4.barh(df['Degree'], df['Avg_Pay_1'], color='#1f0ffc')
ax4.xaxis.set_tick_params(rotation=90)
ax4.set_title('Avg. 1st & 10 Year Pay per ROI Data')
ax4.set_xlabel('Average Pay (USD)')
ax4.invert_yaxis()
ax4.grid(True, axis='x', linestyle='dotted')
ax4.bar_label(bar41)
ax4.set_xbound(0, 160000)
fig.tight_layout(h_pad=5)


# %%
fig3, ax5 = plt.subplots(figsize=(7, 4))
ax5: Axes
bar5 = ax5.barh(df['Degree'], df['Required_Credits'], color='#1f0ffc')
ax5.xaxis.set_tick_params(rotation=90)
ax5.set_title('Required Credits')
ax5.set_xlabel('Approximate Required Credits')
ax5.invert_yaxis()
ax5.grid(True, axis='x', linestyle='dotted')
ax5.bar_label(bar5)

fig3.tight_layout()

plt.show()


