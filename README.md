# Mod-0 Project: Cart abandonment

#### Business Understanding: 
- This analysis explores customer behavior during online shopping sessions, with a focus on the relationship between those who complete purchases and those who abandon their carts. The goal is to understand what factors contribute to cart abandonment and identify behavioral patterns that could help improve the user experience and boost conversion rates.

#### Data Lifecycle: 
<img width="230" alt="Screenshot" src="https://github.com/user-attachments/assets/c54975cb-837f-48fc-8409-09e6563488d3" />

- **Business problem:** How can we reduce cart abandonment rates and gain deeper insights into customer behavior during online shopping sessions?
- **Data collection:** The dataset used in this project was sourced from Ratul Ghosh’s Customer Cart Abandonment Analysis, which was publicly available on his GitHub repository. The data was already organized and cleaned, meaning it was structured and ready for analysis. Since it wasn’t raw or unprocessed, I was able to begin exploring and analyzing it immediately.
- **Data processing:** There were some empty cells in the dataset, which I filled in with "NA" using Excel to ensure consistency. To improve reliability and usability, I also added a few custom columns. Since the dataset is session-based, I wanted to focus more on whether customers took key actions, rather than how many times they repeated them (like viewing pages or logging in), which I considered useful but not necessary for my specific analysis.

Here are the columns I created:
- `added_items` This column uses an `IF` statement to check if a customer added any items to their cart. I labeled the result as `"Yes"` or `"No"`.
- `confirmed_added_items` While not essential, I created this column to help myself. It converts the `"Yes"/"No"` values from added_items into `1` and `0` so I could more easily calculate totals in a Pivot Table.
- `confirmed_initiated` The original dataset included a column showing how many times each customer initiated a checkout. My new column simplifies that by flagging it with a `1` if they initiated checkout at least once, or `0` if they didn’t.

These changes allowed me to focus on whether a customer took action at all, rather than how often — which aligned better with my goal of analyzing cart abandonment.





