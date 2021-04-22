import pandas as pd

df_data = pd.read_csv('LinkedIn_Data_Q1FY21.csv')
print(df_data)

print(df_data.columns)

print(df_data["Total Spent"])

nan_value = float("NaN")
df_data.replace(0.00, nan_value, inplace=True)
df_data.dropna(subset = ["Total Spent"], inplace=True)
print(df_data)

print(df_data["Total Spent"])

print(df_data.isna().sum())

print(df_data.drop_duplicates())

del df_data["Start Date (in UTC)"]
print(df_data)

print(df_data["Campaign Objective"].value_counts())

df_leads = df_data[df_data["Campaign Objective"] == "Lead generation"]

print(df_leads)
column_sum = df_leads["Clicks"].sum()
print(column_sum)

leads_cost = df_leads["Total Spent"].sum()
print(leads_cost)
print(leads_cost/column_sum)

df_visits = df_data[df_data["Campaign Objective"] == "Website visits"]

print(df_visits)
column_suma = df_visits["Clicks"].sum()
print(column_suma)

visits_cost = df_visits["Total Spent"].sum()
print(visits_cost)
print(visits_cost/column_suma)

for lab, row in df_visits.iterrows() :
    df_data["CPC"] = df_data["Total Spent"]/df_data["Clicks"]
print(df_data)


df_geo = pd.read_csv('GEO_Ad_Spend.csv')
print(df_geo)


# merge dataframes
print(df_data["Ad ID"].isin(df_geo["Ad ID"]).value_counts())

df_geo_sp = pd.merge(df_data, df_geo[["Ad ID", "Country"]], on ="Ad ID")
print(df_geo_sp)

df_geo_spend = (df_geo_sp.drop_duplicates())
print(df_geo_spend)

# to check countries listed in this column
df_country = df_geo_spend.drop_duplicates(subset=["Country"])
print(df_country)

# to replace non-country names with 'brand'
df_geo_spend["Country"] = df_geo_spend["Country"].replace(["Sandy Ono", "x"], "BRAND")
print(df_geo_spend)

# plotting visuals
import matplotlib.pyplot as plt

df_data.plot(x="Total Spent", y="Clicks", kind= 'scatter')
plt.show()

import seaborn as sns
sns.scatterplot(x="Total Spent", y="Clicks", data=df_data, hue= "Campaign Objective")
plt.show()

sns.scatterplot(x="Total Spent", y="Clicks", data=df_data, hue= "Campaign Objective", style="Campaign Status")
plt.show()

plt.barh(df_data["Campaign Status"], df_data["Total Spent"])
plt.xlabel("Total Spent")
plt.ylabel("Campaign Status")
plt.show()

plt.barh(df_geo_spend["Country"], df_geo_spend["Total Spent"])
plt.xlabel("Total Spent")
plt.ylabel("Country")
plt.show()

sns.scatterplot(x="Total Spent", y="CPC", data=df_geo_spend, hue= "Country")
plt.show()

# Using bokeh to create a interactive visualisation
from bokeh.io import output_notebook, show
from bokeh.plotting import figure, output_notebook, show
from bokeh.transform import factor_cmap

output_notebook()

df_geo_spend.Country.unique()

index_cmap = factor_cmap("Country", factors=sorted(df_geo_spend.Country.unique()))

p= figure(plot_width=600, plot_height=450, title = "Country Cost Effectiveness")
p.scatter("CPC", "Total Spent",source=df_geo_spend,fill_alpha=0.6, fill_color=index_cmap,size=10,legend="Country")
p.xaxis.axis_label ="CPC"
p.yaxis.axis_label ="Total Spent"
p.legend.location = "top right"

show(p)



























