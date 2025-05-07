import pandas as pd
import matplotlib.pyplot as plt

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
    added_to_cart = row['Confirmed_Added_Items']
    confirmed_purchase = row['Purchase_Confirmed']

    # use a if statement to check if that cart was abondened or not
    #if people added an item, BUT didn't checkout, print yes, otherwise no 
    if added_to_cart > 0 and confirmed_purchase == 0: 
        print(f"Row {index}: Cart Abandoned → Yes")
    else:
        print(f"Row {index}: Cart Abandoned → No")

# PIE CHART 
# Count how many customers fall into each segment 'Customer_Segment_Type' 
# where 0 = Target, 1 = Loyal, 2 = Untargeted
counts = df["Customer_Segment_Type"].value_counts()
'''
# print(counts)
Customer_Segment_Type
1    44
0    42
2    14
'''

#Labels
counts.index = ['Target', 'Loyal', 'Untargeted']
#create the pie chart
counts.plot(kind='pie',
            autopct='%1.1f%%',
            figsize=(6,6))
#the title
plt.title("Customer Segment distributation")
#makes the pie chart a circle
plt.axis('equal')
#shows the chart
plt.show()