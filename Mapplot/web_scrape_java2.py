from selenium import webdriver
from selenium_chrome_driver import get_chrome_driver
from selenium.webdriver.common.by import By
import time
import csv 
from collections import Counter
import re
from datetime import datetime


# Setup Selenium WebDriver
#chrome_driver='tools\chromedriver-win64\chromedriver.exe'  # Use the correct path
#service = Service(chrome_driver)
#driver = webdriver.Chrome(service=service)

# Initialize the WebDriver using the function from selenium_chrome_driver.py
driver = get_chrome_driver()

#link
url = 'https://ubuntu.com/download/desktop'

#get file name from link
domain = url.split("//")[-1].split("/")[0].split('.')[0]
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{domain}_data_{timestamp}.csv"

# Open the webpage
driver.get(url)

# Wait for JavaScript to load content
time.sleep(5)  # Adjust this as necessary

# Find elements by class name
#elements = driver.find_elements(By.CLASS_NAME, 'place_title')
page_text = driver.find_element(By.TAG_NAME, "body").text

# Extract text and data-marker from each element
#data = [{'name': element.text, 'data_marker': element.get_attribute('data-marker')} for element in elements]

# Remove non-alphabetic characters and split text into words
words = re.findall(r'\b\w+\b', page_text.lower())

# Count occurrences of each word
word_count = Counter(words)

# Print the extracted data
#for data in data:
#    print(f"Name: {data['name']}, Data-Marker: {data['data_marker']}")

# Print word counts
#for word, count in word_count.items():
#    print(f"{word}: {count}")

#with open('data.csv', 'w', newline='', encoding='utf-8') as file:
#    writer = csv.DictWriter(file, fieldnames=['data_marker', 'name'])
#    writer.writeheader()
#    writer.writerows(data)

with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Word', 'Count'])  # Writing header

    for word, count in word_count.items():
        writer.writerow([word, count])  # Writing each word and its count

#Close the browser
driver.quit()
