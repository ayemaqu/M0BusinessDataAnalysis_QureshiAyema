import pandas as pd

# retrieve original data set
df = pd.read_csv('data_cart_abandonment.csv')

# fill empty cells with NA
# df.fillna('NA', inplace=True )

# Select the first 100 rows
df_sample = df.head(100)

# Save to a new CSV file 
df_sample.to_csv('data_cart_abandonment_sample.csv', index=False)



