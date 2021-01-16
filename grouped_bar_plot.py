import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars_data1 = pd.read_csv('Toyota.csv', index_col=0, na_values=["??","????"])
cars_data2 = cars_data1.copy()
cars_data2.dropna(axis=0, inplace=True)

# Frequency distribution of fuel type of the cars
sns.countplot(x="FuelType", data=cars_data2, hue="Automatic")

plt.show()