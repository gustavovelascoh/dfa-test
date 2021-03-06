#!/usr/bin/python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from random import random
import traceback


random_secs_limit = 15

url = "https://www.dfa.ie/passports/contact/"

time.sleep(random_secs_limit*random())

current_time = time.strftime("%Y-%m-%d %H:%M:%S")

chrome_options = Options()
#chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage");

try:

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)
    time.sleep(5)
    soup = BeautifulSoup(browser.page_source, "html.parser")

    chat_status = soup.find("div",{"id": "chat-button"}).find("img")["alt"]

    print("%s, %s" % (current_time, chat_status))

    browser.close()
    browser.quit()
except:
    print(traceback.format_exc())
