import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes_to_excel(url, excel_file_path):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes_divs = soup.find_all('div', class_='quote')
        
        quotes = []
        for quote_div in quotes_divs:
            text = quote_div.find('span', class_='text').text
            author = quote_div.find('small', class_='author').text
            quotes.append({'text': text, 'author': author})
        
        # Convert the list of dictionaries to a pandas DataFrame
        quotes_df = pd.DataFrame(quotes)
        
        # Save the DataFrame to an Excel file
        quotes_df.to_excel(excel_file_path, index=False)
        
        print(f"Data saved to {excel_file_path}")
    else:
        print("Failed to retrieve the webpage")

# Usage example
url = 'http://quotes.toscrape.com'
excel_file_path = 'quotes.xlsx'  # Specify your desired path and file name
scrape_quotes_to_excel(url, excel_file_path)
