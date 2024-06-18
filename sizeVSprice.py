import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Load the CSV file
file_path = 'categorized_business_listings.csv'
listings_df = pd.read_csv(file_path)

# Remove rows with missing price or size
listings_df = listings_df.dropna(subset=['Price', 'Size (sq ft)'])

# Convert Price and Size (sq ft) to numeric
listings_df['Price'] = listings_df['Price'].str.replace(',', '').astype(float)
listings_df['Size (sq ft)'] = listings_df['Size (sq ft)'].str.replace(',', '').astype(float)

# Plot Size vs. Price
plt.figure(figsize=(10, 6))
sns.scatterplot(data=listings_df, x='Size (sq ft)', y='Price', hue='Category', palette='viridis')
plt.title('Size vs. Price of Businesses')
plt.xlabel('Size (sq ft)')
plt.ylabel('Price ($)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save and display the plot
plt.savefig('size_vs_price.png')
plt.show()
