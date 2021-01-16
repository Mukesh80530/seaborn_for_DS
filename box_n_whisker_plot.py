import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars_data1 = pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
cars_data2 = cars_data1.copy()
cars_data2.dropna(axis=0, inplace=True)

# sns.boxplot(y=cars_data2['Price'])

# Box and whiskers plot for numerical vs categorical variable
# sns.boxplot(x=cars_data2['FuelType'], y=cars_data2['Price'])

# Grouped box and whisker plot of price vs FuelType and Automatic
sns.boxplot(x=cars_data2['FuelType'], y=cars_data2['Price'], hue="Automatic", data=cars_data2)

plt.show()