import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# URL of the product page
url = "https://amzn.in/d/4HmAtE1"

# Send a request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)
print(response)
if response.status_code != 200:
    raise Exception(f"Failed to load page {url}")

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)

# Extract the desired data
# Example selectors - these need to be adjusted based on the actual HTML structure
title = soup.find(id='productTitle').get_text(strip=True) if soup.find(id='productTitle') else 'N/A'
price = soup.find('span', class_='a-offscreen').get_text(strip=True) if soup.find('span', class_='a-offscreen') else 'N/A'
rating = soup.find('span', class_='a-icon-alt').get_text(strip=True) if soup.find('span', class_='a-icon-alt') else 'N/A'

# Store the extracted data in a dictionary
product_data = {
    'Title': title,
    'Price': price,
    'Rating': rating
}

# Save the data to a CSV file
df = pd.DataFrame([product_data])
df.to_csv('product_details.csv', index=False)

# Save the data to a JSON file
with open('product_details.json', 'w') as json_file:
    json.dump(product_data, json_file, indent=4)

print("Data has been successfully scraped and saved to CSV and JSON")
