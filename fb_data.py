import json

import csv

import pandas as pd

import facebook

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

import re

from tabulate import tabulate

from time import sleep 




def main():
    token = "EAACOfoHQz3sBAOJFZC3M1ZCGw4n0DfbEEWwd9t0LlL35NKhmRnABM5ibZAygjRx6lXF5vZBLtEgZB8BEQeyhb4TaqTLnjr3AKMO8xOiUJcLuNXkZAFt2dXru8FjM4lFgSxnm4JHSwGsgZA2hzZByFAShyWuQZAURgirpKcHU6BZBo8L85fnEmxH1a4QBEPDQ4I12nfugdvNsCZADAKQVyrHdGw5snuqCSJwBuFKvtEudxUdoQZDZD"
    node = "397007524493560" #group_id 

    graph = facebook.GraphAPI(token)

    fields = ['videos{comments}']

    videos = graph.get_object(node,fields=fields)

    comment_data = videos['videos']['data']

    # print(json.dumps(videos['videos']['data'],indent=4))

    #code for structured csv
    email = "jeffysam02@gmail.com"
    passwd = "myfriendisgod"

    d = {}
    url = "https://mobile.facebook.com/groups/397007524493560?refid=27"
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='chromedriver',chrome_options=option)
    driver.implicitly_wait(30)
    driver.get(url)
    username =  driver.find_element_by_id('m_login_email')
    username.send_keys(email)
    password =driver.find_element_by_id('m_login_password')
    password.send_keys(passwd)
    login = driver.find_element_by_name('login')
    login.click()
    driver.implicitly_wait(20)

    def get_name(comment_id):

        if(comment_id in d):

            return d[comment_id]

        else:
            url_2 = f"https://mobile.facebook.com/{comment_id}"
            driver.execute_script("window.open('');")
            sleep(10)
            driver.switch_to.window(driver.window_handles[1])
            driver.get(url_2)
            sleep(10)
            driver.implicitly_wait(30)
            names = driver.find_elements_by_class_name('_2b05')
            names_text = [x.text for x in names]
            comment_ids = driver.find_elements_by_xpath("//div[@class='_2b06']/div[@data-sigil='comment-body']")
            for i,j in enumerate(comment_ids):
                d[j.get_attribute('data-commentid')] = names_text[i]

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            return d.get(comment_id,None)









    with open('results2.csv','w',encoding='utf-8') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(["Facebook Post ID","Facebook Comment ID","Facebook Comment Content","Posted By","Created Date and Time"])

        for i in comment_data:

            if("comments" in i):

                for j in i["comments"]['data']:

                    # print(i['id'],j['id'],j['message'],type(j['id']),j['created_time'])
                    writer.writerow([i['id'],j['id'],j['message'],get_name(j['id']),j['created_time']])


            else:
                writer.writerow([i['id'],"Na N","Na N","Na N"])





    with open('data.json','w') as f:
        json.dump(videos['videos']['data'],f)

    df = pd.read_json('data.json')
    
    df.to_csv("results.csv")


if __name__ == "__main__":
  main()
