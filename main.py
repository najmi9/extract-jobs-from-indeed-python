#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
Created on Tusday Oct 04 09:36:42 2020

@author: Najmi Imad
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv


def main():
	job = input('Job title, keywords, or company : \n')
	city = input('city or origin : \n')
	
	url = "https://ma.indeed.com/"
	
	options = Options()
	options.headless=True
	driver = webdriver.Chrome("../chromedriver", options=options)
	driver.get(url)
	driver.find_element_by_xpath('//input[@name="q"]').send_keys(job)
	driver.find_element_by_xpath('//input[@name="l"]').send_keys(city)
	driver.find_element_by_xpath('//button[@type="submit"]').click()
	sleep(5)
	
	jobs = driver.find_elements_by_xpath('//div[@class="jobsearch-SerpJobCard unifiedRow row result clickcard"]')
	
	title=company=location=salury=date="Not Provided"

	skils_array = []
	with open('data.csv', 'w') as f:
		csv_file = csv.writer(f)
		csv_file.writerow(["title", "company", "location", "salury", "required skils" ,"date"])
	
	print("There is {} jobs for this search".format(len(jobs)))
	
	for job in jobs:

		title = job.find_element_by_css_selector('h2.title').text 
		

		try:
			company = job.find_element_by_css_selector('span.company').text
		except Exception as e:
			pass

		try:
			location = job.find_element_by_css_selector('span.accessible-contrast-color-location').text
		except Exception as e:
			pass
		
		try:
			salury = job.find_element_by_css_selector('span.salaryText').text
		except Exception as e:
			pass
		
		try:
			date = job.find_element_by_css_selector('span.date').text
		except Exception as e:
			pass

		try:
			required_skils =  job.find_element_by_css_selector('div.jobCardReqItem')
			for sk in required_skils:
				skils_array.append(sk)
		except Exception as e:
			pass

		with  open('data.csv', 'a') as f:
			csv_file = csv.writer(f)
			csv_file.writerow([title, company, location, salury, ','.join(skils_array) ,date])
		
		title=company=location=salury=date="Not Provided"
	
	driver.close()
	driver.quit()

if __name__ == '__main__':
	main()