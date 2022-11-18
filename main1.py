'''import pandas as pd #Returns only 60 rows
df = pd.read_csv('akpo_fpso.csv')
print(df)'''

'''import pandas as pd #Returns ALL the rows and colums
df = pd.read_csv('akpo_fpso.csv')
print(df.to_string())'''

'''import pandas as pd
print(pd.options.display.max_rows)'''

'''import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('akpo_fpso.csv')
print(df)'''

'''import pandas as pd
df = pd.read_csv('akpo_fpso.csv')
#print(df.head(10))
print(df.info()) #Gives info about the csv file being analysed.'''

'''import pandas as pd
df = pd.read_csv('akpo_fpso.csv')
new_df = df.dropna()
print(new_df.to_string())'''

https://github.com/Nnamaka001/numpy_test.git