from selenium import webdriver
from selene import browser

options = webdriver.ChromeOptions()
options.add_argument('--headless')
# Add other options as needed

browser.config.driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
)

browser.config.base_url = 'https://google.com'
browser.config.timeout = 2

browser.open('/ncr')