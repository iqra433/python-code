import pytest
from pywin.dialogs.ideoptions import buttonControlMap
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
class Navigation:
      def open_site(self):
          driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          driver.get("https://www.demoblaze.com/")
          driver.implicitly_wait(1000)
          return driver
