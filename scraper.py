from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (optional)

service = Service(r"\path\to\chromedriver.exe")  # Replace with your ChromeDriver path
driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://betolimp.co.za/en/sports/"
driver.get(url)

# Wait for the page to load (adjust time as needed)
time.sleep(5)

# Get the page source
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

links = soup.find_all('a')
for link in links:
    print(link.get('href'))


driver.quit()