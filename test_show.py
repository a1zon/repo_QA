import pytest
from selene import browser, have, be, command
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class StudentForm:
    # Селекторы
    FIRSTNAME_INPUT = "#firstName"
    LASTNAME_INPUT = "#lastName"
    EMAIL_INPUT = "#userEmail"
    MOBILE_INPUT = "#userNumber"
    SUBJECTS_INPUT = "#subjectsInput"
    SUBJECTS_OPTION_MATHS = "#react-select-2-option-0"
    UPLOAD_INPUT = "#uploadPicture"
    CURRENT_ADDRESS_INPUT = "#currentAddress"
    STATE_DROPDOWN = "#state"
    STATE_INPUT = "#react-select-3-input"
    CITY_DROPDOWN = "#city"
    CITY_INPUT = "#react-select-4-input"
    DATE_OF_BIRTH_INPUT = "#dateOfBirthInput"
    SUBMIT_BUTTON = "#submit"
    GENDER_MALE_LABEL = "label[for='gender-radio-1']"
    MODAL_CLOSE = "[data-dismiss='modal']"  # Кнопка закрытия модалки

    def __init__(self, browser_obj):
        self.browser = browser_obj

    def select_subjects(self, subject: str):
        subjects_input = self.browser.element(self.SUBJECTS_INPUT)
        subjects_input.perform(command.js.scroll_into_view)
        subjects_input.should(be.clickable).click()
        subjects_input.type(subject)
        self.browser.element(self.SUBJECTS_OPTION_MATHS).should(be.visible).click()

    def select_date_of_birth(self):
        dob_input = self.browser.element(self.DATE_OF_BIRTH_INPUT)
        dob_input.perform(command.js.scroll_into_view)
        dob_input.should(be.clickable).click()
        self.browser.element(".react-datepicker__month-select option[value='0']").click()
        self.browser.element(".react-datepicker__year-select option[value='2000']").click()
        self.browser.element(".react-datepicker__day--001").click()

    def select_state(self, state: str):
        state_dropdown = self.browser.element(self.STATE_DROPDOWN)
        state_dropdown.perform(command.js.scroll_into_view)
        state_dropdown.should(be.clickable).click()
        state_input = self.browser.element(self.STATE_INPUT).with_(timeout=3).should(be.present)
        state_input.type(state)
        state_input.press(Keys.ENTER)

    def select_city(self, city: str):
        # Ждём, пока не исчезнут все модалки (чтобы не перекрывали клики)
        self.browser.all('.modal.show').should(have.size(0))

        city_dropdown = self.browser.element(self.CITY_DROPDOWN)
        city_dropdown.perform(command.js.scroll_into_view)
        city_dropdown.should(be.clickable).click()
        city_input = self.browser.element(self.CITY_INPUT).with_(timeout=3).should(be.present)
        city_input.type(city)
        city_input.press(Keys.ENTER)

    def submit(self):
        submit_btn = self.browser.element(self.SUBMIT_BUTTON)
        submit_btn.perform(command.js.scroll_into_view)
        submit_btn.should(be.clickable).click()

    def close_modal(self):
        """Закрыть модальное окно, если оно есть"""
        close_btn = self.browser.element(self.MODAL_CLOSE)
        close_btn.should(be.visible).click()
        # Ждём, пока модалка полностью исчезнет
        self.browser.all('.modal.show').should(have.size(0))


@pytest.fixture(autouse=True, scope='function')
def browser_config():
    options = Options()
    # options.add_argument('--headless=new')  # включай для CI
    browser.config.driver_options = options
    browser.config.timeout = 10
    browser.config.hold_browser_open = True  # Чтобы не закрывалось при ошибке

    browser.open('https://demoqa.com/automation-practice-form')
    browser.element("#firstName").with_(timeout=5).should(be.present)

    # Проверка: если модалка осталась с прошлого теста — закрыть
    if browser.element("#example-modal-sizes-title-lg").matching(be.present):
        form = StudentForm(browser)
        form.close_modal()

    yield
    browser.quit()


def test_valid_name():
    form = StudentForm(browser)
    form.browser.element(form.FIRSTNAME_INPUT).type("Andrew")
    gender_label = form.browser.element(form.GENDER_MALE_LABEL)
    gender_label.perform(command.js.scroll_into_view)
    gender_label.should(be.clickable).click()
    form.submit()

    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
    form.close_modal()

    # Проверка, что поле подсвечено зелёным
    form.browser.element(form.FIRSTNAME_INPUT).should(
        have.css_property("border-color").value("rgb(40, 167, 69)")
    )


def test_valid_form():
    form = StudentForm(browser)

    form.browser.element(form.FIRSTNAME_INPUT).type("Andrew")
    form.browser.element(form.LASTNAME_INPUT).type("Ivanov")
    form.browser.element(form.EMAIL_INPUT).type("andrew.ivanov@example.com")
    form.browser.element(form.MOBILE_INPUT).type("1234567890")
    form.select_subjects("Maths")
    form.browser.element(form.UPLOAD_INPUT).set("/Users/Geyger.Andrey/Desktop/file_example_JPG_100kB.jpg")
    form.browser.element(form.CURRENT_ADDRESS_INPUT).type("123 Main St")
    form.browser.element(form.GENDER_MALE_LABEL).should(be.clickable).click()
    form.select_date_of_birth()
    form.select_state("California")
    form.select_city("Los Angeles")

    form.submit()

    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
    browser.element(".modal-body .table td:nth-child(2)").should(have.text("Andrew Ivanov"))
    form.close_modal()
