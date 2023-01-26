from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--start-maximized')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

dwait = float(0.5) #default wait time in seconds 

driver = webdriver.Chrome(options=chrome_options)

def clean_text(text):
  """extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def main():
  driver.get("http://automated.pythonanywhere.com/login/") #load the page
  #enter creds and press RETURN
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(dwait)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  #wait for load, then find & click the HOME button element
  time.sleep(dwait)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  #wait for laod, then find the element with the desired text 
  time.sleep(2)
  mytext = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  #clean up the text and return it
  return clean_text(mytext.text)

print(main())

