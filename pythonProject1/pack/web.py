from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
driver.maximize_window()
driver.get(r'https://the-internet.herokuapp.com/')

driver.find_element(By.LINK_TEXT, "A/B Testing").click()
driver.find_element(By.LINK_TEXT, "Elemental Selenium").click()
windows = driver.window_handles
driver.switch_to.new_window()
driver.close()
driver.switch_to.window(windows[1])
driver.execute_script("window.scrollBy(0, 500);")
driver.find_element(By.ID, "email").send_keys("nandance07@gmail.com")
list_box = driver.find_element(By.ID, "options")
opt = Select(list_box)
opt.select_by_visible_text("Python")
driver.find_element(By.XPATH, '/input[@type="submit"]').click()
con_msg = 'Thank you!'
actual_text = driver.find_element(By.TAG_NAME, "h1")
if con_msg != actual_text.text:
    driver.get_screenshot_as_file("nan.png")
driver.quit()
