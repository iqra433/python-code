from selenium.webdriver.common.by import By
import time

class Checkout:
    def __init__(self, driver):
        self.driver = driver

    def place_order(self):
        time.sleep(2)

        # Go to cart page
        self.driver.find_element(By.ID, "cartur").click()
        time.sleep(2)

        # Click "Place Order"
        self.driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
        time.sleep(1)

        # Fill in the form
        self.driver.find_element(By.ID, "name").send_keys("John Doe")
        self.driver.find_element(By.ID, "country").send_keys("Pakistan")
        self.driver.find_element(By.ID, "city").send_keys("Lahore")
        self.driver.find_element(By.ID, "card").send_keys("1234567812345678")
        self.driver.find_element(By.ID, "month").send_keys("12")
        self.driver.find_element(By.ID, "year").send_keys("2025")

        # Click "Purchase"
        self.driver.find_element(By.XPATH, "//button[text()='Purchase']").click()
        time.sleep(2)

        # Get confirmation text
        confirmation = self.driver.find_element(By.XPATH, "//div[@class='sweet-alert  showSweetAlert visible']/h2").text
        print("Order Confirmation:", confirmation)

        # Click OK
        self.driver.find_element(By.XPATH, "//button[text()='OK']").click()
