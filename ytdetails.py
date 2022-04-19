# from selenium.common.exceptions import TimeoutException
# from django.db import router
# from  demo8  import mycursor ,mydb

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import concurrent.futures
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import flask


# driver = webdriver.Chrome()

data = ['https://www.youtube.com/watch?v=OQij6GB2FA8'] 

# for row in mycursor.fetchall():
#     if row not in data:
#         data.append(row)

app = flask.Flask(__name__)

class ytdetails:
    
    # app.config["DEBUG"] = True

    # @app.route('/get_youtube_page_existence/<youtube_page_url>', methods=['GET'])      

    def get_youtube_page_existence(youtube_page_url):
    # response = requests.get(url=youtube_page_url)
        driver = webdriver.Chrome()
        driver.get(youtube_page_url)
        
        wait = WebDriverWait(driver, 10)
        view =wait.until(EC.visibility_of_element_located(
            (By.XPATH,"""//*[@id="count"]/ytd-video-view-count-renderer/span[1]"""))).text
        likes = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'ytd-toggle-button-renderer.style-text:nth-child(1) > a:nth-child(1) > yt-formatted-string:nth-child(2)'))).text
        subscribe = wait.until(EC.visibility_of_element_located(
            (By.XPATH,"""//*[@id="owner-sub-count"]"""))).text
        channel = wait.until(EC.visibility_of_element_located(
            (By.XPATH,"""//*[@id="text-container"]"""))).text
        title1 = wait.until(EC.visibility_of_element_located(
            (By.XPATH,"""//*[@id="container"]/h1"""))).text
        uploaddate = wait.until(EC.visibility_of_element_located(
            (By.XPATH,"""//*[@id="info-strings"]/yt-formatted-string"""))).text
  
   
        time.sleep(5)
        print(view, likes, subscribe, channel, title1, uploaddate)

        sql1 = "UPDATE app SET views = %s, likes = %s, subsc = %s, channel_name = %s, title = %s, dics = %s,stauts ='complate' WHERE urls = %s"
        val1 = (view, likes, subscribe, channel, title1, uploaddate, youtube_page_url)
        
        # mycursor.execute(sql1 ,val1)

        # mydb.commit()
        print("inserted....")

        # return fun.get_youtube_page_existence(router)
    
    def startPoint(): 
        data1=[]
        for x in data:
            data1.append(x["urls"])
        print(data1)

        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     futures = []
        #     for url in data1:
        #         futures.append(executor.submit(get_youtube_page_existence, youtube_page_url=url))
        #     for future in concurrent.futures.as_completed(futures):
        #         time.sleep(20)

    

    if __name__ == '__main__':
        @app.route('/getdata', methods=['GET'])

        def getdata():
            print("Hello")
            yt = ytdetails()
            print(yt)
            # yt.startPoint()
            return {"test":"asd"}

    app.run()
