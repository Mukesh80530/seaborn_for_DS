import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars_data1 = pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
cars_data2 = cars_data1.copy()
cars_data2.dropna(axis=0, inplace=True)


f, (ax_box, ax_hist) = plt.subplots(2, gridspec_kw={"height_ratios": (.15, .85)})
sns.boxplot(cars_data2['Price'], ax=ax_box)
sns.distplot(cars_data2['Price'], ax=ax_hist, kde=False)
plt.show()