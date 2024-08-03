import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine

#Extraction
pages = [page for page in range(1, 11)]

names = []
new_prices = []
old_prices = []
discounted = []

for page_num in pages:
    url = f'https://www.jumia.com.ng/catalog/?q=laptops&page={page_num}#catalog-listing'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    listings = soup.find_all('div', class_ = 'info')
    
    for listing in listings:
        
        name = listing.find('h3', class_ = 'name').text
        names.append(name)
        
        prices = listing.find("div", class_ = "prc").text
        new_prices.append(prices)
        
        if listing.find("div", class_ = "s-prc-w"):
            price = listing.find("div", class_ = "old").text
            old_prices.append(price)
            
            discount = listing.find("div", class_ = "bdg _dsct _sm").text
            discounted.append(discount)
        else:
            old_prices.append('None')
            discounted.append('None')
            
data = {'Name': names, 'New_Price': new_prices, 'Old_prices': old_prices, 'Discounted': discounted}
all_laptops_df = pd.DataFrame(data)


# Transformations

# Function to clean price values
def clean_price(price):
    if pd.isna(price):
        return None
    return price.replace('₦', '').replace(',', '').strip()

# Clean 'New_Price' and 'Old_prices' columns
all_laptops_df['New_Price'] = all_laptops_df['New_Price'].apply(clean_price)
all_laptops_df['Old_prices'] = all_laptops_df['Old_prices'].apply(clean_price)


# loading

db_url = f"postgresql://{db_params['username']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"

engine = create_engine(db_url)

with engine.connect() as conn:
    all_laptops_df.to_sql('jumia_laptops', conn, index=False, if_exists='replace')
    
print('Data loaded successfully')
        
        