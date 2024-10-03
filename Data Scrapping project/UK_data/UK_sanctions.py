import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


unique_id_list = []
ofsi_group_id_list = []
name_list  =[]
regime_name_list = []
type_list = []
designation_source_list = []
date_designated_list = []
sanctions_imposed_list  = []


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

s = Service("D:/Atta/Internship/Week 3/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)
url = "https://search-uk-sanctions-list.service.gov.uk/"
driver.get(url)
import time
time.sleep(10)
# Locate the dropdown element
dropdown = driver.find_element(By.XPATH, """/html/body/app-root/div/app-search-root/div/div/pagination/div/div/select""")

# Create a Select object
select = Select(dropdown)

# Select an option by visible text
select.select_by_index(3)

time.sleep(10)


for i in range(1,24,1):
    time.sleep(10)
    elements = driver.find_elements(By.CSS_SELECTOR, 'td.govuk-table__cell')
    time.sleep(4)
    for i in range(0,len(elements),9):
        unique_id_list.append(elements[i].text)
        ofsi_group_id_list.append(elements[i+1].text)
        name_list.append(elements[i+2].text)
        regime_name_list.append(elements[i+3].text)
        type_list.append(elements[i+4].text)
        designation_source_list.append(elements[i+5].text)
        date_designated_list.append(elements[i+6].text)
        sanctions_imposed_list.append(elements[i+7].text)
    if(i == 90):
        break
    time.sleep(2)
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/app-root/div/app-search-root/div/div/pagination/div/div/button[3]""")))
    time.sleep(3)
    button.click()


import pandas as pd
df = pd.DataFrame({"unique_iD" : unique_id_list, 
                    "OFSI_group_id" : ofsi_group_id_list,
                    "Name" : name_list,
                    "regime_name" : regime_name_list,
                    "type" : type_list,
                    "designation_source" : designation_source_list,
                    "date_designated" : date_designated_list,
                    "sanctions_imposed" : sanctions_imposed_list})


df.to_excel("UK_Sanctions_list.xlsx")
    
df.to_csv("UK_Sanctions_list.csv")





