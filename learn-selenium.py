from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome()

driver.get("https://www.youtube.com/watch?v=NHLF0yM_TBQ")

title = driver.title

time.sleep(10)

authors = driver.find_elements(by= By.ID, value= "author-text")
messages = driver.find_elements(by= By.ID, value="content-text")
print(messages)
texts = []
for message, author in zip(messages, authors):
   texts.append({
       'Author': author.text,
       'Comment': message.text
   })


with open('comments1.csv', 'w', newline='', encoding='utf-8')as csvfile:
    fieldnames = ['Author', 'Comment']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(texts)