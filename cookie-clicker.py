from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time


service = webdriver.ChromeService()
driver = webdriver.Chrome(service=service)



cookie_id = "bigCookie"
num_cookies = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"
driver.get("https://orteil.dashnet.org/cookieclicker/")
WebDriverWait(driver , 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'English')]"))
)
english_text = driver.find_element(By.XPATH, "//*[contains(text(),'English')]")
english_text.click()
WebDriverWait(driver , 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)
cookie = driver.find_element(By.ID, cookie_id)
cookie.click()

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, num_cookies).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",",""))
    
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text
        
        if not product_price.isdigit():
            continue
        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break