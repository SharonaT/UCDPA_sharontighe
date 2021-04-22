import geopandas as gpd

ireland = gpd.read_file('counties.shp')
ireland.head(3)
ireland.plot(column='NAME_TAG', figsize=(8,8));

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

boyle = pd.read_csv("Tourist Attractions in Boyle.csv")
boyle.head()

plt.subplots(figsize =(8,7))
sns.scatterplot(data=boyle, y="Latitude", x="Longitude", hue="Name")

ireland = gpd.read_file('counties.shp')
ireland.plot(legend=True, figsize=(12,12))
sns.scatterplot(data=boyle, y="Latitude", x="Longitude", hue="Name")
plt.xlim(-9.0, -8.0)
plt.ylim(53.7, 54.6);


