from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:/Users/Morfeu/Documents/europa-python/geckodriver-v0.24.0-win64')

driver = webdriver.Firefox()
driver.get('http://google.com.br')