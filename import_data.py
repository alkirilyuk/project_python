import cx_Oracle
import os
import config
from pprint import pprint
import vk_connect

LOCATION_ORACLE = r"C:\Users\Алёна Кирилюк\Downloads\instantclient_19_8"
os.environ["PATH"] = LOCATION_ORACLE + ";" + os.environ["PATH"]

conn = cx_Oracle.connect(
    config.user, 
    config.password, 
    config.dsn, 
    encoding=config.encoding)

curs = conn.cursor()
for first_name, last_name, sex, bdate, education in zip(vk_connect.first_name_for_import, vk_connect.last_name_for_import, vk_connect.sex_for_import, vk_connect.bdate_for_import, vk_connect.education_for_import):
    curs.execute("INSERT INTO VK_CONTENT (FIRST_NAME, LAST_NAME, SEX, BDATE, EDUCATION) VALUES (:FIRST_NAME, :LAST_NAME, :SEX, :BDATE, :EDUCATION)", 
    FIRST_NAME=first_name, LAST_NAME=last_name, SEX= sex, BDATE=bdate, EDUCATION = education)
conn.commit()
print('Import success!')
conn.close()
