from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os
from time import sleep 




email = "jeffysam02@gmail.com"
passwd = "myfriendisgod"


# url = "https://www.facebook.com/groups/870250880025270/"

url = "https://mobile.facebook.com/groups/870250880025270?refid=27"

option = webdriver.ChromeOptions()
option.add_argument("-incognito")

driver = webdriver.Chrome(executable_path='chromedriver',chrome_options=option)


# driver = webdriver.Firefox()
driver.implicitly_wait(30)

driver.get(url)

#driver.find_element_by_id('email')
username =  driver.find_element_by_id('m_login_email')
username.send_keys(email)


#driver.find_element_by_id('pass')
password =driver.find_element_by_id('m_login_password')
password.send_keys(passwd)


#driver.find_element_by_name('loginbutton')
login = driver.find_element_by_name('login')
login.click()



# post = driver.find_elements_by_xpath("//div[@class='_5pbx userContent _3576']")
driver.implicitly_wait(20)

# driver.find_element_by_xpath('//*[@id="feedback_inline_897834713933553"]/div[1]/a').click()

# seen = driver.find_elements_by_class_name('_4mo')

# seen_name = [x.text for x in seen]

# print(seen_name)

# driver.find_element_by_xpath('//*[@id="u_0_4"]').click()

# unseen = driver.find_elements_by_class_name('_4mo')

# unseen_name = [x.text for x in seen]

# print(unseen_name)

seen_data = driver.find_elements_by_xpath("//div[@class='_52j9 _52jg _2sba _2sba _5qux']/a")

print(seen_data)

for i in seen_data:
    link = i.get_attribute("href")

    driver.execute_script("window.open('');")
    sleep(3)

    driver.switch_to.window(driver.window_handles[1])
    driver.get(link)
    sleep(3)
    seen = driver.find_elements_by_class_name('_4mo')
    seen_name = [x.text for x in seen]
    print(seen_name)
    print()
    driver.close()
    sleep(3)

    driver.switch_to.window(driver.window_handles[0])



sleep(5)

driver.quit() 

