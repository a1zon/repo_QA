from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selene import query
import requests
from script_os import TMP_DIR
def test():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False,
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(), options=options)
    browser.config.driver = driver

    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    href = browser.element("[data-testid=\"raw-button\"]").get(query.attribute("href"))
    print(href)
    content = requests.get(url =href).content
    with open("tmp/README.rst", "wb") as file:
        file.write(content)

    with open("tmp/README.rst", "r") as file:
        a = file.read()
        assert 'test_answer' in a
    # browser.element("[data-testid=\"download-raw-button\"]").click()
    # time.sleep(10)  # wait for the download to complete
