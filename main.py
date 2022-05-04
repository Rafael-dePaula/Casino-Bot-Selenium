from webscraping.browser import Browser
import time

browser = Browser()
browser.get('https://www.google.com')
temp = None
while True:
    try:
        browser.login()
        temp = browser.roulette(temp)
    finally:
        ...
