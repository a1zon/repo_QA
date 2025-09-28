# from selenium import webdriver
# from selene import browser

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# # Add other options as needed

# browser.config.driver = webdriver.Remote(
#     command_executor='http://localhost:4444/wd/hub',
#     options=options
# )

# browser.config.base_url = 'https://google.com'
# browser.config.timeout = 12

# browser.open('/ncr')

def test_test1():
    assert 1 == 1 

def test_sum():
    a = 10
    b = 20 
    assert a + b == 30

def test_fail():
    assert 1 == 1