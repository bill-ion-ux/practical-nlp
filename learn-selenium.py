from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("https://www.youtube.com/watch?v=NHLF0yM_TBQ")

title = driver.title

time.sleep(10)

messages = driver.find_elements(by= By.ID, value="content-text")
print(messages)
text = []
for message in messages:
    text.append(message.text)
    print(message.text)


