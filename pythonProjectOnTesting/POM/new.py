import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True  # Use Chromium-based Microsoft Edge
edge_options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Edge(options=opt)
driver.implicitly_wait(30)

driver.maximize_window()
# driver.get("https://www.facebook.com/")
# driver.find_element("id", "email").send_keys("8660532161")
# driver.find_element("id", "pass").send_keys("#Mn_071098")
# driver.find_element("name", "login").click()
# time.sleep(10)
# action_obj = ActionChains(driver)
# action_obj.key_down(Keys.ESCAPE).perform()
# driver.find_element('xpath', '//a[@aria-label="Home"]').click()
# driver.find_element("xpath", '(//div[@aria-label="Account Controls and Settings"]//div[2])[2]').click()
# #
# # time.sleep(10)
