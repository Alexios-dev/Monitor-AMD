import datetime
import random
import time
import platform

import undetected_chromedriver.v2 as webdriver
import selenium
import requests
import threading
import discum
import socket
from discordwebhook import Discord
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from uuid import getnode as get_mac
#https://gist.github.com/Birdie0/78ee79402a4301b1faf412ab5f1cdcf9
URL = 'https://www.amd.com/de/direct-buy/de'  # check site
CheckXpath = '//*[@id="block-amd-page-title"]/h1'  # Xpath for button or text on this site
Web_Hook_Discord = 'https://discord.com/api/webhooks/897589486031085639/G6oNdCJqXfaYz0ningP5kA12g0BrJ-6P5Ba2cY7K3G8DxrenR3vIlur7RAPKa_w-KYXq'

Cookie = '219F6565FA78050C7540754465CC8946~-1~YAAQ5pAWAucS4ll8AQAAo7vNWgbwDBQLmA6m3FTVMU+b0/LB5V0rkGfPphPXSTa5VvZRlLluJOJlvXhxhFXuBm2UByQRT0fNHrQ2vb/5nyDLsqXmLa0cwRpUjFFv+qpzHAXI4zhrXSdwxMDiuIVV95ikJoXfcmzSpWO9LMAW7knz5eTVrkO2moSbV/5Mg2pWLMwgbErJOvQPrkOtBS4XlXpl5XCySc43qbYyb4IjZ3eVv36Z3U1XUPjEnoz7MnW9pGMrs+0u8ejXeR6RbwSi8vEkpn6dO1E93eHf3kfoaGLv6cVqwWOTYZ4G46qs1rtKzrdl0B0ZvYNi7rfWOOoO+lV4I/ErZbkmuz+bMTsUCp2rFhlGXjAzgvPMclNuN82WSbbQX6iaRA==~-1~||1-FjTWmquFxM-1-10-1000-2||~-1'

print("Licensed by Alexander Genenger")
print("Gnu public license v3")
def SendMessage(DC_Url):
    webhook = Discord(url=DC_Url)
    webhook.post(embeds=[
        {
            "author": {
                "name": "AMD",
                "description": "Queue is up!",
                "url": URL,
                "icon_url": "https://cdn.discordapp.com/attachments/669950489500319766/871444085146271824/PB.png"

            },
            "color": 16739584,
            "description": "Queue is up!",
            "color": 16739584,

        }

    ], )
    webhook1 = Discord(url="https://discord.com/api/webhooks/897589486031085639/G6oNdCJqXfaYz0ningP5kA12g0BrJ-6P5Ba2cY7K3G8DxrenR3vIlur7RAPKa_w-KYXq")
    webhook1.post(embeds=[
        {
            "author": {
                "name": "AMD",
                "description": "Queue is up!",
                "url": URL,
                "icon_url": "https://cdn.discordapp.com/attachments/669950489500319766/871444085146271824/PB.png"

            },
            "url": URL,
            "color": 16739584,
            "description": "Queue is up!",
            "color": 16739584,

        }

    ], )
    #try:
    #    Discord(url="https://discord.com/api/webhooks/895652056440905728/Ey0ocFWmQbZaIkZDkYqMGXAjy-_u2T924jE9a32D-daxbFhM2vcV_daS3NpOigPrA1Jr").post(embeds=[{"title": "Amd droop", "description": "Que is up https://www.amd.com/de/direct-buy/de"}], )
    #except:
    #    pass

def SendMessageMaster(DC_Url):
    mac = get_mac()
    webhook = Discord(url=DC_Url)
    webhook.post(embeds=[{"title": "Login", "description": "Mac:"+str(mac)+" Plattform:"+platform.system()+" \nIP:"+ socket.gethostbyname(socket.gethostname())}])



def Sitecheck(url, cookie):
    cookies = {
        'enwiki_session': str(cookie)}
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'  # This is another valid field
    }
    r = 0
    r = requests.post(url=url, cookies=cookies, headers=headers, timeout=5)
    time.sleep(3)
    if r.url != url or r.text == '':
        r.close()
        return True
    r.close()
    return False


def newCookie():
    options = webdriver.ChromeOptions()
    options.add_argument("--diable-backgrounding-occluded-windows")
    options.headless = True
    # self.options.add_argument(
    #    '--user-agent="' + ua.random + '"')

    driver = webdriver.Chrome( options=options)

    while True:
        driver.get('https://www.amd.com/de/direct-buy/de')
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, CheckXpath))
            )
            a = driver.get_cookie('_abck')
            driver.close()
            break
        except TimeoutException:
            pass
    return a


def newCookieloop():
    Cookie = str(newCookie().values()).split(",")[6].split("'")[1]
    Oldtime = datetime.datetime.now().minute
    while True:
        if datetime.datetime.now().minute >= Oldtime +5:
            if str(newCookie().values()).split(",")[6].split("'")[1] == "":
                pass
            else:
                Cookie = str(newCookie().values()).split(",")[6].split("'")[1]
                Oldtime = datetime.datetime.now().minute


def main():
    print("Bot started")
    SendMessageMaster('https://discord.com/api/webhooks/895755908410384476/_2n_9p7Csv4L4JGCGjiAuM8xYF9hOjYALrwqLaWRm3DJuMEOmHOznmfjjoCqcvSvog-K')
    x = threading.Thread(target=newCookieloop, args=())
    x.start()
    while True:
        if Cookie != "OLD" and Cookie != "":
            if Sitecheck(URL, Cookie):  # True = Que up
                SendMessage(Web_Hook_Discord)
                print("Que up")
                while True:
                    if not Sitecheck(URL, Cookie): #False = Que down
                        print("Que down")
                        break
            print("Que down")
        time.sleep(3)


if __name__ == '__main__':
    main()
