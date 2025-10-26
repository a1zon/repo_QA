from selene import be, browser, command


def click_visible(selector):
    el = browser.element(selector)
    el.should(be.present)
    el.perform(command.js.scroll_into_view)
    el.with_(timeout=5).should(be.clickable).click()