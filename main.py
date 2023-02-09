import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df_hh_income = pd.read_csv('Median_Household_Income_2015.csv', encoding="windows-1252")
df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

# Replace all nan with 0
df_hh_income['Median Income'] = df_hh_income['Median Income'].replace(np.nan, 0)


# --------- poverty rate by state -------- #
"""df_pct_poverty['State'].unique()

df_pct_poverty.Poverty_Pct.unique()
df_pct_poverty.Poverty_Pct.replace('-', np.nan, regex=True, inplace=True)
df_pct_poverty.Poverty_Pct = df_pct_poverty.Poverty_Pct.astype(float)

poverty = df_pct_poverty.groupby('State')['Poverty_Pct'].mean().sort_values(ascending=False)

plt.figure(figsize=(14, 4))
plt.suptitle('Poverty Rate by State in the US')
plt.ylabel('Poverty Rate', fontsize=10)
plt.xlabel('US State', fontsize=10)

for n in range(len(poverty)):
    plt.xticks(fontsize=10, rotation=90)
    plt.yticks(fontsize=14)
    plt.bar(poverty.index[n], poverty[n])

plt.show()"""

# --------- HS completion by state -------- #
"""df_pct_completed_hs.percent_completed_hs.replace('-', np.nan, regex=True, inplace=True)
df_pct_completed_hs.percent_completed_hs = df_pct_completed_hs.percent_completed_hs.astype(float)

graduation = df_pct_completed_hs.groupby('Geographic Area')['percent_completed_hs'].mean().sort_values(ascending=False)

plt.figure(figsize=(14,4))
plt.suptitle('High School Graduation Rate by US State')
plt.ylabel('High School Graduation Rate', fontsize=14)
plt.xlabel('US State', fontsize=14)

plt.xticks(fontsize=10, rotation=90)
plt.yticks(fontsize=14)
plt.scatter(graduation.index, graduation)
plt.show()"""

# --------- poverty vs hs completion -------- #
graduation_vs = df_pct_completed_hs.groupby('Geographic Area')['percent_completed_hs'].mean()
poverty_vs = df_pct_poverty.groupby('State')['Poverty_Pct'].mean()

plt.figure(figsize=(14, 3))
plt.suptitle('Poverty Rates and High School Graduation Rates', fontsize=14)
plt.xlabel('US State', fontsize=12)
plt.xticks(fontsize=10, rotation=55)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('Poverty', color='#E6232E')  # can use a HEX code
ax2.set_ylabel('Graduation', color='skyblue')  # or a named colour

ax1.plot(poverty_vs.index, poverty_vs, color='#E6232E', linewidth=3, linestyle='--')
ax2.plot(graduation_vs.index, graduation_vs, color='skyblue', linewidth=3, marker='o')

plt.show()
