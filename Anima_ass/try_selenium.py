from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://subhd.com/ar0/327068')

element = driver.find_element_by_id("down")
element.click()
print(element.text)
driver.quit()
