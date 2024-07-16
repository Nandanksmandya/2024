import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r"https://demoqa.com/automation-practice-form")
driver.execute_script("window.scrollBy(0, 200);")
driver.find_element("xpath", '//input[@placeholder="First Name"]').send_keys("Nandan")
driver.find_element("xpath", '//input[@placeholder="Last Name"]').send_keys("K S")
driver.find_element("xpath", '//input[@id="userEmail"]').send_keys(r"nandance07@gmail.com")
driver.find_element("xpath", '//input[@id="gender-radio-1"]//..').click()
driver.find_element("xpath", '//input[@id="userNumber"]').send_keys("8660532161")
driver.execute_script("window.scrollBy(0, 200);")
driver.find_element("xpath", '//button[@aria-label="Next Month"]').click()
driver.find_element("xpath", '//button[@aria-label="Next Month"]').click()
driver.find_element("xpath", '//button[@aria-label="Next Month"]').click()
driver.find_element("xpath", '//option[@value="1998"]').click()
time.sleep(10)
