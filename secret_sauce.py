from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground/'

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        inpt = self.driver.find_element(By.ID, 'ipt1')
        inpt.clear()
        inpt.send_keys(text)

    def get_input_text(self):
        inpt = self.driver.find_element(By.ID, 'ipt1')
        return inpt.get_attribute('value')

    def click_button_1(self):
        button = self.driver.find_element(By.ID, 'b1')
        button.click()

# --- Test Code ---

# Setup Chrome WebDriver
service = Service()  # You can specify the path to chromedriver here if needed
browser = webdriver.Chrome(service=service)

try:
    test_value = 'it worked'
    
    # Initialize page object
    trng_page = TrainingGroundPage(driver=browser)
    trng_page.go()
    
    # Run the test
    trng_page.type_into_input(test_value)
    txt_from_input = trng_page.get_input_text()
    
    assert txt_from_input == test_value, f"❌ Test Failed: Expected '{test_value}', but got '{txt_from_input}'."
    print("✅ Test Passed.")

finally:
    time.sleep(2)  # Optional: view the browser before closing
    browser.quit()
