import pytest 
from selene import browser, have, be
from selenium.webdriver.chrome.options import Options 
from pathlib import Path
from selenium.webdriver import ActionChains
from js_click import click_visible
from registration_page import RegistrationPage
from sources import Sources



@pytest.fixture (autouse=True, scope="function")
def browser_config():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    browser.config.driver_options = options
    browser.config.timeout = 25
    browser.open("https://demoqa.com/automation-practice-form")
    yield
    browser.quit()


def test_min_valid_form():
    page = RegistrationPage()
    page.fill_first_name("Andrew")
    page.fill_last_name("Second")
    page.fill_number("1231231231")
    page.select_gender()

    page.submit_form()
    page.modal_title.should(have.text("Thanks for submitting the form"))


def test_all_valid_form():
    page = RegistrationPage()
    page.fill_first_name("Andrew")
    page.fill_last_name("Second")
    page.fill_number("1231231231")
    page.select_gender()
    page.fill_email("test@gmail.com")
    click_visible("#dateOfBirthInput")
    page.select_date_of_birth()
    page.select_subjects("Math")
 
    page.upload_picture(Sources.PICTURE_PATH)   
    page.fill_current_address("Some address 1") 
    page.select_state("California")
    page.select_city("Los Angeles")
    page.submit_form()

    
    page.modal_title.should(have.text("Thanks for submitting the form"))


