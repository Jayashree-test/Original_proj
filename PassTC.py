import time

from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://leap.cuemath.com/login")
driver.find_element(By.XPATH,"//*[@id='root']/div[1]/div[2]/div[8]/div[2]/form/div[1]/div[1]/div/div[1]/input").send_keys("c9884646088")
# obj1=driver.switch_to.frame()
# obj1.dismiss()
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("c9884646088")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
a=driver.title
print(a)
if a== "Cuemath Leap":
    print("TC Pass")
else:
    print("Tc Fail")
time.sleep(5)
driver.close()
