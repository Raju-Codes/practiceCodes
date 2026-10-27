import pandas as pd
df = pd.read_csv("diabetes.xlsx - diabetes.csv.csv")
print(df.head())

print(df.info())


print(df.tail())

print("Total Columns",df.shape[0])
print("Total Rows",df.shape[1])