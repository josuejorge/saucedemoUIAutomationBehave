from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import TIMEOUT


class CartPage:

    _CART_ITEMS        = (By.CSS_SELECTOR, ".cart_item")
    _REMOVE_BTNS       = (By.CSS_SELECTOR, "[data-test^='remove']")
    _CHECKOUT_BTN      = (By.CSS_SELECTOR, "[data-test='checkout']")
    _CONTINUE_SHOP_BTN = (By.CSS_SELECTOR, "[data-test='continue-shopping']")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, TIMEOUT)

    def get_item_count(self):
        return len(self.driver.find_elements(*self._CART_ITEMS))

    def is_empty(self):
        return self.get_item_count() == 0

    def remove_first_item(self):
        self.wait.until(EC.element_to_be_clickable(self._REMOVE_BTNS)).click()

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable(self._CHECKOUT_BTN)).click()

    def continue_shopping(self):
        self.wait.until(EC.element_to_be_clickable(self._CONTINUE_SHOP_BTN)).click()
