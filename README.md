# Mod-0 Project: Cart abandonment

#### Business Understanding: 
- This analysis explores customer behavior during online shopping sessions, with a focus on the relationship between those who complete purchases and those who abandon their carts. The goal is to understand what factors contribute to cart abandonment and identify behavioral patterns that could help improve the user experience and boost conversion rates.
-----
### Data Lifecycle: 
<img width="230" alt="Screenshot" src="https://github.com/user-attachments/assets/c54975cb-837f-48fc-8409-09e6563488d3" />

- **Business problem:** How can we reduce cart abandonment rates and gain deeper insights into customer behavior during online shopping sessions?
- **Data collection:** The dataset used in this project was sourced from Ratul Ghosh’s Customer Cart Abandonment Analysis, which was publicly available on his GitHub repository. The data was already organized and cleaned, meaning it was structured and ready for analysis. Since it wasn’t raw or unprocessed, I was able to begin exploring and analyzing it immediately.
- **Data processing:** There were some empty cells in the dataset, which I filled in with "NA" using Excel to ensure consistency. To improve reliability and usability, I also added a few custom columns. Since the dataset is session-based, I wanted to focus more on whether customers took key actions, rather than how many times they repeated them (like viewing pages or logging in), which I considered useful but not necessary for my specific analysis.

- Here are the columns I created:
  - `added_items` This column uses an `IF` statement to check if a customer added any items to their cart. I labeled the result as `"Yes"` or `"No"`.
  - `confirmed_added_items` While not essential, I created this column to help myself. It converts the `"Yes"/"No"` values from added_items into `1` and `0` so I could more easily calculate totals in a Pivot Table.
  - `confirmed_initiated` The original dataset included a column showing how many times each customer initiated a checkout. My new column simplifies that by flagging it with a `1` if they initiated checkout at least once, or `0` if they didn’t.

  - These changes allowed me to focus on whether a customer took action at all, rather than how often — which aligned better with my goal of analyzing cart abandonment.

- **Data analysis:** In Excel, I used formulas to calculate both the cart abandonment rate and the drop-off rate. To support these calculations, I added custom columns that simplified the logic and made the formulas easier to apply and interpret.
  - I also used for loops in Python to organize and categorize customer behavior more clearly. This allowed me to take a different approach to analyzing abandonment, specifically by checking which customer groups (Target, Loyal, or Untargeted) were more likely to abandon their carts. This method helped me break the data into more meaningful segments and draw more insightful conclusions.
- **Data presentation:** To communicate my findings, I would create a PowerPoint presentation supported by charts I built during my analysis. These visualizations — including pie charts — helped illustrate the different types of customers (Target, Loyal, Untargeted) and how each group behaved in terms of cart abandonment. The visuals make it easier to explain key patterns and support potential solutions, such as improving the checkout process or retargeting segments that are more likely to abandon their carts.


---

#### Excel Analysis: 
- In Excel, I analyzed the cart abandonment rate using the formula: `(1 - (# of purchases / # of carts created)) * 100`
  - This calculation reveals the percentage of customers who added items to their carts but didn’t complete the purchase. Understanding cart abandonment is essential in e-commerce, as it helps identify potential issues in the checkout process. Common causes of abandonment can include unexpected shipping costs, a complex or confusing checkout experience, or a lack of trust in the website. By identifying these pain points, businesses can make improvements that reduce friction and increase conversions.
- I also calculated the checkout drop-off rate using the formula: `(1 - (# of purchases confirmed / # of checkouts initiated)) * 100`
  - This metric shows when and where customers lose interest or exit the process after initiating checkout. It provides a deeper layer of insight that goes hand-in-hand with cart abandonment, especially when customers start to check out but never complete the purchase. Together, these metrics help pinpoint where the user journey breaks down. 


#### Python Analysis: 
- In Python, I used for loops to explore customer behavior more directly. One loop checked which customers added items to their carts, and whether they completed the purchase or abandoned it. Another loop categorized customer sessions into three clear groups:
  - _Purchased_: Customer added items to cart and confirmed a purchase
  - _Abandoned_: Customer added items but didn’t complete the checkout
  - _Inactive_: Customer didn’t add anything and didn’t attempt to check out

- I then created a pie chart to visually show the distribution of customer types — Target, Loyal, and Untargeted — and how they behaved in terms of cart activity. To verify that my for loops were working correctly, I compared the Python output to the calculations I made in Excel. This helped me ensure that my custom logic (like counting added items or confirmed purchases) matched the actual values in the dataset.
- I created two separate pie charts for different purposes:
  - Graph 1(figure 1): Shows the distribution of customer segments: `0 = Target, 1 = Loyal, 2 = Untargeted`
  - Graph 2(figure 2): Shows the outcome of the session: `Purchased, Abandoned, or Inactive`
    - The second graph is based on categories I created in Python using logic from the original columns. By checking whether customers added items and confirmed purchases, I was able to reclassify behavior to better analyze who completed the customer journey and who dropped off.
<img width="270" alt="Screenshot" src="https://github.com/user-attachments/assets/eceb1938-5d09-4cf4-ade2-fca59d6cfa4e" />
Figure 1
<img width="270" alt="Screenshot" src="https://github.com/user-attachments/assets/58a6112d-898b-4355-af2c-353c39c5bde2" />
Figure 2

#### Data types:
- The dataset contains both numeric and categorical data types. The numeric columns represent quantitative data, such as the number of items added to a cart, the number of pages viewed, or the number of checkout confirmations. These are discrete values because they represent counts — whole numbers, not continuous measurements.
- At the same time, the dataset relies heavily on categorical (qualitative) data. For example, the `Customer_Segment_Type` column includes labels like Target, Loyal, and Untargeted, and new categories I created (such as Purchased, Abandoned, and Inactive) are also qualitative. These categories are important for grouping and interpreting customer behavior patterns. Because the analysis involves both numerical metrics and labeled categories, this dataset is a mix of quantitative and qualitative data types.

#### Conclusion: 3 things I learned this Module 
1. I learned how to work with real-world data and organize it in a way that supports meaningful analysis. I also realized how easy it is to “scope creep” when you're curious — I had to remind myself to stay focused on answering my specific business problem.
2. If I had more time, I would explore creating additional graphs, and experiment with building new input columns directly in Excel. I’d like to connect those Excel inputs to Python to create visuals based on both tools.
3. I learned how to use for loops in Python to iterate through rows and perform logic-based calculations. This helped me translate raw data into categories like “Purchased” or “Abandoned,” and gave me more control over the structure of my analysis.
