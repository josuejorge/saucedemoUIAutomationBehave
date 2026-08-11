from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from config.config import TIMEOUT


class HomePage:

    _INVENTORY_LIST   = (By.CSS_SELECTOR, ".inventory_list")
    _INVENTORY_ITEMS  = (By.CSS_SELECTOR, ".inventory_item")
    _PRODUCT_NAMES    = (By.CSS_SELECTOR, ".inventory_item_name")
    _PRODUCT_PRICES   = (By.CSS_SELECTOR, ".inventory_item_price")
    _ADD_TO_CART_BTNS = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    _CART_BADGE       = (By.CSS_SELECTOR, ".shopping_cart_badge")
    _CART_LINK        = (By.CSS_SELECTOR, ".shopping_cart_link")
    _SORT_DROPDOWN    = (By.CSS_SELECTOR, "[data-test='product-sort-container']")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, TIMEOUT)

    def is_loaded(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._INVENTORY_LIST))
            return True
        except Exception:
            return False

    def get_product_count(self):
        self.wait.until(EC.visibility_of_element_located(self._INVENTORY_LIST))
        return len(self.driver.find_elements(*self._INVENTORY_ITEMS))

    def get_product_names(self):
        self.wait.until(EC.visibility_of_element_located(self._INVENTORY_LIST))
        return [el.text for el in self.driver.find_elements(*self._PRODUCT_NAMES)]

    def get_product_prices(self):
        self.wait.until(EC.visibility_of_element_located(self._INVENTORY_LIST))
        return [
            float(el.text.replace("$", ""))
            for el in self.driver.find_elements(*self._PRODUCT_PRICES)
        ]

    def add_first_item_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self._ADD_TO_CART_BTNS)).click()

    def get_cart_badge_count(self):
        return self.wait.until(EC.visibility_of_element_located(self._CART_BADGE)).text

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self._CART_LINK)).click()

    def select_sort(self, value):
        dropdown = self.wait.until(EC.visibility_of_element_located(self._SORT_DROPDOWN))
        Select(dropdown).select_by_value(value)
