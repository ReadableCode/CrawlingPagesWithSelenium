from datetime import datetime  
from datetime import timedelta   
import CrawlingPagesWithSeleniumConfig
from selenium import webdriver
import csv


today = datetime.now()
maxPageNum = 5
maxPageDigit = 3

with open('result.csv', 'w') as f:
	f.write("Buyers, Price \n")

driver = webdriver.Firefox()

for i in range(1, maxPageNum + 1):
	pageNum = (maxPageDigit - len(str(i))) * "0" + str(i)
	url = "http://econpy.pythonanywhere.com/ex/" + pageNum + ".html"
	#print(url)
	
	driver.get(url)
	buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
	prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
	
	numPageItems = len(buyers)

	for i in range(numPageItems):
		print(buyers[i].text + " : " + prices[i].text)

	with open('result.csv', 'a') as f:
		for i in range(numPageItems):
			f.write(buyers[i].text + "," + prices[i].text + "\n")
	
	
	
	
# driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# # extract lists of buyers and prices based on xpath
# buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
# prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# numPageItems = len(buyers)

# for i in range(numPageItems):
	# print(buyers[i].text + " : " + prices[1].text)

# #cleanup when you are done
driver.close()



# print (today)
# print (program2config.testVar)