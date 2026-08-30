import pandas as pd

# to print series type of data.
s= pd.Series(["Raju","27","raju@gmail.com","Bangalore Marathalli","QHS3278GHS",12345],index=['Name','Age','Mail','address','GST','sellerID'])
print(s)

# to print data in rows and column format
data = {
    "Name":["Rajesh", "Bob"],
    "Age":[23,25],
    "Mail" :["rajesh@gmail.com","bob@gmail.com"],
    "Address":["Bangalore", "Andhra Pradesh"],
    "GST":["TYDG123456TY","HDFT736212GG"],
    "sellerID":[64237,3217]
}

df = pd.DataFrame(data)
print(df)

# Selecting rows and columns in Pandas
print("Selecting rows and columns")
print(df[['Name',"Age"]])

# To select rows in pandas
print("To select rows in pandas")
print(df.iloc[0])

# To print the range of Rows
print(df[0:2])
print("df.iloc[0:2]")
print(df[(df["Age"]>24 & (df["Age"]<26))])

