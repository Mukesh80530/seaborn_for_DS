import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars_data1 = pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
cars_data2 = cars_data1.copy()
cars_data2.dropna(axis=0, inplace=True)
# print(cars_data2.shape)

# sns.set(style="darkgrid")
# sns.regplot(x=cars_data2['Age'], y=cars_data2['Price'])
# sns.regplot(x=cars_data2['Age'], y=cars_data2['Price'], fit_reg=False)
# sns.regplot(x=cars_data2['Age'], y=cars_data2['Price'], marker="*",fit_reg=False)
# plt.show()

# Another method by thired variable
sns.lmplot(x="Age", y="Price", data=cars_data2, fit_reg=False, hue='FuelType', legend=True, palette="Set1")
plt.show()