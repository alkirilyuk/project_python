import vk_api
import config
import pandas as pd

token = vk_api.VkApi(token= config.vk_token)
vk = token.get_api()


response = vk.groups.getMembers(group_id = "1", fields = " bdate, sex, country, education,contacts", count = 100)
data_for_import = response.get( 'items' )

first_name_for_import=[]
last_name_for_import=[]
sex_for_import=[]
bdate_for_import=[]
education_for_import=[]

for i in range(0,len(data_for_import)):
    first_name_for_import.append(data_for_import[i].get('first_name'))
    last_name_for_import.append(data_for_import[i].get('last_name'))
    sex_for_import.append(data_for_import[i].get('sex'))
    bdate_for_import.append(data_for_import[i].get('bdate'))
    education_for_import.append(data_for_import[i].get('university_name'))
