import pandas as pd

# read specific columns of csv file using Pandas
df = pd.read_csv("ReportLog.csv", usecols=[' Script Name', ' Automation Percentage'])

df1 = pd.read_csv("ReportLog_2510.csv", usecols=[' Script Name', ' Automation Percentage'])

dct = df1.set_index(' Script Name').T.to_dict('index')
d = dct[' Automation Percentage']
df["Automation Percentage New"] = df[' Script Name'].map(d)

df.to_csv("Diffrence.csv", index=False)

