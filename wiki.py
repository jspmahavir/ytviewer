import requests
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import gmtime, sleep, strftime, time

def get_youtube_url(youtube_url, timeout=10):
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.get(youtube_url)
    return driver.title

video_urls = [
    "https://www.youtube.com/watch?v=tPEE9ZwTmy0",
    "https://www.youtube.com/watch?v=teHfNsXbtDc"
]

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in video_urls:
        futures.append(executor.submit(get_youtube_url, youtube_url=url))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())