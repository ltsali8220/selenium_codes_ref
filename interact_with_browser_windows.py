from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Optional: Helps avoid GPU rendering issues on some setups (useful for recording/CI)
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')

# Setup Chrome driver (you can specify Service(executable_path="path/to/chromedriver") if needed)
driver = webdriver.Chrome(service=Service(), options=options)

# Open main tab
driver.get('http://techstepacademy.com/training-ground')

# Open additional tabs with the same URL
for _ in range(4):
    driver.execute_script('window.open("http://techstepacademy.com/training-ground", "_blank");')

# Optional: Let the browser stay open for a few seconds so you can see it
time.sleep(5)

# Clean up
driver.quit()
