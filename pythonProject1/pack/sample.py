from selenium import webdriver
from selenium.webdriver.common.by import By

# To stop automatically closing browser
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option,)
driver.maximize_window()
driver.get(r'https://www.selenium.dev/')
driver.find_element(By.XPATH, '//div[@id="main_navbar"]//li[2]').click()
listOfElements = []
allElements = driver.find_elements(By.XPATH,"//a")
# print(allElements)
for texts in allElements:
    listOfElements.append(texts)
print(listOfElements)
driver.close()
