from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

class Product:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        time.sleep(2)  # wait for site to load
        self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Add to cart").click()
        time.sleep(2)
        alert = Alert(self.driver)
        alert.accept()
