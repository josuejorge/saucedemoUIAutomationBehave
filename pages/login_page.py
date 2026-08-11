from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import BASE_URL, TIMEOUT


class LoginPage:

    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON   = (By.ID, "login-button")
    _ERROR_MESSAGE  = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, TIMEOUT)

    def navigate(self):
        self.driver.get(BASE_URL)
        self.driver.execute_script("window.localStorage.clear();")

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT)).send_keys(username)
        self.driver.find_element(*self._PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self._LOGIN_BUTTON).click()

    def click_login_without_credentials(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()

    def is_login_successful(self):
        try:
            self.wait.until(EC.url_contains("/inventory.html"))
            return True
        except Exception:
            return False

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self._ERROR_MESSAGE)
        ).text
