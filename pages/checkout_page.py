from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import TIMEOUT


class CheckoutPage:

    _FIRST_NAME    = (By.CSS_SELECTOR, "[data-test='firstName']")
    _LAST_NAME     = (By.CSS_SELECTOR, "[data-test='lastName']")
    _POSTAL_CODE   = (By.CSS_SELECTOR, "[data-test='postalCode']")
    _CONTINUE_BTN  = (By.CSS_SELECTOR, "[data-test='continue']")
    _CANCEL_BTN    = (By.CSS_SELECTOR, "[data-test='cancel']")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    _FINISH_BTN    = (By.CSS_SELECTOR, "[data-test='finish']")
    _COMPLETE_HDR  = (By.CSS_SELECTOR, ".complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, TIMEOUT)

    def fill_info(self, first_name, last_name, postal_code):
        self.wait.until(EC.visibility_of_element_located(self._FIRST_NAME)).send_keys(first_name)
        self.driver.find_element(*self._LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self._POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self._CONTINUE_BTN)).click()

    def click_cancel(self):
        self.wait.until(EC.element_to_be_clickable(self._CANCEL_BTN)).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self._FINISH_BTN)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE)).text

    def get_complete_header(self):
        return self.wait.until(EC.visibility_of_element_located(self._COMPLETE_HDR)).text
