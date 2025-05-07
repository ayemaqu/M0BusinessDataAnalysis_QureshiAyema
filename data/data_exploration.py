import pandas as pd

df = pd.read_excel('Analysis.xlsx')

#print header row
print(df.columns)
# Print the first 5 rows of data to understand its structure.
print(df.head(5))
# Use the type() function to view the variable (column) types in the
print(df.dtypes)

# Write a basic loop to filter rows based on a specific condition
# loop through each row
for index, row in df.iterrows():
    # go through rows for cart/checkout
    added = row['Confirmed_Added_Items']
    confirmed = row['Purchase_Confirmed']

    # use a if statement to check if that cart was abondened or not
    #if people added an item, BUT didn't checkout, print yes, otherwise no 
    if added > 0 and confirmed == 0: 
        print(f"Row {index}: Cart Abandoned → Yes")
    else:
        print(f"Row {index}: Cart Abandoned → No")
