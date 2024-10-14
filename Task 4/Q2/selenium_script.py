import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import TimeoutException, NoSuchElementException
s = Service("D:/atta/Internship/Week 1/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)
url = "https://www.urdupoint.com/names/boys/a.html"
driver.get(url)
import time
time.sleep(5)

wait = WebDriverWait(driver, 10)
# b = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div[6]/div[1]/div[12]/a[6]""")))
# b.click()

for i in range(12):
    time.sleep(10)
    c = True
    while c:
        try:
            button = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[2]/div[6]/div[1]/div[15]/span""")))
            button.click()
            break
        # button = driver.find_element(By.XPATH, """/html/body/div[2]/div[6]/div[1]/div[15]/span""")
        except Exception as e:
            print("exception occurs")
            time.sleep(5)

time.sleep(10)
tds = driver.find_elements(By.TAG_NAME, "td")


def isdigit(s):
    if(s == ""):
        return False
    """
    Check if the string s contains only digit characters.

    :param s: Input string
    :return: True if all characters in the string are digits, False otherwise
    """
    for char in s:
        if char < '0' or char > '9':
            return False
    return True


eng_names_list = []
urdu_names_list = []

for i in range(len(tds)):
    if(isdigit(tds[i].text)):
        eng_names_list.append(tds[i+1].text)
        urdu_names_list.append(tds[i+2].text)

    else:
        continue

import pandas as pd
df = pd.DataFrame({"English" : eng_names_list,
                   "urdu" : urdu_names_list})

df.to_csv("A_eng_urdu_names.csv", index=False)
df.to_excel("A_eng_urdu_names.xlsx", index=False)