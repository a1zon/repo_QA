from selene import browser

def test_todo():

    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').type("Buy groceries").press_enter()
    # browser.element(id="new-todo").type("Walk the dog").press_enter()