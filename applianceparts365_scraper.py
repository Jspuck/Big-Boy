import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://applianceparts365.com/dishwasher-bottom-door-gasket-for-frigidaire-809006501-1058857"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the price element
price_element = soup.select_one("#price-value-1058857")

# Extract the price text
price_text = price_element.text.strip()

print(price_text)  # Output: $4.64