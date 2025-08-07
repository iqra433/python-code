import pytest
from pywin.dialogs.ideoptions import buttonControlMap
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
def test_openbrowser():
      driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
      driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
      startbutton=driver.find_element(By.CSS_SELECTOR,"div[id='start'] button")
      startbutton.click()
