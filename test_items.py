import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_languages(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary")
    assert button.is_displayed(), "Button is not displayed on the page"