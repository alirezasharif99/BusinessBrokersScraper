import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_page_content(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page: {url}")
        return None

def parse_listing_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    listings = []
    
    for listing in soup.find_all('li', class_='summary-list-item'):
        business_name = listing.find('h3', class_='summary-title').text.strip() if listing.find('h3', class_='summary-title') else "N/A"
        location = listing.find('small', class_='font-15px').text.strip() if listing.find('small', class_='font-15px') else "N/A"
        #price = listing.find('span', class_='doller-font-12px').text.strip() if listing.find('span', class_='doller-font-12px') else "N/A"
        price_element = listing.find('span', class_='doller-font-12px')
        if price_element:
            price = price_element.next_sibling.strip() if price_element.next_sibling else "N/A"
        else:
            price = "N/A"

        description = listing.find('p', class_='summary-text').text.strip() if listing.find('p', class_='summary-text') else "No description available"
        size = "N/A"
        for label in listing.find_all('p', class_='mb-1 font-bold'):
            if 'Size (sq ft)' in label.text:
                size_value = label.find_next('span', class_='text-black float-right bg-white')
                if size_value:
                    size = size_value.text.strip()
        monthly_rent = "N/A"
        for rent_label in listing.find_all('p', class_='mb-1 font-bold'):
            if 'Monthly Rent/Sq. Ft.' in rent_label.text:
                rent_value_span = rent_label.find_next('span', class_='float-right bg-white')
                if rent_value_span:
                    monthly_rent = rent_value_span.text.strip().replace("$", "").replace(",", "")
                break
        print(monthly_rent)
        gross_revenue = "N/A"
        listings.append({
            'Business Name': business_name,
            'Location': location,
            'Price': price,
            'Size (sq ft)': size,
            'Monthly Rent/Sq. Ft.': monthly_rent,
            'Gross Revenue': gross_revenue,
            'Description': description
        })
    return listings

def scrape_business_listings(base_url, pages):
    all_listings = []
    for page in range(1, pages + 1):
        url = f"{base_url}&page={page}"
        content = get_page_content(url)
        if content:
            listings = parse_listing_page(content)
            all_listings.extend(listings)
    return all_listings

def save_to_csv(listings, filename='business_listings.csv'):
    df = pd.DataFrame(listings)
    df.to_csv(filename, index=False)
    print(f"Saved {len(listings)} listings to {filename}")

# Example usage:
base_url = 'https://www.findbusinesses4sale.com/search/ontario/businesses-for-sale-in-toronto/?searchId=66575b771c5a4361'
pages = 3  # Number of pages to scrape (adjust as necessary)
listings = scrape_business_listings(base_url, pages)
save_to_csv(listings)
