# Extracting Data using Beautifulsoup + Requests

# Project Scope:
'''
Top Business School Data
- Entrance Average
- Required / Recommended Classes
- Application Deadlines

BeautifulSoup + Request integration
'''
# END OF PROJECT Scope

# import statements
from bs4 import BeautifulSoup # Install command: python3 -m pip install beautifulsoup4
import requests # Install command: python3 -m pip install requests
# END OF IMPORTS

# URL to scrape data from Quene's website
url = "https://www.queensu.ca/admission/applying/competitive-average"

# Send a GET request to the URL
response = requests.get(url)

'''
How to start our data collection:
1. Inspect the each university's website and see how the information is stored
    Example: Queen's info was stored in a table tag (https://www.w3schools.com/html/html_tables.asp)

2. target the data by trying the .find_all method.
'''

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the relevant data (for example, all text within table tags)
    data = soup.find_all('table')

    # Print the extracted data
    for paragraph in data:
        print(paragraph.get_text())
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)