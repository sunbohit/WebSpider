from selenium import webdriver
import time

file_path = './ass/url.txt'
infile = open(file_path,'r')


def download(urlline):
	driver = webdriver.Chrome()
	driver.get(urlline)
	element = driver.find_element_by_id("down")
	element.click()
	print(element.text)
	time.sleep(3000)
	driver.quit()
count = 1
for line in infile.readlines():
	line = line.strip()
	print(str(count)+" : "+line)
	download(line)
	count+=1
