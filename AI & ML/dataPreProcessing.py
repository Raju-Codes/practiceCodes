import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn import preprocessing

#Reading a file
df = pd.read_csv('AI & ML/diabetes.csv')

#to Print the top 5 values
print(df.head())
# to print the last 5 values
print(df.tail())
#to Get the summary on data
print(df.info())

print(df.shape[0])