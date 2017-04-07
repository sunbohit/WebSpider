from selenium import webdriver
import time

file_path = './url.txt'
infile = open(file_path,'r')

for line in infile.readlines():
	line = line.strip()
	print(line)
	download(line)
def download(urlline)
	driver = webdriver.Chrome()
	driver.get(urlline)
	element = driver.find_element_by_id("down")
	element.click()
	print(element.text)
	time.sleep(100)
	driver.quit()
