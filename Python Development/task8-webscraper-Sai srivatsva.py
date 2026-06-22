import requests
from bs4 import BeautifulSoup
import csv

def optimized_scraper(url, output_filename="scraped_data.csv"):
    with requests.Session() as session:
        try:
            print(f"Fetching data from {url}...")
            response = session.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error: Network issue occurred - {e}")
            return

    soup = BeautifulSoup(response.text, 'html.parser')

    with open(output_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write CSV Header
        writer.writerow(['Title', 'Price'])

        items = soup.find_all('article', class_='product_pod')
        
        if not items:
            print("Error: Could not find target elements. The website structure may have changed.")
            return
            
        for item in items:
            title_tag = item.h3.a
            title = title_tag.get('title') if title_tag else "No Title"
            
            price_tag = item.find('p', class_='price_color')
            price = price_tag.text.strip() if price_tag else "No Price"
            
            writer.writerow([title, price])

    print(f"Success! Extracted {len(items)} items and saved to '{output_filename}'.")

if __name__ == "__main__":
    print("--- Optimized Web Scraper ---")
    
    target_url = "https://books.toscrape.com/"
    
    optimized_scraper(target_url)