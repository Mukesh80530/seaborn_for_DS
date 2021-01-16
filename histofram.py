import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars_data1 = pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
cars_data2 = cars_data1.copy()
cars_data2.dropna(axis=0, inplace=True)

# histogram with default kernel density estimate
# sns.distplot(cars_data2['Age'])

# histogram without kernel density estimate
# sns.distplot(cars_data2['Age'], kde=False)

# Histogram with fixed no. of bins
sns.distplot(cars_data2['Age'], kde=False, bins=5)

plt.show()