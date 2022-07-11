import concurrent.futures.thread
from crypt import methods
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
# from threading import local
import zipfile

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
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube

import website
from config import create_config
app = Flask(__name__)

log = logging.getLogger('werkzeug')

log.disabled = False

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

class coreLogic:
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

    api = None
    total_proxies = 0
    views = []
    refresh = None
    filename = None
    proxy_api = None
    host = None
    port = None
    proxy_list = []
    OSNAME = None
    EXE_NAME = None
    database = None
    minimum = 0
    maximum = 0
    category = None
    proxy_type = None
    bandwidth = None
    auth_required = None
    background = None
    playback_speed = None
    max_threads = 0
    min_threads = 0
    keyword = None
    video_title = None
    video_id = None
    agent = None
    statisticsLogAPI = None

    WEBRTC = os.path.join('extension', 'webrtc_control.zip')
    ACTIVE = os.path.join('extension', 'always_active.zip')
    FINGERPRINT = os.path.join('extension', 'fingerprint_defender.zip')
    TIMEZONE = os.path.join('extension', 'spoof_timezone.zip')
    CUSTOM_EXTENSIONS = glob(os.path.join('extension', 'custom_extension', '*.zip')) + \
        glob(os.path.join('extension', 'custom_extension', '*.crx'))

    DATABASE = 'database.db'
    DATABASE_BACKUP = 'database_backup.db'

    # Languages = ['en_AU,en','en_BZ,en','en_CA,en','en_CB,en','en_GB,en','en_IE,en','en_JM,en','en_NZ,en','en_PH,en','en_TT,en','en_US,en','en_ZA,en','en_ZW,en']

    WIDTH = 0
    VIEWPORT = ['2560,1440', '1920,1080', '1440,900',
                '1536,864', '1366,768', '1280,1024', '1024,768']

    # OSNAMES = ["lan", "mac"]

    CHROME = ['{8A69D345-D564-463c-AFF1-A69D9E530F96}',
            '{8237E44A-0054-442C-B6B6-EA0509993955}',
            '{401C381F-E0DE-4B85-8BD8-3F3F14FBDA57}',
            '{4ea16ac7-fd5a-47c3-875b-dbf4a2008c20}']

    REFERERS = ['https://search.yahoo.com/', 'https://duckduckgo.com/', 'https://www.google.com/',
            'https://www.bing.com/', 'https://t.co/']

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


    def timestamp(self):
        date_fmt = datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        return bcolors.OKGREEN + f'[{date_fmt}] '

    def getTime(self):
        now = datetime.now()
        curremtDateTime = now.strftime("%d/%m/%Y %H:%M:%S")
        return curremtDateTime

    def download_driver(self):
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
                for i in self.CHROME:
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


    def copy_drivers(self,total,EXE_NAME):
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


    def create_database(self):
        with closing(sqlite3.connect(self.DATABASE)) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute("""CREATE TABLE IF NOT EXISTS
                statistics (date TEXT, view INTEGER)""")

                connection.commit()

        try:
            # remove previous backup if exists
            os.remove(self.DATABASE_BACKUP)
        except:
            pass

        try:
            # backup latest database
            shutil.copy(self.DATABASE, self.DATABASE_BACKUP)
        except:
            pass

    def update_database(self):
        
        today = str(datetime.today().date())
        with closing(sqlite3.connect(self.DATABASE, timeout=threads*10)) as connection:
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

    def call_stats(self,logs,type):
        if type == 'json':
            finalString = json.dumps(logs)
        elif type == 'object':
            finalString = str(logs)

        # print()
        with open("views.json", "a") as outfile:
            outfile.write("---------------------------------------------------------\n")
            outfile.write("Date Time: " + str(self.timestamp()))
            outfile.write(finalString + "\n")
            outfile.write("---------------------------------------------------------\n")
            
    def create_html(self,text_dict):
        console = self.console

        if len(console) > 50:
            console.pop(0)

        date_fmt = f'<span style="color:#23d18b"> [{datetime.now().strftime("%d-%b-%Y %H:%M:%S")}] </span>'
        str_fmt = ''.join(
            [f'<span style="color:{key}"> {value} </span>' for key, value in text_dict.items()])
        html = date_fmt + str_fmt

        console.append(html)


    def load_url(self):
        print(bcolors.WARNING + 'Loading urls...' + bcolors.ENDC)

        with open('urls.txt', encoding="utf-8") as fh:
            links = [x.strip() for x in fh if x.strip() != '']

        print(bcolors.OKGREEN +
            f'{len(links)} url loaded from urls.txt' + bcolors.ENDC)

        return links


    def load_search(self,search_text):
        print(bcolors.WARNING + 'Loading queries...' + bcolors.ENDC)

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

    def load_proxy(self,proxyData):
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


    def check_proxy(self):
        if self.category == 'f':
            headers = {
                'User-Agent': f'{self.agent}',
            }
            proxy_dict = {
                "http": f"{self.proxy_type}://{self.proxy}",
                "https": f"{self.proxy_type}://{self.proxy}",
            }
            response = requests.get(
                'https://www.youtube.com/', headers=headers, proxies=proxy_dict, timeout=30)
            status = response.status_code

        else:
            status = 200

        return status


    def get_driver(self, path, proxy, proxy_type, pluginfile):
        options = webdriver.ChromeOptions()
        # options.headless = True
        # options.add_argument("--headless")
        options.add_argument(f"--window-size={choice(self.VIEWPORT)}")
        options.add_argument("--log-level=3")
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation", "enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': 'en_US,en'})
        options.add_argument(f"user-agent={self.agent}")
        options.add_argument("--mute-audio")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-features=UserAgentClientHint')
        webdriver.DesiredCapabilities.CHROME['loggingPrefs'] = {
            'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}

        if not self.background:
            options.add_extension(self.WEBRTC)
            options.add_extension(self.FINGERPRINT)
            options.add_extension(self.TIMEZONE)
            options.add_extension(self.ACTIVE)

            if self.CUSTOM_EXTENSIONS:
                for extension in self.CUSTOM_EXTENSIONS:
                    options.add_extension(extension)

        if self.auth_required:
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
        # chrome_options.add_argument(f"user-agent={self.agent}")
        # chrome_options.add_argument(f'--proxy-server={proxy_type}://{proxy}')
        # chrome_options.add_argument(f'--proxy-server={proxy_static}')

        # open chrome
        # cpath = '/var/www/html/ytviewer/chrome_driver'
        # cpath = '/usr/bin/chromedriver'
        # cpath = '/root/.wdm/drivers/chromedriver/linux64/98.0.4758.80/chromedriver'
        # self.driver = webdriver.Chrome(executable_path=cpath, options=chrome_options)
        # self.driver = webdriver.Chrome(executable_path=cpath, options=options)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        # self.driver = webdriver.Chrome(executable_path=path, options=options)


    def personalization(self):
        search = self.driver.find_element(By.XPATH,
            f'//button[@aria-label="Turn {choice(["on","off"])} Search customization"]')
        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", search)
        search.click()

        history = self.driver.find_element(By.XPATH,
            f'//button[@aria-label="Turn {choice(["on","off"])} YouTube History"]')
        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", history)
        history.click()

        ad = self.driver.find_element(By.XPATH,
            f'//button[@aria-label="Turn {choice(["on","off"])} Ad personalization"]')
        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", ad)
        ad.click()

        confirm = self.driver.find_element(By.XPATH,'//button[@jsname="j6LnYe"]')
        self.driver.execute_script("arguments[0].scrollIntoViewIfNeeded();", confirm)
        confirm.click()


    def bypass_consent(self):
        try:
            consent = self.driver.find_element(By.XPATH,"//button[@jsname='higCR']")
            self.driver.execute_script("arguments[0].scrollIntoView();", consent)
            consent.click()
            if 'consent' in self.driver.current_url:
                self.personalization()
        except:
            consent = self.driver.find_element(By.XPATH,
                "//input[@type='submit' and @value='I agree']")
            self.driver.execute_script("arguments[0].scrollIntoView();", consent)
            consent.submit()
            if 'consent' in self.driver.current_url:
                self.personalization()

    def bypass_popup(self):
        try:
            agree = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@aria-label="Agree to the use of cookies and other data for the purposes described"]')))
            self.driver.execute_script(
                "arguments[0].scrollIntoViewIfNeeded();", agree)
            sleep(1)
            agree.click()
        except:
            pass


    def bypass_other_popup(self):
        popups = ['Got it', 'Skip trial', 'No thanks', 'Dismiss', 'Not now']
        shuffle(popups)

        for popup in popups:
            try:
                self.driver.find_element(By.XPATH,
                    f"//*[@id='button' and @aria-label='{popup}']").click()
            except:
                pass


    def skip_initial_ad(self, position, video):
        try:
            video_len = self.duration_dict[video]
            if video_len > 30:
                self.bypass_popup()
                skip_ad = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
                    (By.CLASS_NAME, "ytp-ad-skip-button-container")))

                print(self.timestamp() + bcolors.OKBLUE +
                    f"Tried {position} | {video} | Viewing Ads..." + bcolors.ENDC)

                self.create_html({"#23d18b": f"Tried {position} | {video} | Viewing Ads..."})

                ad_duration = self.driver.find_element(By.CLASS_NAME, 
                    'ytp-time-duration').get_attribute('innerText')
                ad_duration = sum(x * int(t)
                                for x, t in zip([60, 1], ad_duration.split(":")))
                ad_duration = ad_duration * uniform(.01, .1)
                sleep(ad_duration)
                # skip_ad.click()
        except:
            pass


    def type_keyword(self, retry=False):
        input_keyword = self.driver.find_element(By.CSS_SELECTOR,'input#search')
        if retry:
            for _ in range(10):
                try:
                    input_keyword.click()
                    break
                except:
                    sleep(5)
                    pass

        input_keyword.clear()
        for letter in self.keyword:
            input_keyword.send_keys(letter)
            sleep(uniform(.1, .4))

        method = randint(1, 2)
        if method == 1:
            input_keyword.send_keys(Keys.ENTER)
        else:
            try:
                self.driver.find_element(By.XPATH,
                    '//*[@id="search-icon-legacy"]').click()
            except:
                self.driver.execute_script(
                    'document.querySelector("#search-icon-legacy").click()')


    def search_video(self):
        i = 0
        try:
            self.type_keyword()
        except:
            try:
                self.bypass_popup()
                self.type_keyword(retry=True)
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
                section = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
                    (By.XPATH, f'//ytd-item-section-renderer[{i}]')))
                find_video = section.find_element(By.XPATH,
                    f'//a[@href="/watch?v={self.video_id}"]')
                print(find_video)
                self.driver.execute_script(
                    "arguments[0].scrollIntoViewIfNeeded();", find_video)

                # driver.find_element(By.XPATH,'//a[@href="/watch?v=OQij6GB2FA8"]').click()
                sleep(5)
                self.bypass_popup()
                self.bypass_other_popup()
                # self.call_stats(driver, "object")
                try:
                    # section.click()
                    self.driver.find_element(By.XPATH,f'//a[@href="/watch?v={self.video_id}"]').click()
                    
                except:
                    self.driver.execute_script(
                        "arguments[0].click();", section)
                break
            except NoSuchElementException:
                sleep(5)
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
                    (By.TAG_NAME, 'body'))).send_keys(Keys.CONTROL, Keys.END)

        return i


    def play_video(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR,'[title^="Pause (k)"]')

            # Click on LIKE button 
            # sleeping()
            # driver.find_element(By.CSS_SELECTOR,'yt-icon.style-scope.ytd-toggle-button-renderer').click()
        except:
            try:
                self.driver.find_element(By.CSS_SELECTOR,
                    'button.ytp-large-play-button.ytp-button').send_keys(Keys.ENTER)
            except:
                try:
                    self.driver.find_element(By.CSS_SELECTOR,
                        '[title^="Play (k)"]').click()
                except:
                    try:
                        self.driver.execute_script(
                            "document.querySelector('button.ytp-play-button.ytp-button').click()")
                    except:
                        pass


    def play_music(self):
        try:
            self.driver.find_element(By.XPATH,
                '//*[@id="play-pause-button" and @title="Pause"]')
        except:
            try:
                self.driver.find_element(By.XPATH,
                    '//*[@id="play-pause-button" and @title="Play"]').click()
            except:
                self.driver.execute_script(
                    'document.querySelector("#play-pause-button").click()')


    def save_bandwidth(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR,
                "button.ytp-button.ytp-settings-button").click()
            self.driver.find_element(By.XPATH,
                "//div[contains(text(),'Quality')]").click()

            random_quality = choices(
                ['144p', '240p', '360p'], cum_weights=(0.7, 0.9, 1.00), k=1)[0]
            quality = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, f"//span[contains(string(),'{random_quality}')]")))
            self.driver.execute_script(
                "arguments[0].scrollIntoViewIfNeeded();", quality)
            quality.click()

        except:
            try:
                self.driver.find_element(By.XPATH,
                    '//*[@id="container"]/h1/yt-formatted-string').click()
            except:
                pass


    def change_playback_speed(self):
        if self.playback_speed == 2:
            self.driver.find_element(By.ID,'movie_player').send_keys('<'*randint(1, 3))
        elif self.playback_speed == 3:
            self.driver.find_element(By.ID,'movie_player').send_keys('>'*randint(1, 3))


    def random_command(self):
        self.bypass_other_popup()

        option = choices([1, 2], cum_weights=(0.7, 1.00), k=1)[0]
        if option == 2:
            command = choice(self.COMMANDS)
            if command in ['m', 't', 'c']:
                self.driver.find_element(By.ID,'movie_player').send_keys(command)
            elif command == 'k':
                if randint(1, 2) == 1:
                    self.driver.find_element(By.ID,'movie_player').send_keys(command)
                self.driver.execute_script(
                    f'document.querySelector("#comments"){choices(["scrollIntoView", "scrollIntoViewIfNeeded"])}();')
                sleep(uniform(4, 10))
                self.driver.execute_script(
                    'document.querySelector("#movie_player").scrollIntoViewIfNeeded();')
            else:
                self.driver.find_element(By.ID,
                    'movie_player').send_keys(command*randint(1, 5))


    def quit_driver(self, pluginfile):
        try:
            self.driver_list.remove(self.driver)
        except:
            pass
        self.driver.quit()

        try:
            os.remove(pluginfile)
        except:
            pass

        status = 400
        return status


    def sleeping(self):
        sleep(5)


    def main_viewer(self, proxy_type, proxy, position):
        try:
            global WIDTH
            global VIEWPORT

            self.checked[position] = None

            header = Headers(
                browser="chrome",
                os=self.OSNAME,
                headers=False
            ).generate()
            self.agent = header['User-Agent']
            url = ''

            if position % 2:
                try:
                    method = 1
                    url = choice(self.urls)
                    output = url
                    if 'music.youtube.com' in url:
                        youtube = 'Music'
                    else:
                        youtube = 'Video'
                except:
                    raise self.UrlsError

            else:
                try:
                    method = 2
                    query = choice(self.queries)
                    searchVar = query[0].split()
                    shuffle(searchVar)
                    self.keyword = (' '.join(searchVar))
                    self.video_title = query[1]
                    self.video_id = query[2]
                    print("Search Keyword ====>",self.keyword)
                    url = "https://www.youtube.com"
                    output = self.video_title
                    youtube = 'Video'
                except:
                    url = choice(self.urls)
                    output = url
                    if 'music.youtube.com' in url:
                        youtube = 'Music'
                    else:
                        raise self.SearchError

            if self.category == 'r' and self.proxy_api:
                proxies = self.scrape_api(link=proxy)
                proxy = choice(proxies)

                
            # Initilize stats data for youtube
            
            status = self.check_proxy()
            
            proxy_data = proxy.split('@')
            if len(proxy_data) == 2:
                proxy_ip = proxy_data[1].split(':')[0]
                proxy_port = proxy_data[1].split(':')[1]
            elif len(proxy_data) == 1:
                proxy_ip = proxy_data.split(':')[0]
                proxy_port = proxy_data.split(':')[1]

            self.logData = {
                "unique_reference_id": self.postData['unique_reference_id'],
                "agent": self.agent,
                "status": 'InProgress',
                "reason": "Working.."
            }

            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post(self.statisticsLogAPI, data=json.dumps(self.logData), headers=headers)

            # self.call_stats(logData, "json")
            
            if status == 200:
                try:
                    self.logData['status'] = 'Good Proxy'
                    # call_stats(logData, "json")
                    print(self.timestamp() + bcolors.OKBLUE + f"Tried {position} | " + bcolors.OKGREEN +
                        f"{proxy} | {proxy_type} --> Good Proxy | Opening a new driver..." + bcolors.ENDC)

                    self.create_html({"#3b8eea": f"Tried {position} | ",
                                "#23d18b": f"{proxy} | {proxy_type} --> Good Proxy | Opening a new driver..."})

                    patched_driver = os.path.join(
                        'patched_drivers', f'chromedriver_{position%threads}{self.EXE_NAME}')

                    try:
                        Patcher(executable_path=patched_driver).patch_exe()
                        # print("patched set")
                    except:
                        pass

                    pluginfile = os.path.join(
                        'extension', f'proxy_auth_plugin{position}.zip')

                    factor = int(threads/6)
                    sleep_time = int((str(position)[-1])) * factor
                    sleep(sleep_time)

                    sleep(5)

                    self.get_driver(patched_driver, proxy, proxy_type, pluginfile)

                    self.driver_list.append(self.driver)

                    sleep(5)

                    try:
                        proxy_dict = {
                            "http": f"{proxy_type}://{proxy}",
                            "https": f"{proxy_type}://{proxy}",
                        }
                        location = requests.get(
                            "https://pro.ip-api.com/json/?key=bvanql2zZLPdKzF", proxies=proxy_dict, timeout=180).json()
                        params = {
                            "latitude": location['lat'],
                            "longitude": location['lon'],
                            "accuracy": randint(20, 100)
                        }
                        self.logData['country'] = location['country']
                        self.logData['region_name'] = location['regionName']
                        self.logData['city'] = location['city']
                        self.logData['zip'] = location['zip']
                        self.logData['timezone'] = location['timezone']
                        self.logData['isp'] = location['isp']
                        self.logData['query_ip'] = location['query']

                        print("Proxy => " + proxy +  " ==> Internal ip: " + bcolors.OKCYAN + location['query'] + bcolors.ENDC)


                        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                        requests.post(self.statisticsLogAPI, data=json.dumps(self.logData), headers=headers)

                        self.driver.execute_cdp_cmd(
                            "Emulation.setGeolocationOverride", params)
                    except:
                        pass

                    referer = choice(self.REFERERS)
                    if referer:
                        if method == 2 and 't.co/' in referer:
                            self.driver.get(url)
                        else:
                            self.driver.get(referer)
                            if 'consent.yahoo.com' in self.driver.current_url:
                                try:
                                    consent = self.driver.find_element(By.XPATH,
                                        "//button[@name='agree']")
                                    self.driver.execute_script(
                                        "arguments[0].scrollIntoView();", consent)
                                    consent.click()
                                    self.driver.get(referer)
                                except:
                                    pass
                            self.driver.execute_script(
                                "window.location.href = '{}';".format(url))
                    else:
                        self.driver.get(url)

                    if 'consent' in self.driver.current_url:
                        print(self.timestamp() + bcolors.OKBLUE +
                            f"Tried {position} | Bypassing consent..." + bcolors.ENDC)

                        self.create_html(
                            {"#3b8eea": f"Tried {position} | Bypassing consent..."})

                        self.bypass_consent()

                    if youtube == 'Video':
                        if method == 1:
                            self.skip_initial_ad(position, output)

                        else:
                            scroll = self.search_video()
                            print(scroll)
                            if scroll == 0:
                                raise self.CaptchaError
                            elif scroll == 10:
                                raise self.QueryError
                            else:
                                pass

                            self.skip_initial_ad(position, output)

                        # try:
                        #     WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                        #         (By.XPATH, '//ytd-player[@id="ytd-player"]')))
                        # except:
                        #     raise CaptchaError
                        
                        self.bypass_popup()

                        self.bypass_other_popup()

                        self.play_video()

                        if self.bandwidth:
                            self.save_bandwidth()

                        self.change_playback_speed()

                        view_stat = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(
                            (By.XPATH, '//span[@class="view-count style-scope ytd-video-view-count-renderer"]'))).text

                    else:
                        try:
                            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
                                (By.XPATH, '//*[@id="player-page"]')))
                        except:
                            raise self.CaptchaError

                        self.bypass_popup()

                        self.play_music()

                        view_stat = 'music'

                    if self.WIDTH == 0:
                        WIDTH = self.driver.execute_script('return screen.width')
                        VIEWPORT = [i for i in self.VIEWPORT if int(i[:4]) <= WIDTH]

                    if 'watching' in view_stat:
                        error = 0
                        while True:
                            view_stat = self.driver.find_element(By.XPATH,
                                '//span[@class="view-count style-scope ytd-video-view-count-renderer"]').text
                            if 'watching' in view_stat:
                                print(self.timestamp() + bcolors.OKBLUE + f"Tried {position} | " + bcolors.OKGREEN +
                                    f"{proxy} | {output} | " + bcolors.OKCYAN + f"{view_stat} " + bcolors.ENDC)

                                self.create_html({"#3b8eea": f"Tried {position} | ",
                                            "#23d18b": f"{proxy} | {output} | ", "#29b2d3": f"{view_stat} "})
                            else:
                                error += 1

                            self.play_video()
                            self.random_command()

                            if error == 5:
                                break
                            sleep(60)

                    else:
                        current_url = self.driver.current_url
                        try:
                            video_len = self.duration_dict[output]
                        except KeyError:
                            video_len = 0
                            while video_len == 0:
                                video_len = self.driver.execute_script(
                                    "return document.getElementById('movie_player').getDuration()")

                            self.duration_dict[output] = video_len

                        video_len = video_len*uniform(self.minimum, self.maximum)

                        duration = strftime("%Hh:%Mm:%Ss", gmtime(video_len))

                        print(self.timestamp() + bcolors.OKBLUE + f"Tried {position} | " + bcolors.OKGREEN +
                            f"{proxy} --> {youtube} Found : {output} | Watch Duration : {duration} " + bcolors.ENDC)

                        self.create_html({"#3b8eea": f"Tried {position} | ",
                                    "#23d18b": f"{proxy} --> {youtube} Found : {output} | Watch Duration : {duration} "})

                        loop = int(video_len/4)
                        for _ in range(loop):
                            sleep(5)
                            current_time = self.driver.execute_script(
                                "return document.getElementById('movie_player').getCurrentTime()")
                            if youtube == 'Video':
                                self.play_video()
                                self.random_command()
                            elif youtube == 'Music':
                                self.play_music()

                            if current_time > video_len or self.driver.current_url != current_url:
                                break

                    if randint(1, 2) == 1:
                        self.driver.find_element(By.ID,'movie_player').send_keys('k')

                    self.view.append(position)

                    view_count = len(self.view)

                    self.logData['status'] = "success"
                    self.logData['reason'] = "View count added"
                    print(self.timestamp() + bcolors.OKCYAN +
                        f'{self.proxy} | {output} | View added : {view_count}' + bcolors.ENDC)

                    self.create_html({"#29b2d3": f'{self.proxy} | {output} | View added : {view_count}'})

                    if self.database:
                        try:
                            self.update_database()
                        except:
                            pass

                    status = self.quit_driver(pluginfile)
                    pass

                except self.CaptchaError:
                    print(self.timestamp() + bcolors.FAIL +
                        f"{self.proxy} | Tried {position} | Slow internet speed or Stuck at recaptcha! Can't load YouTube..." + bcolors.ENDC)

                    self.create_html(
                        {"#f14c4c": f"{self.proxy} Tried {position} | Slow internet speed or Stuck at recaptcha! Can't load YouTube..."})
                    
                    self.logData['status'] = 'error'
                    self.logData['reason'] = "Slow internet speed or Stuck at recaptcha! Can't load YouTube..."
                    status = self.quit_driver(pluginfile)
                    pass

                except self.QueryError:
                    print(self.timestamp() + bcolors.FAIL +
                        f"{self.proxy} | Tried {position} | Can't find this [{self.video_title}] video with this keyword [{self.keyword}]" + bcolors.ENDC)

                    self.create_html(
                        {"#f14c4c": f"{self.proxy} | Tried {position} | Can't find this [{self.video_title}] video with this keyword [{self.keyword}]"})

                    self.logData['status'] = 'error'
                    self.logData['reason'] = f"Can't find this [{self.video_title}] video with this keyword [{self.keyword}]"
                    status = self.quit_driver(pluginfile)
                    pass

                except Exception as e:
                    *_, exc_tb = sys.exc_info()
                    print(self.timestamp() + bcolors.FAIL +
                        f"{self.proxy} | Tried {position} | Line : {exc_tb.tb_lineno} | " + str(e) + bcolors.ENDC)

                    self.create_html(
                        {"#f14c4c": f"{self.proxy} | Tried {position} | Line : {exc_tb.tb_lineno} | " + str(e)})

                    self.logData['status'] = 'error'
                    self.logData['reason'] = f"Tried {position} | Line : {exc_tb.tb_lineno} | " + str(e)
                    status = self.quit_driver(pluginfile)
                    pass

        except self.UrlsError:
            print(self.timestamp() + bcolors.FAIL +
                f"{self.proxy} | Tried {position} | Your urls.txt is empty!" + bcolors.ENDC)

            self.create_html(
                {"#f14c4c": f"{self.proxy} | Tried {position} | Your urls.txt is empty!"})
            pass

        except self.SearchError:
            print(self.timestamp() + bcolors.FAIL +
                f"{self.proxy} | Tried {position} | Your search.txt is empty!" + bcolors.ENDC)

            self.create_html(
                {"#f14c4c": f"{self.proxy} | Tried {position} | Your search.txt is empty!"})
            pass

        except Exception as e:
            print(self.timestamp() + bcolors.OKBLUE + f"{self.proxy} | Tried {position} | " +
                bcolors.FAIL + f"{proxy} | {proxy_type} --> Bad proxy " + str(e) + bcolors.ENDC)

            self.create_html({"#3b8eea": f"{self.proxy} | Tried {position} | ",
                        "#f14c4c": f"{proxy} | {proxy_type} --> Bad proxy " + str(e)})

            self.checked[position] = proxy_type
            pass


    def stop_server(self, immediate=False):
        if self.api and self.server_running:
            print('Trying to stop the server')
            if not immediate:
                while 'state=running' in str(futures[1:-1]):
                    sleep(5)

            self.server_running = False
            requests.post(f'http://127.0.0.1:{self.port}/shutdown')


    def view_video(self, position):
        if position == 0:
            if self.api and not self.server_running:
                self.server_running = True
                # self.port = self.port + 1
                website.start_server(host=self.host, port=self.port)

        elif position == self.total_proxies - 1:
            self.stop_server()

        else:
            # position = 0
            proxy = self.proxy_list[position]
            self.proxy = proxy

            if self.proxy_type:
                self.main_viewer(self.proxy_type, proxy, position)
            else:
                self.main_viewer('http', proxy, position)
                if self.checked[position] == 'http':
                    self.main_viewer('socks4', proxy, position)
                if self.checked[position] == 'socks4':
                    self.main_viewer('socks5', proxy, position)


    def clean_exit(self, executor):
        executor.shutdown(wait=False)

        driver_list_ = list(self.driver_list)
        for driver in driver_list_:
            self.quit_driver(driver, None)

        while True:
            try:
                work_item = executor._work_queue.get_nowait()
            except queue.Empty:
                break

            if work_item is not None:
                work_item.future.cancel()

    def ipCheck(self):
        lPos = 2 # Here i picked static position for proxy.
        location = []
        response = []
        try:
            proxy_dict = {
                "http": f"{self.proxy_type}://{self.proxy_list[lPos]}",
                "https": f"{self.proxy_type}://{self.proxy_list[lPos]}",
            }
            # Get Location data
            location = requests.get("https://pro.ip-api.com/json/?key=bvanql2zZLPdKzF", proxies=proxy_dict, timeout=180).json()
        except:
            pass

        # Check ProxyIP / Original IP for Unique Behaviour
        if str(location['status']) != 'fail':
            getData = {"reference_id": self.postData['unique_reference_id'], "generated_ip": location['query']}
            response = requests.get(self.statisticsCheckAPI, getData).json()
            return response
        else:
            return location

    def main(self):
        global start_time
        global futures
        global threads
        start_time = time()
        threads = randint(self.min_threads, self.max_threads)
        if self.api:
            threads += 1

        # pool_number = [i for i in range(self.total_proxies)]
        # print("pool_number = ",pool_number)
        pool_number = [2] # static condition

        # res = self.ipCheck()
        # if(res):
        #     if res['status'] == False:
        #         self.logData = {
        #             "unique_reference_id": self.postData['unique_reference_id'],
        #             "status": 'error',
        #             "reason": "This IP and Proxy Already Used"
        #         }
        #         return
        #     if res['status'] == 'fail':
        #         self.logData = {
        #             "unique_reference_id": self.postData['unique_reference_id'],
        #             "status": 'error',
        #             "reason": res['message']
        #         }
        #         pass

        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(self.view_video, position)
                    for position in pool_number]
              
            try:
                for future in as_completed(futures):

                    if len(self.view) == self.views:
                        print(
                            bcolors.WARNING + f'{self.proxy} | Amount of views added : {self.views} | Stopping program...' + bcolors.ENDC)

                        # Additonally Added for chrome exit()
                        # driver_list_ = list(self.driver_list)
                        # for driver in driver_list_:
                        #     self.quit_driver(driver, None)
                        #     driver.quit()
                            
                        # self.clean_exit(executor)
                        self.quit_driver(None)
                        self.stop_server()
                        break

                    elif self.refresh != 0:

                        if (time() - start_time) > self.refresh*60:

                            self.clean_exit(executor)
                            self.stop_server()
                            break

                    future.result()

            except KeyboardInterrupt:
                self.clean_exit(executor)
                executor._threads.clear()
                concurrent.futures.thread._threads_queues.clear()
                self.stop_server(immediate=True)
                sys.exit()

if __name__ == '__main__':

    
    @app.route('/youtubeDesc', methods=['GET'])
    def youtubeDesc():
        video = YouTube("https://www.youtube.com/watch?v=o35Xi0h7880")
        print (video.description)
        customeRes = {'status': 'error','transcript': 'No Description were found'}
        return jsonify(customeRes)

    @app.route('/transcript', methods=['GET'])
    def transcript():
        video_id = request.json["video_id"]
        scriptRes = ''
        customeRes = ''
        try:
            res = ''
            responses = YouTubeTranscriptApi.get_transcript(video_id)
            print('\n'+"Video: "+"https://www.youtube.com/watch?v="+str(video_id)+'\n'+'\n'+"Captions:")
            print(responses)
            for response in responses:
                text = response['text']
                res += " "+ text
            transcript = res.replace("[Music]", " ")
            scriptRes = transcript.replace("   ", " ")
            customeRes = {'status': 'success','transcript': scriptRes}
        except Exception as e:
            # print(e)
            customeRes = {'status': 'error','transcript': 'No transcripts were found'}
        return jsonify(customeRes)

    @app.route('/copyai', methods=['POST'])
    def copyai():
        postData = request.json
        videoContent = postData["transcript"]
        video_id = postData["video_id"]
        proxy = postData["proxy"]
        port = postData["port"]
        comments = []
    
        print(video_id)

        try:
            copyai_url = 'https://www.copy.ai/tools/instagram-caption-generator#'
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument("--headless")
            
            options.add_argument("--proxy-server=%s:%s" % (proxy,port))

            # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
            position = randint(1,10)
            threads = randint(1, 2)
            EXE_NAME = ""
            path = os.path.join(
                        'patched_drivers', f'chromedriver_{position%threads}{EXE_NAME}')
            driver = webdriver.Chrome(executable_path=path, options=options)
            driver.get(copyai_url)

            fieldOne = driver.find_element(By.XPATH,'//*[@id ="input-one"]')
            fieldOne.send_keys(videoContent)
            fieldTwo = driver.find_element(By.XPATH,'//*[@id ="input-two"]')
            fieldTwo.send_keys(videoContent)

            sleep(10)

            craetebtn = driver.find_element(By.XPATH,'//*[@id="create-copy-button"]')
            craetebtn.click()

            sleep(10)

            ungated0 = driver.find_element(By.XPATH,'//*[@id="ungated-0"]')
            comment0 = ungated0.get_attribute('originaltext')
            comments.append(comment0)
            ungated1 = driver.find_element(By.XPATH,'//*[@id="ungated-1"]')
            comment1 = ungated1.get_attribute('originaltext')
            comments.append(comment1)
            ungated2 = driver.find_element(By.XPATH,'//*[@id="ungated-2"]')
            comment2 = ungated2.get_attribute('originaltext')
            comments.append(comment2)
            ungated3 = driver.find_element(By.XPATH,'//*[@id="ungated-3"]')
            comment3 = ungated3.get_attribute('originaltext')
            comments.append(comment3)
            ungated4 = driver.find_element(By.XPATH,'//*[@id="ungated-4"]')
            comment4 = ungated4.get_attribute('originaltext')
            comments.append(comment4)
            print(comments)
        except Exception as e:
            print(e)
            # sleep(10)
            driver.close()
        # print(commnets)

        # sleep(10)
        # driver.close()

        response = {'video': video_id, 'comments': comments}
        return jsonify(response)

    @app.route('/checkdata', methods=['POST'])
    def checkdata():
        cl = coreLogic()
        cl.postData = request.json
        cl.view = []
        cl.logData = []
        
        print(cl.timestamp() + bcolors.OKCYAN + f'----------------------------------Started new call------------------------------------------------' + bcolors.ENDC)
        cl.OSNAME, cl.EXE_NAME = cl.download_driver()
    
        # cl.call_stats(cl.postData, 'json')

        cl.urls = cl.load_url()
        cl.queries = cl.load_search(cl.postData["search_text"])
        
        with open('config.json', 'r') as openfile:
            config = json.load(openfile)

        cl.api = config["http_api"]["enabled"]
        cl.host = config["http_api"]["host"]
        cl.port = config["http_api"]["port"]
        cl.database = config["database"]
        cl.views = config["views"]
        cl.minimum = config["minimum"] / 100
        cl.maximum = config["maximum"] / 100
        cl.category = config["proxy"]["category"]
        cl.proxy_type = config["proxy"]["proxy_type"]
        cl.filename = config["proxy"]["filename"]
        cl.auth_required = config["proxy"]["authentication"]
        cl.proxy_api = config["proxy"]["proxy_api"]
        cl.refresh = config["proxy"]["refresh"]
        cl.background = config["background"]
        cl.bandwidth = config["bandwidth"]
        cl.playback_speed = config["playback_speed"]
        cl.max_threads = config["max_threads"]
        cl.min_threads = config["min_threads"]

        # Set Log API URL
        cl.statisticsLogAPI = config["logAPI"]
        cl.statisticsCheckAPI = config["CheckAPI"]

        if cl.auth_required and cl.background:
            print(bcolors.FAIL +
                "Premium proxy needs extension to work. Chrome doesn't support extension in Headless mode." + bcolors.ENDC)
            input(bcolors.WARNING +
                f"Either use proxy without username & password or disable headless mode " + bcolors.ENDC)
            sys.exit()

        cl.copy_drivers(cl.max_threads,cl.EXE_NAME)

        cl.proxy_list = cl.load_proxy(cl.postData["proxy"])

        cl.total_proxies = len(cl.proxy_list)

        print(bcolors.OKCYAN +
              f'Total proxies : {cl.total_proxies}' + bcolors.ENDC)

        cl.proxy_list.insert(0, 'dummy')
        cl.proxy_list.append('dummy')

        cl.total_proxies += 2

        check = -1

        updateLog = {
                "unique_reference_id": cl.postData['unique_reference_id'],
                "status": 'InProgress',
                "reason": "Working.."
            }

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        # requests.post(cl.statisticsLogAPI, data=json.dumps(updateLog), headers=headers)
        
        while len(cl.view) < cl.views:
            try:
                check += 1
                if check == 0:
                    cl.main()
                else:
                    cl.sleeping()
                    print(bcolors.WARNING +
                        f'Total Checked : {check} times' + bcolors.ENDC)
                    # cl.main()

                    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                    requests.post(cl.statisticsLogAPI, data=json.dumps(cl.logData), headers=headers)
                    
                    # cl.logData["stats_reponse_API"] = json.loads(statisticsPost)
                    # cl.logData['video_id'] = cl.video_id
                    return jsonify(cl.logData)
            except KeyboardInterrupt:
                sys.exit()

        cl.view = []

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        requests.post(cl.statisticsLogAPI, data=json.dumps(cl.logData), headers=headers)

        # cl.logData["stats_reponse_API"] = json.loads(statisticsPost)
        # print(statisticsPost)
        # cl.logData['video_id'] = cl.video_id
        return jsonify(cl.logData)

    app.run(host='0.0.0.0', port=5000)