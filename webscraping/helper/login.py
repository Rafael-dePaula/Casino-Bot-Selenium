from src.helpers import configs, scripts
from selenium.webdriver.common.by import By
import time


def confirms(browser):
    page_elements = configs.get_elements('live_roulette')

    # identity confirm
    time.sleep(5)

    try:
        iframe_member = browser.get_element(by=By.CSS_SELECTOR,
                                            value='iframe.members-notifications-frame.overlayWholePage')
        browser.switch_to.frame(iframe_member)
        el = browser.get_element(by=By.ID, value='remindLater')
        el.click()
    except Exception as e:
        print("remind later button not found: ", e)
    finally:
        browser.switch_to.default_content()

    time.sleep(2)
    # logged confirm
    try:
        el = browser.get_element(by=By.CSS_SELECTOR, value=page_elements['logged_btn'])
        el.click()

    except Exception as e:
        print("logged confirm element not found: ", e)


def run(browser, user=None):
    # Get important infos
    urls = configs.get_urls()
    user = configs.get_user()

    # Load scripts
    script_check_login = scripts.check_login()
    script_login = scripts.sign_in()

    # Load Page
    browser.get(urls['login'])

    # Already logged ?
    time.sleep(2)
    already_logged: bool = browser.compile_and_run(script_check_login)['value']

    if already_logged:
        print("Already logged")
        return

    time.sleep(5)

    # Login
    _ = browser.compile_and_run(script_login)
    print('logged')
    time.sleep(5)
    print('check confirms')
    confirms(browser)
