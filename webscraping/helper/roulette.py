import requests
from datetime import datetime
from src.helpers import configs, scripts, regex as re
from selenium.webdriver.common.by import By
import time


def run(browser, temp=None):
    urls = configs.get_urls()
    page_elements = configs.get_elements('live_roulette')

    if browser.current_url != urls['live_roulette']:
        browser.get(urls['live_roulette'])

    try:
        time.sleep(10)
        iframe_outside = browser.get_element(By.CLASS_NAME, page_elements['iframe_outside'])
        browser.switch_to.frame(iframe_outside)
        iframe2 = browser.get_element(By.ID, 'gamecontent')
        browser.switch_to.frame(iframe2)
    except Exception as e: 
        print("error to get iframe", e)
        return

    temp_numbers = temp
    print('temp: ', temp_numbers)

    start = time.time()
    count = 0
    while True:
        try:
            # get numbers
            try:
                numbers = browser.get_element(By.CLASS_NAME, 'roulette-game-area__history-line').text
            except Exception as e:
                print("numbers not found", e)
                return temp_numbers
            numbers = [int(n) for n in numbers.split('\n')]

            if temp_numbers:
                cond = all(list(map(lambda a, b: a == b, temp_numbers, numbers)))
                cond2 = len(temp_numbers) > len(numbers)
                if cond or cond2:
                    continue

            temp_numbers = numbers.copy()
            print(time.time() - start, ' ', numbers)

            count += 1
            with requests.post(f'http://127.0.0.1:8000/history/roulette/',
                               json={
                                   "number": numbers[0],
                                   "time": datetime.now().isoformat()
                               }) as res:
                res = res.json()
                if res['notifier'] == 'attentive_message':
                    return temp_numbers
            if count >= 4:
                return temp_numbers
            start = time.time()

        except Exception as e: 
            print("error to get numbers", e)
            return temp_numbers
