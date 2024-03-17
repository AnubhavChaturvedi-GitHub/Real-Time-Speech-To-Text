from os import getcwd
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Setting up Chrome options with specific arguments
chrome_options = webdriver.ChromeOptions()  # Creating ChromeOptions to customize the behavior of the Chrome browser
chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Adding an argument to simulate a fake UI for media stream
chrome_options.add_argument("--headless=new")  # Adding an argument to run Chrome in headless mode with a new session

# Setting up the Chrome driver with specified service and options
driver = webdriver.Chrome(service=Service(executable_path=r"chromedriver.exe"), options=chrome_options)

# Creating the URL for the website using the current working directory
website = f"{getcwd()}\\try.html"

# Opening the website in the Chrome browser
driver.get(website)

def Listen():
    start_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'start')))
    start_button.click()

    output_text = ""
    try:
        with open("output.txt", "w") as output_file:
            while True:
                output_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'output')))
                current_text = output_element.text.strip()
                if current_text != output_text:
                    output_text = current_text
                    print(output_text)
                    output_file.write(output_text + "\r")  # Write to file
                    if "jarvis" in output_text.lower():
                        print("Hello sir")
                time.sleep(0.5)  # Adjust the sleep duration as needed
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    try:
        Listen()
    finally:
        driver.quit()
