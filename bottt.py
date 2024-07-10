import time
from colorama import init, Fore
import pyfiglet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Initialize colorama
init(autoreset=True)

# Create a Figlet font object
custom_fig = pyfiglet.Figlet(font='big')

# Print the menu options with colors
print(Fore.GREEN + custom_fig.renderText('Choose Delay:'))
print("1. " + Fore.RED + "Slow (5 second delay)")
print("2. " + Fore.LIGHTYELLOW_EX + "Normal (2 second delay)")
print("3. " + Fore.LIGHTGREEN_EX + "Turbo (1 second delay)")
print("4. " + Fore.CYAN + "Custom (Specify number of tabs)")

# Get user input for delay option
delay_option = input("Enter your choice: ")

# Function to perform delay based on user choice
def perform_delay(choice, driver, url):
    if choice == '1':
        time.sleep(5)
    elif choice == '2':
        time.sleep(2)
    elif choice == '3':
        time.sleep(1)
    elif choice == '4':
        num_tabs = int(input("Enter the number of tabs to open: "))
        for _ in range(num_tabs):
            driver.execute_script("window.open('" + url + "');")
    else:
        print("Invalid choice. Using default delay of 1 second.")
        time.sleep(1)

# Now you can run the main code after the delay
print(Fore.RED + custom_fig.renderText('FINN.NO BOT, made by zer0sec and anony0977'))

url = 'https://www.finn.no/bap/forsale/ad.html?finnkode=360695455'  # Update with your ad URL

# Set Chrome options to open a new incognito window
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the URL in incognito mode
driver.get(url)

# Perform delay based on user choice
perform_delay(delay_option, driver, url)

while True:
    # Wait for some time before repeating the process
    time.sleep(2)
