from colorama import init, Fore
import pyfiglet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Initialize colorama
init(autoreset=True)

# Create a Figlet font object
custom_fig = pyfiglet.Figlet(font='big')

# Function to validate if the URL is from Finn.no
def validate_finn_url(url):
    return 'finn.no' in url

# Print the menu options with colors
print(Fore.GREEN + custom_fig.renderText('FINN.NO VIEWBOT:'))
print("1. " + Fore.RED + "Slow (15 tabs)")
print("2. " + Fore.LIGHTYELLOW_EX + "Normal (50 tabs)")
print("3. " + Fore.LIGHTGREEN_EX + "Turbo (100 tabs)")
print("4. " + Fore.CYAN + "Custom (Specify number of tabs)")
print("Disclaimer. " + Fore.CYAN + "More ram = More power (use this at ur own risk ;)")

# Get user input for delay option
delay_option = input("Enter your choice: ")

# Get the URL from the user
url = input("Enter the Finn.no ad URL: ")

# Validate the URL
if not validate_finn_url(url):
    print("Invalid link. Please provide a Finn.no ad URL.")
    exit()

# Function to perform delay based on user choice
def perform_delay(choice, url):
    if choice == '1':
        return 15  # Slow option
    elif choice == '2':
        return 50  # Normal option
    elif choice == '3':
        return 100  # Turbo option
    elif choice == '4':
        num_tabs = int(input("Enter the number of tabs to open: "))
        return num_tabs
    else:
        print("Invalid choice. Using default of 15 tabs.")
        return 15

# Function to open tabs and manage Chrome sessions
def open_tabs(driver, num_tabs, url):
    tabs_opened = 0
    while tabs_opened < num_tabs:
        driver.execute_script("window.open('" + url + "');")
        tabs_opened += 1
        if tabs_opened % 50 == 0:  # Close and reopen Chrome after every 50 tabs
            driver.quit()
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
    return driver

# Now you can run the main code after the delay
print(Fore.RED + custom_fig.renderText('FINN.NO BOT, made by zer0sec and anony0977'))

# Set Chrome options to open a new incognito window
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Get the number of tabs to open based on user choice
num_tabs = perform_delay(delay_option, url)

# Open tabs and manage Chrome sessions
driver = open_tabs(driver, num_tabs, url)

while True:
    # Wait for some time before repeating the process
    time.sleep(2)
