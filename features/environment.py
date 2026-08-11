import sys
import os

# garante que a raiz do projeto está no path para imports de pages/ e config/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
