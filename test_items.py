from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

    browser.find_element(By.TAG_NAME, 'button[value="Добавить в корзину"]')
