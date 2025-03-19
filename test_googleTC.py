import time

from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.co.in/")
# driver.find_element(By.ID,"APjFqb").send_keys("Amazon")
driver.find_element(By.NAME,"btnK").click()
a= driver.title
print(a)
# driver.find_element(By.PARTIAL_LINK_TEXT,"Shop online at").click()
# print("shop online link clicked")
# b=driver.title
# print(b)

