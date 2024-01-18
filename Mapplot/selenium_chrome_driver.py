from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#working driver setup
def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    chrome_driver='tools\chromedriver-win64\chromedriver.exe'  # Use the correct path
    init_service = Service(chrome_driver)
    driver = webdriver.Chrome(service=init_service, options=chrome_options)
    return driver

#test driver
#driver=get_chrome_driver()
#driver.get('https://www.google.com')
#print(driver.title)  # Should print the page title
#driver.quit()
