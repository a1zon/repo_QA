from selene import browser, be, have, command
from js_click import click_visible
import time

class RegistrationPage:
    def __init__(self):
        self._wait_for_page_to_load()
        
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.number = browser.element("#userNumber") 
        self.gender = browser.element("label[for='gender-radio-1']")
        self.email  = browser.element("#userEmail")
        self.date_of_birth = browser.element("#dateOfBirthInput")
        self.subjects = browser.element("#subjectsInput")
        self.upload_picture_element = browser.element("#uploadPicture")
        self.current_address = browser.element("#currentAddress")
        self.state_element = browser.element("#state")
        self.city_element = browser.element("#city")
        self.submit_element = browser.element("#submit")
        self.modal = browser.element(".modal.show")
        self.modal_title = browser.element("#example-modal-sizes-title-lg")
        self.modal_close = browser.element("[data-dismiss='modal']")
    
    def _wait_for_page_to_load(self):
        time.sleep(2)  
        try:
            browser.element("#close-fixedban").with_(timeout=3).click()
        except:
            pass
        
        try:
            browser.element("#adplus-anchor").with_(timeout=2).click()
        except:
            pass
            
        # Now wait for the form
        browser.element("#firstName").with_(timeout=20).should(be.present).should(be.visible)

    def fill_first_name(self, value):
        self.first_name.type(value)
       
    def fill_number(self, value):
        self.number.type(value)

    def fill_last_name(self, value): 
        self.last_name.type(value)
    
    def select_gender(self):
        self.gender.click()
    
    def fill_email(self, value):
        self.email.type(value)
    
    def select_date_of_birth(self):
        click_visible("#dateOfBirthInput")
        browser.element(".react-datepicker__month-select option[value='0']").click()
        browser.element(".react-datepicker__year-select option[value='2000']").click()
        browser.element(".react-datepicker__day--001").click()
    
    def select_subjects(self, subject):
        self.subjects.type(subject)
        browser.element("#react-select-2-option-0").click()
    
    def upload_picture(self, picture):
        self.upload_picture_element.set(picture)
    
    def fill_current_address(self, value):
        self.current_address.type(value)
    
    def select_state(self, state_name):
        click_visible("#state")
        browser.element("#react-select-3-option-0").with_(timeout=7).should(be.visible).click()
    
    def select_city(self, city_name):
        click_visible("#city")
        browser.element("#react-select-4-option-0").with_(timeout=7).should(be.visible).click()
    
    def submit_form(self):
        self.submit_element.should(be.present)
        self.submit_element.perform(command.js.scroll_into_view)
        self.submit_element.with_(timeout=5).should(be.clickable).click()
    