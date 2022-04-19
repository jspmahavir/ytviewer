import concurrent.futures.thread
import hashlib
import io
import json
import logging
import os
import platform
import queue
from re import L, split
from sched import scheduler
import shutil
import sqlite3
import subprocess
import sys
from threading import local
import zipfile

from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import closing
from datetime import datetime
from glob import glob
from random import choice, choices, randint, shuffle, uniform
from time import gmtime, sleep, strftime, time

import requests
import undetected_chromedriver as uc
# import undetected_chromedriver.v2 as uc
from fake_headers import Headers, browsers
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver.patcher import Patcher 
from flask import Flask, jsonify, render_template, request
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import website
from config import create_config
app = Flask(__name__)


log = logging.getLogger('werkzeug')



log.disabled = False

# Local Url # Return json Response
scheduleLogAPI = 'http://192.168.1.19:8888/yt-admin/scheduleapi/scheduleLogEntry'
statisticsLogAPI = 'http://192.168.1.19:8888/yt-admin/proxyapi/saveYTStatistics'

os.system("")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.OKGREEN + """

Yb  dP  dP"Yb  88   88 888888 88   88 88""Yb 888888                   
 YbdP  dP   Yb 88   88   88   88   88 88__dP 88__                     
  8P   Yb   dP Y8   8P   88   Y8   8P 88""Yb 88""                     
 dP     YbodP  `YbodP'   88   `YbodP' 88oodP 888888  

                        Yb    dP 88 888888 Yb        dP 888888 88""Yb 
                         Yb  dP  88 88__    Yb  db  dP  88__   88__dP 
                          YbdP   88 88""     YbdPYbdP   88""   88"Yb  
                           YP    88 888888    YP  YP    888888 88  Yb 
""" + bcolors.ENDC)

SCRIPT_VERSION = '1.6.2'

proxy = None
driver = None
status = None
server_running = False

urls = []
queries = []
hash_urls = None
hash_queries = None
start_time = None

driver_list = []
view = []
duration_dict = {}
checked = {}
console = []
threads = 0
proxyCollection = None
logData = []
postData = []
scheduleLogId = 0

WEBRTC = os.path.join('extension', 'webrtc_control.zip')
ACTIVE = os.path.join('extension', 'always_active.zip')
FINGERPRINT = os.path.join('extension', 'fingerprint_defender.zip')
TIMEZONE = os.path.join('extension', 'spoof_timezone.zip')
CUSTOM_EXTENSIONS = glob(os.path.join('extension', 'custom_extension', '*.zip')) + \
    glob(os.path.join('extension', 'custom_extension', '*.crx'))

DATABASE = 'database.db'
DATABASE_BACKUP = 'database_backup.db'

WIDTH = 0
VIEWPORT = ['2560,1440', '1920,1080', '1440,900',
            '1536,864', '1366,768', '1280,1024', '1024,768']

CHROME = ['{8A69D345-D564-463c-AFF1-A69D9E530F96}',
          '{8237E44A-0054-442C-B6B6-EA0509993955}',
          '{401C381F-E0DE-4B85-8BD8-3F3F14FBDA57}',
          '{4ea16ac7-fd5a-47c3-875b-dbf4a2008c20}']

REFERERS = ['https://www.google.com/', 'https://www.google.com/', 'https://www.google.com/',
            'https://www.google.com/', 'https://www.google.com/', '']

COMMANDS = [Keys.UP, Keys.DOWN, 'k', 'j', 'l', 't', 'c']

website.console = console
website.database = DATABASE

link = 'https://gist.githubusercontent.com/MShawon/29e185038f22e6ac5eac822a1e422e9d/raw/versions.txt'

output = requests.get(link, timeout=60).text
chrome_versions = output.split('\n')

browsers.chrome_ver = chrome_versions



def monkey_patch_exe(self):
    linect = 0
    replacement = self.gen_random_cdc()
    replacement = f"  var key = '${replacement.decode()}_';\n".encode()
    with io.open(self.executable_path, "r+b") as fh:
        for line in iter(lambda: fh.readline(), b""):
            if b"var key = " in line:
                fh.seek(-len(line), 1)
                fh.write(replacement)
                linect += 1
        return linect


Patcher.patch_exe = monkey_patch_exe


class UrlsError(Exception):
    pass


class SearchError(Exception):
    pass


class CaptchaError(Exception):
    pass


class QueryError(Exception):
    pass


def timestamp():
    date_fmt = datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    return bcolors.OKGREEN + f'[{date_fmt}] '

def getTime():
    now = datetime.now()
    curremtDateTime = now.strftime("%d/%m/%Y %H:%M:%S")
    return curremtDateTime

def download_driver():
    OSNAME = platform.system()

    print(bcolors.WARNING + 'Getting Chrome Driver...' + bcolors.ENDC)

    if OSNAME == 'Linux':
        OSNAME = 'lin'
        EXE_NAME = ""
        with subprocess.Popen(['google-chrome', '--version'], stdout=subprocess.PIPE) as proc:
            version = proc.stdout.read().decode('utf-8').replace('Google Chrome', '').strip()
    elif OSNAME == 'Darwin':
        OSNAME = 'mac'
        EXE_NAME = ""
        process = subprocess.Popen(
            ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'], stdout=subprocess.PIPE)
        version = process.communicate()[0].decode(
            'UTF-8').replace('Google Chrome', '').strip()
    elif OSNAME == 'Windows':
        OSNAME = 'win'
        EXE_NAME = ".exe"
        version = None
        try:
            process = subprocess.Popen(
                ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
            )
            version = process.communicate()[0].decode(
                'UTF-8').strip().split()[-1]
        except:
            for i in CHROME:
                for j in ['opv', 'pv']:
                    try:
                        command = [
                            'reg', 'query', f'HKEY_LOCAL_MACHINE\\Software\\Google\\Update\\Clients\\{i}', '/v', f'{j}', '/reg:32']
                        process = subprocess.Popen(
                            command,
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
                        )
                        version = process.communicate()[0].decode(
                            'UTF-8').strip().split()[-1]
                    except:
                        pass

        if not version:
            print(bcolors.WARNING +
                  "Couldn't find your Google Chrome version automatically!" + bcolors.ENDC)
            version = input(bcolors.WARNING +
                            'Please input your google chrome version (ex: 91.0.4472.114) : ' + bcolors.ENDC)
    else:
        print('{} OS is not supported.'.format(OSNAME))
        sys.exit()

    try:
        with open('version.txt', 'r') as f:
            previous_version = f.read()
    except:
        previous_version = '0'

    with open('version.txt', 'w') as f:
        f.write(version)

    if version != previous_version:
        try:
            os.remove(f'chromedriver{EXE_NAME}')
        except:
            pass

    major_version = version.split('.')[0]

    uc.TARGET_VERSION = major_version

    uc.install()

    return OSNAME, EXE_NAME


def copy_drivers(total):
    cwd = os.getcwd()
    current = os.path.join(cwd, f'chromedriver{EXE_NAME}')
    os.makedirs('patched_drivers', exist_ok=True)
    for i in range(total+1):
        try:
            destination = os.path.join(
                cwd, 'patched_drivers', f'chromedriver_{i}{EXE_NAME}')
            shutil.copy(current, destination)
        except Exception as e:
            print(e)
            pass


def create_database():
    with closing(sqlite3.connect(DATABASE)) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS
            statistics (date TEXT, view INTEGER)""")

            connection.commit()

    try:
        # remove previous backup if exists
        os.remove(DATABASE_BACKUP)
    except:
        pass

    try:
        # backup latest database
        shutil.copy(DATABASE, DATABASE_BACKUP)
    except:
        pass

def update_data_to_mongo(data,collectionName,type):
    create_collection_mongo(collectionName)
    if type == "single":
        insert_one_record(data)
    else:
        insert_many_record(data)

def create_mongo_database():
    #create connection with mongo
    global mongoclient
    global db
    mongoclient = MongoClient('localhost', 27017)
    #create database if not exist
    # db = mongoclient['youtube_viewer']
    db = mongoclient['demoDB']

def create_collection_mongo(collectionName):
    global mongoclient
    global mycol
    global db
    print("create table/collection in mongo")
    mycol = db[collectionName]

def insert_one_record(insertObj):
    global mycol
    print("insert into mongo code here")
    mycol.insert_one(insertObj)

def insert_many_record(insertObj):
    global mycol
    print("insert multiple data in mongo code here")
    mycol.insert_many(insertObj)

def update_record():
    global mycol
    print("update record code here")

def find_one_data():
    # global x
    global mycol
    print("find data")
    x = mycol.find_one()
    print(x)

def find_all_data():
    print("find all data")
    for x in mycol.find():
        print(x)

def update_database():
    today = str(datetime.today().date())
    with closing(sqlite3.connect(DATABASE, timeout=threads*10)) as connection:
        with closing(connection.cursor()) as cursor:
            try:
                cursor.execute(
                    "SELECT view FROM statistics WHERE date = ?", (today,))
                previous_count = cursor.fetchone()[0]
                cursor.execute("UPDATE statistics SET view = ? WHERE date = ?",
                               (previous_count + 1, today))
            except:
                cursor.execute(
                    "INSERT INTO statistics VALUES (?, ?)", (today, 0),)

            connection.commit()

def insert_collection_record(collectionName, insertObj):
    global mongoclient
    global db
    tmpCollection = db[collectionName]
    _id = tmpCollection.insert_one(insertObj)
    print('collection inserted')
    return _id.inserted_id

def update_collection_record(collectionName, filter, updateObj):
    global mongoclient
    global db
    tmpCollection = db[collectionName]
    newvalues = { "$set": updateObj }
    tmpCollection.update_one(filter, newvalues)
    print('collection updated')

def copy_collection_record(oldCollection, newCollection, filter):
    global mongoclient
    global db
    tmpCollectionOld = db[oldCollection]
    tmpCollectionNew = db[newCollection]
    tmpArr = tmpCollectionOld.find(filter, { "_id": 0})
    for record in tmpArr:
        tmpCollectionNew.insert_one(record)
        tmpCollectionOld.delete_one(filter)
    print('collection copied')

def drop_collection_mongo(collectionName):
    global mongoclient
    global db
    tmpCollection = db[collectionName]
    tmpCollection.drop()


def call_stats(logs, type):
    global finalString
    if type == 'json':
        finalString = json.dumps(logs)
    elif type == 'object':
        finalString = str(logs)

    # print()
    with open("views.json", "a") as outfile:
        outfile.write("---------------------------------------------------------\n")
        outfile.write("Date Time: " + str(timestamp()))
        outfile.write(finalString + "\n")
        outfile.write("---------------------------------------------------------\n")
        
def create_html(text_dict):
    global console

    if len(console) > 50:
        console.pop(0)

    date_fmt = f'<span style="color:#23d18b"> [{datetime.now().strftime("%d-%b-%Y %H:%M:%S")}] </span>'
    str_fmt = ''.join(
        [f'<span style="color:{key}"> {value} </span>' for key, value in text_dict.items()])
    html = date_fmt + str_fmt

    console.append(html)


def load_url():
    print(bcolors.WARNING + 'Loading urls...' + bcolors.ENDC)

    with open('urls.txt', encoding="utf-8") as fh:
        links = [x.strip() for x in fh if x.strip() != '']

    print(bcolors.OKGREEN +
          f'{len(links)} url loaded from urls.txt' + bcolors.ENDC)

    return links


def load_search(search_text):
    print(bcolors.WARNING + 'Loading queries...' + bcolors.ENDC)
    global view
    global scriptExecution
    view = []
    scriptExecution = True
    # with open('search.txt', encoding="utf-8") as fh:
    #     search = [[y.strip() for y in x.strip().split('::::')]
    #               for x in fh if x.strip() != '' and '::::' in x]

    # print('search', search)
    
    search_text = split('::::',search_text)
    st = [search_text[0].strip()]
    st.append(search_text[1].strip())
    st.append(search_text[2].strip())

    final_search_text = [st]
    print(final_search_text)

    # search_text = [[search_text.strip() for search_text in search_text.strip().split('::::')]
    #               for x in fh if x.strip() != '' and '::::' in x]
                
    # print('search text', search_text)

    # print(bcolors.OKGREEN +
    #       f'{len(search)} query loaded from search.txt' + bcolors.ENDC)
    search = final_search_text
    return search

def gather_proxy():
    proxies = []
    print(bcolors.OKGREEN + 'Scraping proxies ...' + bcolors.ENDC)

    link_list = ['https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
                 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
                 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
                 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
                 'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt',
                 'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt']

    for link in link_list:
        response = requests.get(link)
        output = response.content.decode()
        proxy = output.split('\n')
        proxies = proxies + proxy
        print(bcolors.OKGREEN +
              f'{len(proxy)} proxies gathered from {link}' + bcolors.ENDC)
    
    proxies = list(filter(None, proxies))
    shuffle(proxies)

    return proxies

def load_proxy_db():
    global mycol
    print("find proxy from DB")
    proxies = []
    y = ''
    for x in mycol.find():
        if category == 'f':
            y = x['proxy_url'] + ':' + str(x["proxy_port"])
        elif category == 'p':
            y = x['username'] + ':' + x['password'] + '@' + x['proxy_url'] + ':' +str(x["proxy_port"])
        proxies.append(y)
    shuffle(proxies)

    return proxies

def load_proxy(proxyData):
    proxies = []

    # with open(filename, encoding="utf-8") as fh:
    #     loaded = [x.strip() for x in fh if x.strip() != '']

    # for lines in loaded:
    #     if lines.count(':') == 3:
    #         split = lines.split(':')
            
    #         lines = f'{split[2]}:{split[-1]}@{split[0]}:{split[1]}'
    #     proxies.append(lines)

    for lines in proxyData:
        liness = f'{lines["user"]}:{lines["pass"]}@{lines["ip"]}:{lines["port"]}'
        proxies.append(liness)
    
    proxies = list(filter(None, proxies))
    shuffle(proxies)

    return proxies

def scrape_api(link):
    proxies = []

    response = requests.get(link)
    output = response.content.decode()
    if '\r\n' in output:
        proxy = output.split('\r\n')
    else:
        proxy = output.split('\n')

    for lines in proxy:
        if lines.count(':') == 3:
            split = lines.split(':')
            lines = f'{split[2]}:{split[-1]}@{split[0]}:{split[1]}'
        proxies.append(lines)

    proxies = list(filter(None, proxies))
    shuffle(proxies)

    return proxies


def detect_file_change():
    global hash_urls
    global hash_queries
    global urls
    global queries

    # with open("urls.txt", "rb") as f:
    #     new_hash = hashlib.md5(f.read()).hexdigest()

    # if new_hash != hash_urls:
    #     hash_urls = new_hash
    #     urls = load_url()

    # with open("search.txt", "rb") as f:
    #     new_hash = hashlib.md5(f.read()).hexdigest()

    # if new_hash != hash_queries:
    #     hash_queries = new_hash
    #     queries = load_search()


def check_proxy(agent, proxy, proxy_type):
    if category == 'f':
        headers = {
            'User-Agent': f'{agent}',
        }
        proxy_dict = {
            "http": f"{proxy_type}://{proxy}",
            "https": f"{proxy_type}://{proxy}",
        }
        response = requests.get(
            'https://www.youtube.com/', headers=headers, proxies=proxy_dict, timeout=30)
        status = response.status_code

    else:
        status = 200

    return status


def get_driver(path, agent, proxy, proxy_type, pluginfile):
    options = webdriver.ChromeOptions()
    options.headless = background
    # options.add_argument("--headless")
    options.add_argument(f"--window-size={choice(VIEWPORT)}")
    options.add_argument("--log-level=3")
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': 'en_US,en'})
    options.add_argument(f"user-agent={agent}")
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-features=UserAgentClientHint')
    webdriver.DesiredCapabilities.CHROME['loggingPrefs'] = {
        'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}

    if not background:
        options.add_extension(WEBRTC)
        options.add_extension(FINGERPRINT)
        options.add_extension(TIMEZONE)
        options.add_extension(ACTIVE)

        if CUSTOM_EXTENSIONS:
            for extension in CUSTOM_EXTENSIONS:
                options.add_extension(extension)

    if auth_required:
        proxy = proxy.replace('@', ':')
        proxy = proxy.split(':')
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (proxy[2], proxy[-1], proxy[0], proxy[1])

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        options.add_extension(pluginfile)

    else:
        proxy = proxy.replace('@', ':')
        proxy = proxy.split(':')
        PROXY_HOST = proxy[2]
        PROXY_PORT  = proxy[-1]
        options.add_argument("--proxy-server=%s:%s" % (PROXY_HOST,PROXY_PORT))
        # options.add_argument(f'--proxy-server={proxy_type}://{proxy}')
    
    # proxy_static = "209.205.197.90:10399"
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("no-sandbox")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument(f"user-agent={agent}")
    # chrome_options.add_argument(f'--proxy-server={proxy_type}://{proxy}')
    # chrome_options.add_argument(f'--proxy-server={proxy_static}')


    #open chrome
    driver = webdriver.Chrome(executable_path=path, options=options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    return driver


def personalization(driver):
    search = driver.find_element(By.XPATH,
        f'//button[@aria-label="Turn {choice(["on","off"])} Search customization"]')
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", search)
    search.click()

    history = driver.find_element(By.XPATH,
        f'//button[@aria-label="Turn {choice(["on","off"])} YouTube History"]')
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", history)
    history.click()

    ad = driver.find_element(By.XPATH,
        f'//button[@aria-label="Turn {choice(["on","off"])} Ad personalization"]')
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", ad)
    ad.click()

    confirm = driver.find_element(By.XPATH,'//button[@jsname="j6LnYe"]')
    driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", confirm)
    confirm.click()


def bypass_consent(driver):
    try:
        consent = driver.find_element(By.XPATH,"//button[@jsname='higCR']")
        driver.execute_script("arguments[0].scrollIntoView();", consent)
        consent.click()
        if 'consent' in driver.current_url:
            personalization(driver)
    except:
        consent = driver.find_element(By.XPATH,
            "//input[@type='submit' and @value='I agree']")
        driver.execute_script("arguments[0].scrollIntoView();", consent)
        consent.submit()
        if 'consent' in driver.current_url:
            personalization(driver)


def bypass_signin(driver):
    for _ in range(10):
        sleep(2)
        try:
            nothanks = driver.find_element(By.CLASS_NAME, 
                "style-scope.yt-button-renderer.style-text.size-small")
            nothanks.click()
            sleep(1)
            driver.switch_to.frame(driver.find_element(By.ID,"iframe"))
            iagree = driver.find_element(By.ID,'introAgreeButton')
            iagree.click()
            driver.switch_to.default_content()
        except:
            try:
                driver.switch_to.frame(driver.find_element(By.ID,"iframe"))
                iagree = driver.find_element(By.ID,'introAgreeButton')
                iagree.click()
                driver.switch_to.default_content()
            except:
                pass


def bypass_popup(driver):
    try:
        agree = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@aria-label="Agree to the use of cookies and other data for the purposes described"]')))
        driver.execute_script(
            "arguments[0].scrollIntoViewIfNeeded();", agree)
        sleep(1)
        agree.click()
    except:
        pass


def bypass_other_popup(driver):
    popups = ['Got it', 'Skip trial', 'No thanks', 'Dismiss', 'Not now']
    shuffle(popups)

    for popup in popups:
        try:
            driver.find_element(By.XPATH,
                f"//*[@id='button' and @aria-label='{popup}']").click()
        except:
            pass


def skip_initial_ad(driver, position, video):
    try:
        video_len = duration_dict[video]
        if video_len > 30:
            bypass_popup(driver)
            skip_ad = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "ytp-ad-skip-button-container")))

            print(timestamp() + bcolors.OKBLUE +
                  f"Tried {position} | Skipping Ads..." + bcolors.ENDC)

            create_html({"#23d18b": f"Tried {position} | Skipping Ads..."})

            ad_duration = driver.find_element(By.CLASS_NAME, 
                'ytp-time-duration').get_attribute('innerText')
            ad_duration = sum(x * int(t)
                              for x, t in zip([60, 1], ad_duration.split(":")))
            ad_duration = ad_duration * uniform(.01, .1)
            sleep(ad_duration)
            skip_ad.click()
    except:
        pass


def type_keyword(driver, keyword, retry=False):
    input_keyword = driver.find_element(By.CSS_SELECTOR,'input#search')

    if retry:
        for _ in range(10):
            try:
                input_keyword.click()
                break
            except:
                sleep(5)
                pass

    input_keyword.clear()
    for letter in keyword:
        input_keyword.send_keys(letter)
        sleep(uniform(.1, .4))

    method = randint(1, 2)
    if method == 1:
        input_keyword.send_keys(Keys.ENTER)
    else:
        try:
            driver.find_element(By.XPATH,
                '//*[@id="search-icon-legacy"]').click()
        except:
            driver.execute_script(
                'document.querySelector("#search-icon-legacy").click()')


def search_video(driver, keyword, video_title,video_id):
    i = 0
    try:
        type_keyword(driver, keyword)
    except:
        try:
            bypass_popup(driver)
            type_keyword(driver, keyword, retry=True)
        except:
            return i

    for i in range(1, 11):
        try:
            # section = WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            #     (By.XPATH, f'//ytd-item-section-renderer[{i}]')))
            
            # find_video = section.find_element(By.XPATH,
            #     f'//*[@title="{video_title}"]')
            
            # driver.execute_script(
            #     "arguments[0].scrollIntoViewIfNeeded();", find_video)

            section = WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
                (By.XPATH, f'//ytd-item-section-renderer[{i}]')))
            find_video = section.find_element(By.XPATH,
                f'//a[@href="/watch?v={video_id}"]')
            driver.execute_script(
                "arguments[0].scrollIntoViewIfNeeded();", find_video)

            # driver.find_element(By.XPATH,'//a[@href="/watch?v=OQij6GB2FA8"]').click()
            sleep(2)
            bypass_popup(driver)
            bypass_other_popup(driver)
            call_stats(driver, "object")
            try:
                # section.click()
                driver.find_element(By.XPATH,f'//a[@href="/watch?v={video_id}"]').click()
                
            except:
                driver.execute_script(
                    "arguments[0].click();", section)
            break
        except NoSuchElementException:
            sleep(5)
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
                (By.TAG_NAME, 'body'))).send_keys(Keys.CONTROL, Keys.END)

    return i


def play_video(driver):
    try:
        driver.find_element(By.CSS_SELECTOR,'[title^="Pause (k)"]')

        # Click on LIKE button 
        # sleeping()
        # driver.find_element(By.CSS_SELECTOR,'yt-icon.style-scope.ytd-toggle-button-renderer').click()
    except:
        try:
            driver.find_element(By.CSS_SELECTOR,
                'button.ytp-large-play-button.ytp-button').send_keys(Keys.ENTER)
        except:
            try:
                driver.find_element(By.CSS_SELECTOR,
                    '[title^="Play (k)"]').click()
            except:
                try:
                    driver.execute_script(
                        "document.querySelector('button.ytp-play-button.ytp-button').click()")
                except:
                    pass


def play_music(driver):
    try:
        driver.find_element(By.XPATH,
            '//*[@id="play-pause-button" and @title="Pause"]')
    except:
        try:
            driver.find_element(By.XPATH,
                '//*[@id="play-pause-button" and @title="Play"]').click()
        except:
            driver.execute_script(
                'document.querySelector("#play-pause-button").click()')


def save_bandwidth(driver):
    try:
        driver.find_element(By.CSS_SELECTOR,
            "button.ytp-button.ytp-settings-button").click()
        driver.find_element(By.XPATH,
            "//div[contains(text(),'Quality')]").click()

        random_quality = choices(
            ['144p', '240p', '360p'], cum_weights=(0.7, 0.9, 1.00), k=1)[0]
        quality = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[contains(string(),'{random_quality}')]")))
        driver.execute_script(
            "arguments[0].scrollIntoViewIfNeeded();", quality)
        quality.click()

    except:
        try:
            driver.find_element(By.XPATH,
                '//*[@id="container"]/h1/yt-formatted-string').click()
        except:
            pass


def change_playback_speed(driver):
    if playback_speed == 2:
        driver.find_element(By.ID,'movie_player').send_keys('<'*randint(1, 3))
    elif playback_speed == 3:
        driver.find_element(By.ID,'movie_player').send_keys('>'*randint(1, 3))


def random_command(driver):
    bypass_other_popup(driver)

    option = choices([1, 2], cum_weights=(0.7, 1.00), k=1)[0]
    if option == 2:
        command = choice(COMMANDS)
        if command in ['m', 't', 'c']:
            driver.find_element(By.ID,'movie_player').send_keys(command)
        elif command == 'k':
            if randint(1, 2) == 1:
                driver.find_element(By.ID,'movie_player').send_keys(command)
            driver.execute_script(
                f'document.querySelector("#comments"){choices(["scrollIntoView", "scrollIntoViewIfNeeded"])}();')
            sleep(uniform(4, 10))
            driver.execute_script(
                'document.querySelector("#movie_player").scrollIntoViewIfNeeded();')
        else:
            driver.find_element(By.ID,
                'movie_player').send_keys(command*randint(1, 5))


def quit_driver(driver, pluginfile):
    try:
        driver_list.remove(driver)
    except:
        pass
    driver.quit()

    try:
        os.remove(pluginfile)
    except:
        pass

    status = 400
    return status


def sleeping():
    sleep(5)


def main_viewer(proxy_type, proxy, position, executor):
    try:
        global WIDTH
        global VIEWPORT
        global logData
        global scriptExecution
        global postData
        global scheduleLogId
        postData['scheduleLogId'] = scheduleLogId
        postData[executor] = postData
        # detect_file_change()

        checked[position] = None

        header = Headers(
            browser="chrome",
            os=OSNAME,
            headers=False
        ).generate()
        agent = header['User-Agent']
        url = ''

        if position % 2:
            try:
                method = 1
                url = choice(urls)
                output = url
                if 'music.youtube.com' in url:
                    youtube = 'Music'
                else:
                    youtube = 'Video'
            except:
                raise UrlsError

        else:
            try:
                method = 2
                query = choice(queries)
                keyword = query[0]
                video_title = query[1]
                video_id = query[2]
                # print("video_id =>>>>>>>>>>",video_id)
                # exit()
                url = "https://www.youtube.com"
                output = video_title
                youtube = 'Video'
            except:
                url = choice(urls)
                output = url
                if 'music.youtube.com' in url:
                    youtube = 'Music'
                else:
                    raise SearchError

        if category == 'r' and proxy_api:
            proxies = scrape_api(link=proxy)
            proxy = choice(proxies)

            
        # Initilize stats data for youtube
        
        status = check_proxy(agent, proxy, proxy_type)
        
        proxy_data = proxy.split('@')
        if len(proxy_data) == 2:
            proxy_ip = proxy_data[1].split(':')[0]
            proxy_port = proxy_data[1].split(':')[1]
        elif len(proxy_data) == 1:
            proxy_ip = proxy_data.split(':')[0]
            proxy_port = proxy_data.split(':')[1]

        postData[executor]['agent'] = agent
        postData[executor]['proxy'] = proxy
        postData[executor]['proxy_ip'] = proxy_ip
        postData[executor]['proxy_port'] = proxy_port
        postData[executor]['proxy_type'] = proxy_type
        postData[executor]['video_id'] = video_id

        logData = {
            executor:{
                "agent": postData[executor]['agent'],
                "proxy": postData[executor]['proxy'],
                "proxy_ip": postData[executor]['proxy_ip'],
                "proxy_port": postData[executor]['proxy_port'],
                "proxy_type": postData[executor]['proxy_type'],
                "status": status,
                "ytvideo_id": postData[executor]['video_id'],
                "created_date": getTime(),
                "updated_date": getTime(),
                "status_text": 'In-Progress'
            }
        }
        call_stats(logData[executor], "json")

        # MongoDb database collection
        # insert_collection_record('youtube_stats', logData)

        # scheduleData = {
        #     "schedule_id": postData[executor]['schedule_id'],
        #     "schedule_log_id": "",
        #     "server_master_id": postData[executor]['server_master_id'],
        #     "video_url": postData[executor]['video_id'],
        #     "proxy": postData[executor]['proxy'],
        #     "remarks": "Scheduled..",
        #     "request_type": "Insert",
        #     "data_process_server_ip": "2222",
        #     "data_process_proxy_ip": postData[executor]['proxy_ip'],
        #     "port": postData[executor]['proxy_port'],
        #     "status": "InProgress"
        # }
        # headers = {'Content-type': 'multipart/form-data', 'Accept': 'text/plain'}
        # schedulePost = requests.post(scheduleLogAPI, data=scheduleData).text
        # scheduleLog = json.loads(schedulePost)
        # scheduleLogId = scheduleLog["log_id"]
        # postData[executor]['scheduleLogId'] = scheduleLogId

        # Prepared Filter for update proxy data
        # filter = { 'proxy_ip': proxy_ip, 'proxy_port':proxy_port }

        if status == 200:
            try:
                # MongoDb database collection
                # updateData = {'status_code':status, 'status_text': 'Good Proxy', "updated_date": getTime()}
                # update_collection_record("youtube_stats", filter, updateData)
                logData[executor]['status_text'] = 'Good Proxy'
                # call_stats(logData, "json")
                print(timestamp() + bcolors.OKBLUE + f"Tried {position} | " + bcolors.OKGREEN +
                      f"{proxy} | {proxy_type} --> Good Proxy | Opening a new driver..." + bcolors.ENDC)

                create_html({"#3b8eea": f"Tried {position} | ",
                             "#23d18b": f"{proxy} | {proxy_type} --> Good Proxy | Opening a new driver..."})

                patched_driver = os.path.join(
                    'patched_drivers', f'chromedriver_{position%threads}{EXE_NAME}')

                try:
                    Patcher(executable_path=patched_driver).patch_exe()
                    # print("patched set")
                except:
                    pass

                pluginfile = os.path.join(
                    'extension', f'proxy_auth_plugin{position}.zip')

                # factor = int(threads/6)
                # sleep_time = int((str(position)[-1])) * factor
                # sleep(sleep_time)

                sleep(5)

                driver = get_driver(patched_driver, agent, proxy, proxy_type, pluginfile)

                driver_list.append(driver)

                sleep(5)

                try:
                    proxy_dict = {
                        "http": f"{proxy_type}://{proxy}",
                        "https": f"{proxy_type}://{proxy}",
                    }
                    location = requests.get(
                        "http://ip-api.com/json", proxies=proxy_dict, timeout=180).json()
                    params = {
                        "latitude": location['lat'],
                        "longitude": location['lon'],
                        "accuracy": randint(20, 100)
                    }
                    driver.execute_cdp_cmd(
                        "Emulation.setGeolocationOverride", params)
                except:
                    pass

                referer = choice(REFERERS)
                # get current ip
                if referer:
                    if method == 2 and 't.co/' in referer:
                        driver.get(url)
                    else:
                        driver.get(referer)
                        if 'consent.yahoo.com' in driver.current_url:
                            try:
                                consent = driver.find_element(By.XPATH,
                                    "//button[@name='agree']")
                                driver.execute_script(
                                    "arguments[0].scrollIntoView();", consent)
                                consent.click()
                                driver.get(referer)
                            except:
                                pass
                        driver.execute_script(
                            "window.location.href = '{}';".format(url))
                else:
                    driver.get(url)

                if 'consent' in driver.current_url:
                    print(timestamp() + bcolors.OKBLUE +
                          f"Tried {position} | Bypassing consent..." + bcolors.ENDC)

                    create_html(
                        {"#3b8eea": f"Tried {position} | Bypassing consent..."})

                    bypass_consent(driver)

                if youtube == 'Video':
                    if method == 1:
                        skip_initial_ad(driver, position, output)

                    else:
                        scroll = search_video(driver, keyword, video_title, video_id)
                        if scroll == 0:
                            raise CaptchaError
                        elif scroll == 10:
                            raise QueryError
                        else:
                            pass

                        skip_initial_ad(driver, position, output)

                    # try:
                    #     WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                    #         (By.XPATH, '//ytd-player[@id="ytd-player"]')))
                    # except:
                    #     raise CaptchaError
                    
                    bypass_popup(driver)

                    bypass_other_popup(driver)

                    play_video(driver)

                    if bandwidth:
                        save_bandwidth(driver)

                    change_playback_speed(driver)

                    view_stat = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
                        (By.XPATH, '//span[@class="view-count style-scope ytd-video-view-count-renderer"]'))).text

                else:
                    try:
                        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="player-page"]')))
                    except:
                        raise CaptchaError

                    bypass_popup(driver)

                    play_music(driver)

                    view_stat = 'music'

                if WIDTH == 0:
                    WIDTH = driver.execute_script('return screen.width')
                    VIEWPORT = [i for i in VIEWPORT if int(i[:4]) <= WIDTH]

                if 'watching' in view_stat:
                    error = 0
                    while True:
                        view_stat = driver.find_element(By.XPATH,
                            '//span[@class="view-count style-scope ytd-video-view-count-renderer"]').text
                        if 'watching' in view_stat:
                            print(timestamp() + bcolors.OKBLUE + f"Tried {position} | " + bcolors.OKGREEN +
                                  f"{proxy} | {output} | " + bcolors.OKCYAN + f"{view_stat} " + bcolors.ENDC)

                            create_html({"#3b8eea": f"Tried {position} | ",
                                         "#23d18b": f"{proxy} | {output} | ", "#29b2d3": f"{view_stat} "})
                        else:
                            error += 1

                        play_video(driver)
                        random_command(driver)

                        if error == 5:
                            break
                        sleep(60)

                else:
                    current_url = driver.current_url
                    try:
                        video_len = duration_dict[output]
                    except KeyError:
                        video_len = 0
                        while video_len == 0:
                            video_len = driver.execute_script(
                                "return document.getElementById('movie_player').getDuration()")

                        duration_dict[output] = video_len

                    video_len = video_len*uniform(minimum, maximum)

                    duration = strftime("%Hh:%Mm:%Ss", gmtime(video_len))

                    # MongoDb database collection
                    # updateData = {'video_duration':duration, "updated_date": getTime()}
                    # update_collection_record("youtube_stats", filter, updateData)

                    print(timestamp() + bcolors.OKBLUE + f"Tried {position} | " + bcolors.OKGREEN +
                          f"{proxy} --> {youtube} Found : {output} | Watch Duration : {duration} " + bcolors.ENDC)

                    create_html({"#3b8eea": f"Tried {position} | ",
                                 "#23d18b": f"{proxy} --> {youtube} Found : {output} | Watch Duration : {duration} "})

                    loop = int(video_len/4)
                    for _ in range(loop):
                        sleep(5)
                        current_time = driver.execute_script(
                            "return document.getElementById('movie_player').getCurrentTime()")
                        if youtube == 'Video':
                            play_video(driver)
                            random_command(driver)
                        elif youtube == 'Music':
                            play_music(driver)

                        if current_time > video_len or driver.current_url != current_url:
                            break

                if randint(1, 2) == 1:
                    driver.find_element(By.ID,'movie_player').send_keys('k')

                view.append(position)

                view_count = len(view)

                # MongoDb database collection
                # updateData = {'view_count':1, "updated_date": getTime()}
                # update_collection_record("youtube_stats", filter, updateData)
                # copy_collection_record("youtube_stats","youtube_stats_master", filter)
                logData[executor]['status_text'] = "success"
                logData[executor]['view_count'] = 1
                logData[executor]['updated_date'] = getTime()
                logData[executor]['reason'] = "View count added"
                print(timestamp() + bcolors.OKCYAN +
                      f'View added : {view_count}' + bcolors.ENDC)

                create_html({"#29b2d3": f'View added : {view_count}'})

                with open("views.json", "a") as outfile:
                    outfile.write("---------------------------------------------------------\n")
                    outfile.write("Date Time: " + str(timestamp()))
                    outfile.write("View Added: ")
                    outfile.write(str(view_count)+ "\n")
                    outfile.write("---------------------------------------------------------\n")
                
                if database:
                    try:
                        update_database()
                    except:
                        pass

                # status = quit_driver(driver, pluginfile)

            except CaptchaError:
                # MongoDb database collection
                # updateData = {'fail_reason':"Slow internet speed or Stuck at recaptcha! Can't load YouTube...", "updated_date": getTime()}
                # update_collection_record("youtube_stats", filter, updateData)
                
                print(timestamp() + bcolors.FAIL +
                      f"Tried {position} | Slow internet speed or Stuck at recaptcha! Can't load YouTube..." + bcolors.ENDC)

                create_html(
                    {"#f14c4c": f"Tried {position} | Slow internet speed or Stuck at recaptcha! Can't load YouTube..."})
                
                scriptExecution = False
                logData[executor]['status_text'] = 'error'
                logData[executor]['reason'] = "Slow internet speed or Stuck at recaptcha! Can't load YouTube..."
                status = quit_driver(driver, pluginfile)
                pass

            except QueryError:
                # MongoDb database collection
                # updateData = {'fail_reason':"Can't find this [{video_title}] video with this keyword [{keyword}]", "updated_date": getTime()}
                # update_collection_record("youtube_stats", filter, updateData)

                print(timestamp() + bcolors.FAIL +
                      f"Tried {position} | Can't find this [{video_title}] video with this keyword [{keyword}]" + bcolors.ENDC)

                create_html(
                    {"#f14c4c": f"Tried {position} | Can't find this [{video_title}] video with this keyword [{keyword}]"})

                scriptExecution = False
                logData[executor]['status_text'] = 'error'
                logData[executor]['reason'] = f"Can't find this [{video_title}] video with this keyword [{keyword}]"
                status = quit_driver(driver, pluginfile)
                pass

            except Exception as e:
                *_, exc_tb = sys.exc_info()
                print(timestamp() + bcolors.FAIL +
                      f"Tried {position} | Line : {exc_tb.tb_lineno} | " + str(e) + bcolors.ENDC)

                create_html(
                    {"#f14c4c": f"Tried {position} | Line : {exc_tb.tb_lineno} | " + str(e)})

                scriptExecution = False
                logData[executor]['status_text'] = 'error'
                logData[executor]['reason'] = f"Tried {position} | Line : {exc_tb.tb_lineno} | " + str(e)
                status = quit_driver(driver, pluginfile)
                pass

    except UrlsError:
        print(timestamp() + bcolors.FAIL +
              f"Tried {position} | Your urls.txt is empty!" + bcolors.ENDC)

        create_html(
            {"#f14c4c": f"Tried {position} | Your urls.txt is empty!"})
        pass

    except SearchError:
        print(timestamp() + bcolors.FAIL +
              f"Tried {position} | Your search.txt is empty!" + bcolors.ENDC)

        create_html(
            {"#f14c4c": f"Tried {position} | Your search.txt is empty!"})
        pass

    except:
        # MongoDb database collection
        # updateData = {'status':status, 'reason': 'Bad proxy', "updated_date": getTime()}
        # update_collection_record("youtube_stats", filter, updateData)
        
        print(timestamp() + bcolors.OKBLUE + f"Tried {position} | " +
              bcolors.FAIL + f"{proxy} | {proxy_type} --> Bad proxy " + bcolors.ENDC)

        create_html({"#3b8eea": f"Tried {position} | ",
                     "#f14c4c": f"{proxy} | {proxy_type} --> Bad proxy "})
        logData[executor]['status_text'] = 'error'
        logData[executor]['reason'] = "Bad proxy"
        checked[position] = proxy_type
        pass


def stop_server(immediate=False):
    global server_running

    if api and server_running:
        print('Trying to stop the server')
        if not immediate:
            while 'state=running' in str(futures[1:-1]):
                sleep(5)

        server_running = False
        requests.post(f'http://127.0.0.1:{port}/shutdown')


def view_video(position, executor):
    global server_running
    global port
    if position == 0:
        if api and not server_running:
            server_running = True
            port = port + 1
            website.start_server(host=host, port=port)

    elif position == total_proxies - 1:
        stop_server()

    else:
        # position = 0
        proxy = proxy_list[position]

        if proxy_type:
            main_viewer(proxy_type, proxy, position, executor)
        else:
            main_viewer('http', proxy, position, executor)
            if checked[position] == 'http':
                main_viewer('socks4', proxy, position, executor)
            if checked[position] == 'socks4':
                main_viewer('socks5', proxy, position, executor)


def clean_exit(executor):
    executor.shutdown(wait=False)

    driver_list_ = list(driver_list)
    for driver in driver_list_:
        quit_driver(driver, None)

    while True:
        try:
            work_item = executor._work_queue.get_nowait()
        except queue.Empty:
            break

        if work_item is not None:
            work_item.future.cancel()


def main():
    global start_time
    global futures
    global threads
    global total_proxies
    global executorId
    start_time = time()
    threads = randint(min_threads, max_threads)
    if api:
        threads += 1

    pool_number = [i for i in range(total_proxies)]
    # print("pool_number = ",pool_number)
    pool_number = [2] # static condition
    with ThreadPoolExecutor(max_workers=threads) as executor:
        executorId = executor
        call_stats(executor, "object")
        # print(executorId)
        futures = [executor.submit(view_video, position, executor)
                   for position in pool_number]
        # print(futures)
        try:
            for future in as_completed(futures):

                if len(view) == views:
                    print(
                        bcolors.WARNING + f'Amount of views added : {views} | Stopping program...' + bcolors.ENDC)

                    # Additonally Added for chrome exit()
                    driver_list_ = list(driver_list)
                    for driver in driver_list_:
                        quit_driver(driver, None)
                        driver.quit()

                    # clean_exit(executor)
                    # stop_server()
                    break

                elif refresh != 0:

                    if (time() - start_time) > refresh*60:

                        # if filename:
                        #     if proxy_api:
                        #         proxy_list = scrape_api(filename)
                        #     else:
                        #         proxy_list = load_proxy(filename)
                        # else:
                        #     proxy_list = gather_proxy()

                        # print(bcolors.WARNING +
                        #       f'Proxy reloaded from : {filename}' + bcolors.ENDC)

                        # total_proxies = len(proxy_list)
                        # print(bcolors.OKCYAN +
                        #       f'Total proxies : {total_proxies}' + bcolors.ENDC)

                        # proxy_list.insert(0, 'dummy')
                        # proxy_list.append('dummy')

                    
                        # total_proxies += 2

                        clean_exit(executor)
                        stop_server()
                        break

                future.result()

        except KeyboardInterrupt:
            clean_exit(executor)
            executor._threads.clear()
            concurrent.futures.thread._threads_queues.clear()
            stop_server(immediate=True)
            sys.exit()

if __name__ == '__main__':
    # create_mongo_database()
    # create_collection_mongo('youtube_stats')
    # create_collection_mongo('youtube_stats_master')

    OSNAME, EXE_NAME = download_driver()
    view = []
    scriptExecution = True
    executorId = 0
    @app.route('/checkdata', methods=['POST'])
    def checkdata():
        global postData
        postData = request.json
        post_search = postData["search_text"]
        post_proxy = postData["proxy"]
        global api
        global total_proxies
        global views
        global refresh
        global filename
        global proxy_api
        global host
        global port
        global proxy_list
        global proxy_type
        global category
        global bandwidth
        global minimum
        global maximum
        global database
        global urls
        global queries
        global playback_speed
        global background
        global min_threads
        global max_threads
        global auth_required
        global futures
        global scheduleLogId
        
        call_stats(postData, 'json')
        urls = load_url()
        queries = load_search(post_search)
        
        with open('config.json', 'r') as openfile:
            config = json.load(openfile)

        api = config["http_api"]["enabled"]
        host = config["http_api"]["host"]
        port = config["http_api"]["port"]
        database = config["database"]
        views = config["views"]
        minimum = config["minimum"] / 100
        maximum = config["maximum"] / 100
        category = config["proxy"]["category"]
        proxy_type = config["proxy"]["proxy_type"]
        filename = config["proxy"]["filename"]
        auth_required = config["proxy"]["authentication"]
        proxy_api = config["proxy"]["proxy_api"]
        refresh = config["proxy"]["refresh"]
        background = config["background"]
        bandwidth = config["bandwidth"]
        playback_speed = config["playback_speed"]
        max_threads = config["max_threads"]
        min_threads = config["min_threads"]

        if auth_required and background:
            print(bcolors.FAIL +
                "Premium proxy needs extension to work. Chrome doesn't support extension in Headless mode." + bcolors.ENDC)
            input(bcolors.WARNING +
                f"Either use proxy without username & password or disable headless mode " + bcolors.ENDC)
            sys.exit()

        copy_drivers(max_threads)

        # proxy_list = load_proxy(filename)
        proxy_list = load_proxy(post_proxy)

        total_proxies = len(proxy_list)

        print(bcolors.OKCYAN +
              f'Total proxies : {total_proxies}' + bcolors.ENDC)

        proxy_list.insert(0, 'dummy')
        proxy_list.append('dummy')

        total_proxies += 2

        check = -1
        if scriptExecution == True:
            while len(view) < views:
                try:
                    check += 1
                    if check == 0:
                        if scriptExecution == True:
                            main()
                    else:
                        sleeping()
                        print(bcolors.WARNING +
                            f'Total Checked : {check} times' + bcolors.ENDC)
                        if scriptExecution == True:
                            main()
                        else:
                            call_stats(logData[executorId], "json")
                            # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                            # requests.post(statisticsLogAPI, data=json.dumps(logData[executorId]), headers=headers)

                            # Update scheduleData
                            # scheduleData = {
                            #     "schedule_id": postData[executorId]['schedule_id'],
                            #     "schedule_log_id": postData[executorId]['scheduleLogId'],
                            #     "server_master_id": postData[executorId]['server_master_id'],
                            #     "video_url": logData[executorId]['ytvideo_id'],
                            #     "proxy": logData[executorId]['proxy'],
                            #     "remarks": logData[executorId]['reason'],
                            #     "request_type": "Last",
                            #     "data_process_server_ip": "2222",
                            #     "data_process_proxy_ip": logData[executorId]['proxy_ip'],
                            #     "port": logData[executorId]['proxy_port'],
                            #     "status": logData[executorId]['status_text']
                            # }

                            # headers = {'Content-type': 'multipart/form-data', 'Accept': 'text/plain'}
                            # schedulePost = requests.post(scheduleLogAPI, data=scheduleData).text
                            # scheduleLog = json.loads(schedulePost)
                            # scheduleLogStatus = scheduleLog["status"]
                            print(executorId)
                            return jsonify(logData[executorId])
                except KeyboardInterrupt:
                    sys.exit()
            call_stats(logData[executorId], "json")
            # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            # requests.post(statisticsLogAPI, data=json.dumps(logData[executorId]), headers=headers)

            # Update scheduleData
            # scheduleData = {
            #     "schedule_id": postData[executorId]['schedule_id'],
            #     "schedule_log_id": postData[executorId]['scheduleLogId'],
            #     "server_master_id": postData[executorId]['server_master_id'],
            #     "video_url": logData[executorId]['ytvideo_id'],
            #     "proxy": logData[executorId]['proxy'],
            #     "remarks": logData[executorId]['reason'],
            #     "request_type": "Last",
            #     "data_process_server_ip": "2222",
            #     "data_process_proxy_ip": logData[executorId]['proxy_ip'],
            #     "port": logData[executorId]['proxy_port'],
            #     "status": logData[executorId]['status_text']
            # }
            # headers = {'Content-type': 'multipart/form-data', 'Accept': 'text/plain'}
            # schedulePost = requests.post(scheduleLogAPI, data=scheduleData).text
            # scheduleLog = json.loads(schedulePost)
            # scheduleLogStatus = scheduleLog["status"]
            
            return jsonify(logData[executorId])

    app.run(host='0.0.0.0', port=5000)