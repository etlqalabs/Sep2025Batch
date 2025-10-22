import pandas as pd

df = pd.read_csv("Data/emp.csv",parse_dates=['doj'])

print(df['doj'])
df['doj'] = df['doj'].dt.strftime('%m-%d-%y')
print(df['doj'])
