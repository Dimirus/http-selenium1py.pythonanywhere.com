import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

from selenium.webdriver.common.by import By

def test_guest_can_add_book_from_catalog_to_basket(browser):
    browser.get(link)
    time.sleep(5)
    def is_basket_found(browser):
        try:
            browser.implicitly_wait(10)
            browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
            return True
        except:
            return False
    assert is_basket_found, 'Button basket not found' 
