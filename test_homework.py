import pytest 
from selene import browser, be, have, command
from selenium.webdriver.chrome.options import Options 
from pathlib import Path




@pytest.fixture (autouse=True, scope="session")
def browser_config():
    options = Options()
    options.add_argument('--headless=new')
    browser.config.driver_options = options
    browser.config.timeout = 15
    browser.open("https://demoqa.com/automation-practice-form")
    options.add_argument('--window-size=1920,1080')
    yield
    browser.quit()

# def test_browser_form():
#     browser.element("#firstName").with_(timeout=5).should(be.present)

# def test_valid_name():
#     browser.element("#firstName").type("Andrew")
#     browser.element("#firstName").should(have.value("Andrew"))

def click_visible(selector):
    el = browser.element(selector)
    el.should(be.present)
    el.perform(command.js.scroll_into_view)
    el.should(be.clickable).click()

# def test_min_valid_form():
#     browser.element("#firstName").type("Andrew")
#     browser.element("#lastName").type("Second")
#     click_visible("label[for='gender-radio-1']")
#     browser.element("#userNumber").type("1231231231")
#     click_visible("#submit")

#     browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))


# def test_all_valid_form():
#     browser.element("#firstName").type("Andrew")
#     browser.element("#lastName").type("Second")
#     browser.element("#userEmail").tyoe("test@gmail.com")
#     click_visible("label[for='gender-radio-1']")
#     click_visible("#dateOfBirthInput")
#     browser.element(".react-datepicker__month-select option[value='0']").click()
#     browser.element(".react-datepicker__year-select option[value='2000']").click()
#     browser.element(".react-datepicker__day--001").click()
#     click_visible("#subjectsInput")
#     browser.element("#subjectsInput").type("Math")
#     click_visible("#react-select-2-option-0") 
#     file_path = str(Path("/Users/Geyger.Andrey/Desktop/repo_QA/tmp/file_example_JPG_100kB.jpg").resolve())
#     browser.element("#uploadPicture").set(file_path)   
#     browser.element("#currentAddress").type("Some address 1") 


def test_func():    
    click_visible("#state")
    click_visible("#city")

