#file that deals with the chrome driver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument('--no-proxy-server')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome('./driver/chromedriver', options=options)
driver.execute_script("window.onblur = function() { window.onfocus() }")
wait = WebDriverWait(driver,10)