import pandas as pd

# Load the newly uploaded CSV file
file_path ='business_listings.csv'
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

# Save the categorized listings to a new CSV file
categorized_file_path = 'categorized_business_listings.csv'
listings_df.to_csv(categorized_file_path, index=False)




