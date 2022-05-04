from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
import selenium.webdriver.support.expected_conditions as ExpectedConditions
from .helper import login, roulette
PATH = 'src/driver/chromedriver'


class Browser(Chrome):
    first_login: bool = True

    def __init__(self, path=PATH, options=None):
        if options is None:
            options = configure_options()
        super().__init__(executable_path=path, options=options)
        self.webDriverWait = WebDriverWait(self, 10, poll_frequency=5)
        self.minimize_window()

    def login(self, user=None):
        login.run(self)

    def roulette(self, temp=None):
        return roulette.run(self, temp)

    def get_element(self, by, value, multiples=False):
        self.webDriverWait.until(
            ExpectedConditions.presence_of_element_located(
                (by, value))
        )
        if multiples:
            return self.find_elements(by=by, value=value)
        return self.find_element(by=by, value=value)

    def compile_and_run(self, script, **cmd_args):
        script_id = self.execute_cdp_cmd(
            'Runtime.compileScript',
            {'expression': script,
             'sourceURL': 'Top',
             'persistScript': True,
             })['scriptId']

        result = self.execute_cdp_cmd(
            'Runtime.runScript',
            {'scriptId': script_id,
             'silent': True,
             })['result']
        return result


def configure_options():
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    return options
