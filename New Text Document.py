import time
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
# Make a request to https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
page = requests.get("http://time.is", headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.time.text

# print the result
print(page_title)
