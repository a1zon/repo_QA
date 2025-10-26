import pytest
from selene import browser , have ,be, command, query
from selenium.webdriver.chrome.options import Options

class Studentform:
    def __init__(self, browser):
        self.browser = browser
        self.FIRSTNAME = browser.element("#firstName")
        self.LASTNAME = browser.element("#lastName")
        self.EMAIL = browser.element("#userEmail")
        self.SUBMIT = browser.element("#submit")
        self.GENDER1 = browser.element("#gender-radio-1")
        self.GENDER2 = browser.element("#gender-radio-2")
        self.GENDER3 = browser.element("#gender-radio-3")
        self.MOBILE = browser.element("#userNumber")
        self.SUBJECTS = browser.element("#subjectsInput")
        self.UPlOAD = browser.element("#uploadPicture")
        self.CURRENTADDRESS = browser.element("#currentAddress")
        self.STATE = browser.element("#state")
        self.CITY = browser.element("#city")
        self.DATEOFBIRTH = browser.element("#dateOfBirthInput")


@pytest.fixture(autouse=True, scope='session')
def browser_config():
    options = Options()
    options.add_argument('--headless=new')
    browser.config.driver_options = options
    browser.config.timeout = 5
    browser.open('https://demoqa.com/automation-practice-form')
    yield 
    browser.quit()

# def test_valid_page():
#     browser.element('h5').should(have.text('Student Registration Form'))


# def test_user_form():
#     browser.element("#submit").perform(command.js.scroll_into_view)
#     browser.element("#submit").should(be.visible).click()
#     browser.element("#example-modal-sizes-title-lg").should(have.no.present)

def test_valid_name():
    form = Studentform(browser)
    form.FIRSTNAME.type("Andrew")
    form.SUBMIT.perform(command.js.scroll_into_view)
    form.SUBMIT.should(be.visible).click()
    form.FIRSTNAME.should(have.css_property("border-color", "rgb(40, 167, 69)"))

def test_valid_form():
    form = Studentform(browser)
    form.FIRSTNAME.type("Andrew")
    form.LASTNAME.type("Ivanov")
    form.EMAIL.type("andrew.ivanov@example.com")
    form.MOBILE.type("1234567890")
    form.SUBJECTS.click()
    form.SUBJECTS.type("Maths")
    form.UPlOAD.set("path/to/file.jpg")
    form.CURRENTADDRESS.type("123 Main St")
    form.STATE.type("California")
    form.CITY.type("Los Angeles")
    form.DATEOFBIRTH.type("01 Jan 2000")
    form.SUBMIT.perform(command.js.scroll_into_view)
    form.SUBMIT.should(be.visible).click()
    form.FIRSTNAME.should(have.css_property("border-color", "rgb(40, 167, 69)"))
    form.LASTNAME.should(have.css_property("border-color", "rgb(40, 167, 69)"))
    form.EMAIL.should(have.css_property("border-color", "rgb(40, 167, 69)"))
    form.MOBILE.should(have.css_property("border-color", "rgb(40, 167, 69)"))
    form.SUBJECTS.should(have.css_property("border-color", "rgb(40, 167, 69)"))
    form.UPlOAD.should(have.css_property("border-color", "rgb(40, 167, 69)"))
    form.CURRENTADDRESS.should(have.css_property("border-color", "rgb(40, 167, 69)"))
    form.STATE.should(have.css_property("border-color", "rgb(40, 167, 69)"))
    form.CITY.should(have.css_property("border-color", "rgb(40, 167, 69)"))
    form.DATEOFBIRTH.should(have.css_property("border-color", "rgb(40, 167, 69)"))

# def test_invalid_email():

    # browser.element("#firstName").type("Andrew")S
    # browser.element("#lastName").type("Ivanov")
    
    # field = browser.element("#userEmail")
    
    # field.type("123")

    # browser.element("#submit").perform(command.js.scroll_into_view)
    # browser.element("#submit").should(be.visible).click()
    # browser.element("#userEmail").should(have.css_class("is-invalid"))

