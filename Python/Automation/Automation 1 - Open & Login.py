from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://access02.dwp.accenture.com/SecureAuth1/SecureAuth.aspx")
userId=selenium.find_element_by_text("User ID")

userId.send_keys("sbhatter")

selenium.find_element_by_name("Submit").click()
