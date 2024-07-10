from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to the ChromeDriver executable
chrome_driver_path = '/path/to/chromedriver'  # Update with your path

# URL of the FINN.no ad you want to increase views on
url = 'https://www.finn.no/bap/forsale/ad.html?finnkode=360695455'  # Update with your ad URL

def open_and_close_browser():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # Set up Chrome driver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the URL
        driver.get(url)
        # Wait for a few seconds
        time.sleep(5)
    finally:
        # Close the browser
        driver.quit()

while True:
    open_and_close_browser()
    # Wait for a few seconds before reopening
    time.sleep(10)  # Adjust the wait time as needed, It goes on of your Pc specs so more powerfull pc les delay time
