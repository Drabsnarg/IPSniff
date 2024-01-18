from selenium import webdriver
from selenium_chrome_driver import get_chrome_driver
from selenium.webdriver.common.by import By
import time
import csv 


# Setup Selenium WebDriver
#chrome_driver='tools\chromedriver-win64\chromedriver.exe'  # Use the correct path
#service = Service(chrome_driver)
#driver = webdriver.Chrome(service=service)

# Initialize the WebDriver using the function from selenium_chrome_driver.py
driver = get_chrome_driver()

# Open the webpage
driver.get('https://www.drvc.org/maps/')

# Wait for JavaScript to load content
time.sleep(5)  # Adjust this as necessary

# Find elements by class name
church_elements = driver.find_elements(By.CLASS_NAME, 'place_title')

# Extract text and data-marker from each element
church_data = [{'name': element.text, 'data_marker': element.get_attribute('data-marker')} for element in church_elements]

# Print the extracted data
#for data in church_data:
#    print(f"Name: {data['name']}, Data-Marker: {data['data_marker']}")

with open('church_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['data_marker', 'name'])
    writer.writeheader()
    writer.writerows(church_data)
#Close the browser
driver.quit()
