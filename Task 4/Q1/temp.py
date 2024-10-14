import pandas as pd
import requests
from bs4 import BeautifulSoup

r = requests.get("https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/CONSOLIDATED.XML")

with open('CONSOLIDATED.txt', 'r') as file:
    text = file.read()

soup = BeautifulSoup(text,"lxml")

sdn_list = soup.find_all("sdnlist")

# User data
uid_list = []
first_name_list = []
last_name_list = []
sdn_type_list = []
program_list = []

# also known as
aka1_uid_list = []
aka1_type_list = []
aka1_category_list = []
aka1_first_name_list = []
aka1_last_name_list = []

# also known as
aka2_uid_list = []
aka2_type_list = []
aka2_category_list = []
aka2_first_name_list = []
aka2_last_name_list = []

# Date of Birth
dob_uid_list = []
dob_list = []
dob_main_entry_list = []

# Place of birth
pob_uid_list = []
pob_list = []
pob_main_entry_list = []

# address
address_uid_list = []
address_city_list = []
address_state_or_province_list = []
address_country_list = []

for i in sdn_list:
    sdn_entry = i.find_all("sdnentry")
    # print(sdn_entry)
    
    for k in sdn_entry:
        temp_uid = k.find("uid")
        if(temp_uid!=None):
            uid_list.append(temp_uid.text)
        else:
            uid_list.append(None)
        
        temp_first_name = k.find("firstname")
        if(temp_first_name!=None):
            first_name_list.append(temp_first_name.text)
        else:
            first_name_list.append(None)
            
        temp_last_name = k.find("lastname")
        if(temp_last_name != None):
            last_name_list.append(temp_last_name.text)
        else:
            last_name_list.append(None)

        temp_sdn_type = k.find("sdntype")
        if(temp_sdn_type!=None):
            sdn_type_list.append(temp_sdn_type.text)
        else:
            sdn_type_list.append(None)

        temp_program_list = k.find("programlist")
        if(temp_program_list !=None):
            temp_program = temp_program_list.find("program")
            if(temp_program != None):
                program_list.append(temp_program.text)
            else:
                program_list.append(None)
        else:
            program_list.append(None)

        # address_uid_list = []
        # address_city_list = []
        # address_state_or_province_list = []
        # address_country_list = []
        temp_address_list = k.find("addresslist")
        if(temp_address_list!=None):
            temp_address = temp_address_list.find("address")
            temp_address_uid = temp_address.find("uid")
            temp_address_city = temp_address.find("city")
            temp_address_state_or_province = temp_address.find("stateorprovince")
            temp_address_country = temp_address.find("country")

            if(temp_address_uid != None):
                address_uid_list.append(temp_address_uid.text)
            else:
                address_uid_list.append(None)

            if(temp_address_city != None):
                address_city_list.append(temp_address_city.text)
            else:
                address_city_list.append(None)
            if(temp_address_state_or_province !=None):
                address_state_or_province_list.append(temp_address_state_or_province.text)
            else:
                address_state_or_province_list.append(None)
            if(temp_address_country != None):
                address_country_list.append(temp_address_country.text)
            else:
                address_country_list.append(None)
        else:
            address_uid_list.append(None)
            address_city_list.append(None)
            address_state_or_province_list.append(None)
            address_country_list.append(None)
            

        
        temp_aka_list = k.find("akalist")
        # print(temp_aka_list)
        if(temp_aka_list!=None):
            temp_akas = temp_aka_list.find_all("aka")
            len_temp_akas = len(temp_akas)
            if(len_temp_akas<2):
                if(len_temp_akas==1):
                    
                    # print("elif condition", len_temp_akas)
                    temp_akas = temp_akas[0]
                    temp_aka1_uid = temp_akas.find("uid")
                    if(temp_aka1_uid!=None):
                        aka1_uid_list.append(temp_aka1_uid.text)
                    else:
                        aka1_uid_list.append(None)
                    temp_aka1_type = temp_akas.find("type")
                    if(temp_aka1_type!=None):
                        aka1_type_list.append(temp_aka1_type.text)
                    else:
                        aka1_type_list.append(None)
                    temp_aka1_category = temp_akas.find("category")
                    if(temp_aka1_category!=None):
                        aka1_category_list.append(temp_aka1_category.text)
                    else:
                        aka1_category_list.append(None)
                    temp_aka1_first_name = temp_akas.find("firstname")
                    if(temp_aka1_first_name !=None):
                        aka1_first_name_list.append(temp_aka1_first_name.text)
                    else:
                        aka1_first_name_list.append(None)
                    temp_aka1_last_name = temp_akas.find("lastname")
                    if(temp_aka1_last_name!=None):
                        aka1_last_name_list.append(temp_aka1_last_name.text)
                    else:
                        aka1_last_name_list.append(None)

                    aka2_uid_list.append(None)
                    aka2_type_list.append(None)
                    aka2_category_list.append(None)
                    aka2_first_name_list.append(None)
                    aka2_last_name_list.append(None)
            if(len_temp_akas>=2):
                # print("else condition", len_temp_akas)
                counter = 0
                
                for j in temp_akas:
                      
                    if(counter==0):
                        temp_aka1_uid = j.find("uid")
                        if(temp_aka1_uid!=None):
                            aka1_uid_list.append(temp_aka1_uid.text)
                        else:
                            aka1_uid_list.append(None)
                        temp_aka1_type = j.find("type")
                        if(temp_aka1_type!=None):
                            aka1_type_list.append(temp_aka1_type.text)
                        else:
                            aka1_type_list.append(None)
                        temp_aka1_category = j.find("category")
                        if(temp_aka1_category!=None):
                            aka1_category_list.append(temp_aka1_category.text)
                        else:
                            aka1_category_list.append(None)
                        temp_aka1_first_name = j.find("firstname")
                        if(temp_aka1_first_name !=None):
                            aka1_first_name_list.append(temp_aka1_first_name.text)
                        else:
                            aka1_first_name_list.append(None)
                        temp_aka1_last_name = j.find("lastname")
                        if(temp_aka1_last_name!=None):
                            aka1_last_name_list.append(temp_aka1_last_name.text)
                        else:
                            aka1_last_name_list.append(None)
                            
                    elif(counter==1):
                        temp_aka2_uid = j.find("uid")
                        if(temp_aka2_uid!=None):
                            aka2_uid_list.append(temp_aka2_uid.text)
                        else:
                            aka2_uid_list.append(None)
                        temp_aka2_type = j.find("type")
                        if(temp_aka2_type!=None):
                            aka2_type_list.append(temp_aka2_type.text)
                        else:
                            aka2_type_list.append(None)
                        temp_aka2_category = j.find("category")
                        if(temp_aka2_category!=None):
                            aka2_category_list.append(temp_aka2_category.text)
                        else:
                            aka2_category_list.append(None)
                        temp_aka2_first_name = j.find("firstname")
                        if(temp_aka2_first_name !=None):
                            aka2_first_name_list.append(temp_aka2_first_name.text)
                        else:
                            aka2_first_name_list.append(None)
                        temp_aka2_last_name = j.find("lastname")
                        if(temp_aka2_last_name!=None):
                            aka2_last_name_list.append(temp_aka2_last_name.text)
                        else:
                            aka2_last_name_list.append(None)
                        # print(temp_aka2_uid, temp_aka2_type, temp_aka2_category,temp_aka2_first_name,temp_aka2_last_name)
                    elif(counter>2):
                        break
                    counter = counter+1           

        else:

            aka1_uid_list.append(None)
            aka1_type_list.append(None)
            aka1_category_list.append(None)
            aka1_first_name_list.append(None)
            aka1_last_name_list.append(None)

            aka2_uid_list.append(None)
            aka2_type_list.append(None)
            aka2_category_list.append(None)
            aka2_first_name_list.append(None)
            aka2_last_name_list.append(None)

                    
            

        
        
            
        temp_dob_list = k.find("dateofbirthlist")
        if(temp_dob_list!=None): 
            temp_dob_item = temp_dob_list.find("dateofbirthitem")
            temp_dob_uid = temp_dob_item.find("uid")
            temp_dob = temp_dob_item.find("dateofbirth")
            temp_dob_main_entry = temp_dob_item.find("mainentry")

            if(temp_dob_uid!=None):
                dob_uid_list.append(temp_dob_uid.text)
            else:
                dob_uid_list.append(None)
            if(temp_dob!=None):
                dob_list.append(temp_dob.text)
            else:
                dob_list.append(None)
            if(temp_dob_main_entry!=None):
                dob_main_entry_list.append(temp_dob_main_entry.text)
            else:
                dob_main_entry_list.append(None)
            
        else:
            temp_dob_item = None
            temp_dob_uid = None
            temp_dob = None
            temp_dob_main_entry = None

            dob_uid_list.append(temp_dob_uid)
            dob_list.append(temp_dob)
            dob_main_entry_list.append(temp_dob_main_entry)
        
                

        # print(temp_dob_uid ,temp_dob , temp_dob_main_entry )

        temp_pob_list = k.find("placeofbirthlist")
        if(temp_pob_list!=None):
            temp_pob_birth_item = temp_pob_list.find("placeofbirthitem")
            temp_pob_uid = temp_pob_birth_item.find("uid")
            temp_pob = temp_pob_birth_item.find("placeofbirth")
            temp_pob_main_entry = temp_pob_birth_item.find("mainentry")

            if(temp_pob_uid!=None):
                pob_uid_list.append(temp_pob_uid.text)
            else:
                pob_uid_list.append(None)
            if(temp_pob != None):
                pob_list.append(temp_pob.text)
            else:
                pob_list.append(None)
            if(temp_pob_main_entry != None):
                pob_main_entry_list.append(temp_pob_main_entry.text)
            else:
                pob_main_entry_list.append(None)

        else:
            temp_pob_birth_item = None
            temp_pob_uid = None
            temp_pob = None
            temp_pob_main_entry = None
            pob_uid_list.append(temp_pob_uid)
            pob_list.append(temp_pob)
            pob_main_entry_list.append(temp_pob_main_entry)

    
        
        # print(temp_pob_uid ,temp_pob , temp_pob_main_entry )

        
    

df = pd.DataFrame({"uid" : uid_list,
                  "first_name" : first_name_list,
                  "last_name" : last_name_list,
                  "sdn_type" : sdn_type_list,
                  "program" : program_list,
                  "aka1_uid" : aka1_uid_list,
                  "aka1_first_name" : aka1_first_name_list,
                  "aka1_last_name" : aka1_last_name_list,
                  "aka1_type" : aka1_type_list,
                  "aka1_category" : aka1_category_list,
                  "aka2_uid" : aka2_uid_list,
                  "aka2_first_name" : aka2_first_name_list,
                  "aka2_last_name" : aka2_last_name_list,
                  "aka2_type" : aka2_type_list,
                  "aka2_category" : aka2_category_list,
                  "DOB_uid" : dob_uid_list,
                  "DOB" : dob_list,
                  "DOB_main_entry" : dob_main_entry_list,
                  "POB_uid" : pob_uid_list,
                  "POB" : pob_list,
                  "POB_main_entry" : pob_main_entry_list,
                  "address_uid" : address_uid_list,
                  "city" : address_city_list,
                  "state_or_province" : address_state_or_province_list,
                  "country" : address_country_list})


df.to_excel("consolidated.xlsx")

df.to_csv("consolidated.csv")