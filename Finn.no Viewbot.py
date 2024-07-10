import pyperclip
import webbrowser
import time
from colorama import init, Fore
import pyfiglet
import pyfiglet
import time

# Create a Figlet font object
custom_fig = pyfiglet.Figlet(font='big')

# Print the menu options
print(custom_fig.renderText('Choose Delay:'))
print("1. 5 second delay")
print("2. 2 second delay")
print("3. 1 second delay")

# Get user input for delay option
delay_option = input("Enter your choice: ")

# Function to perform delay based on user choice
def perform_delay(choice):
    if choice == '1':
        time.sleep(5)
    elif choice == '2':
        time.sleep(2)
    elif choice == '3':
        time.sleep(1)
    else:
        print("Invalid choice. Using default delay of 1 second.")
        time.sleep(1)

# Perform delay based on user choice
perform_delay(delay_option)

# Now you can run the main code after the delay
print("FINN.NO BOT, made by zer0sec and anony0977")
# Create a Figlet font object
custom_fig = pyfiglet.Figlet(font='big')

# Print the text in big letters
print(custom_fig.renderText('FINN.NO BOT, made by zer0sec and anony0977'))

url = 'https://www.finn.no/bap/forsale/ad.html?finnkode=360695455'  # Update with your ad URL

init(autoreset=True)


while True:
    # Copy the URL to the clipboard
    pyperclip.copy(url)

    # Open the URL in a new tab
    webbrowser.open_new_tab(url)
    
    # Wait for some time before repeating the process
    time.sleep(2)
