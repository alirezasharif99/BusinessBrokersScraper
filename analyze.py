import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV file
file_path = 'business_listings.csv'
listings_df = pd.read_csv(file_path)

# Define categories and associated keywords
categories = {
    'Restaurant': ['restaurant', 'dining', 'cafe', 'bistro', 'eatery'],
    'Healthcare': ['clinic', 'physiotherapy', 'medical', 'healthcare'],
    'Retail': ['retail', 'shop', 'store', 'boutique'],
    'Service': ['laundry', 'service', 'repair', 'cleaning'],
    'Manufacturing': ['manufacturing', 'production', 'factory', 'plant'],
    'Other': []
}

# Function to categorize based on description
def categorize(description):
    for category, keywords in categories.items():
        if any(keyword in description.lower() for keyword in keywords):
            return category
    return 'Other'

# Apply categorization
listings_df['Category'] = listings_df['Description'].apply(categorize)

# Replace empty strings and non-numeric values with NaN
listings_df['Price'] = listings_df['Price'].str.replace(',', '').str.replace('$', '').replace('', pd.NA)

# Convert to float, forcing errors to NaN
listings_df['Price'] = pd.to_numeric(listings_df['Price'], errors='coerce')

# Calculate average price per category
price_trends = listings_df.groupby('Category')['Price'].mean().sort_values(ascending=False)

# Plot the pricing trends by category
plt.figure(figsize=(10, 6))
price_trends.plot(kind='bar', color='skyblue')
plt.title('Average Price by Business Category')
plt.xlabel('Category')
plt.ylabel('Average Price ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save and display the plot
plt.savefig('average_price_by_category.png')
plt.show()


