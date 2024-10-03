
import requests
from bs4 import BeautifulSoup
import time


id_list = []
name_list = []
father_name_list = []
CNIC_list = []
district_list = []
province_list = []


link_condition_string = "/Denotified?counter=7303&page="


url = "https://nfs.punjab.gov.pk/Denotified"

for b in range(1,75,1):

    # url = "https://nfs.punjab.gov.pk/Denotified"
    

    r = requests.get(url)

    time.sleep(5)
    soup = BeautifulSoup(r.text, "lxml")

    table  = soup.find("table")

    table_body = table.find_all("tr")

    td = []
    for i in table_body:
        temp_table_data = i.find_all("td")
        for j in temp_table_data:
            td.append(j.text)

    for i in range(0,len(td),6):
        id_list.append(td[i])
        name_list.append(td[i+1])
        father_name_list.append(td[i+2])
        CNIC_list.append(td[i+3])
        district_list.append(td[i+4])
        province_list.append(td[i+5])

    links = []
    if(b!=74):
        link  = soup.find_all("a")
        links = []
        for i in link:
            links.append(i.get("href"))
        
        for i in links:
            if(i == str(link_condition_string + str(b+1))):
                url = "https://nfs.punjab.gov.pk" + i
                print(url)
                break



import pandas as pd

df = pd.DataFrame({"id" : id_list,
                   "name" : name_list,
                   "father_name" : father_name_list,
                   "CNIC" : CNIC_list,
                   "district" : district_list,
                   "province" : province_list})


df.to_csv("NACTA.csv")
df.to_excel("NACTA.xlsx")