from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--start-maximized')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=chrome_options)

def clean_text(text):
  """extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def main():
  driver.get("http://automated.pythonanywhere.com") #load the page
  time.sleep(2) #idle for 2 seconds, dynamic page elements have time to load
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  return clean_text(element.text)

print(main())
