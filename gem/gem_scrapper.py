import json
import os
from pathlib import Path
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from general_tools import BaseDisplay
from general_tools import user_agent

env = Path(os.path.dirname(__file__)).parent.resolve().joinpath('.env')
if os.path.isfile(env):
    load_dotenv(env)

URL = os.getenv('GEMXYZ_URL')


class GemScrapper(BaseDisplay):
    def __init__(self, contract_address: str, url: str = URL, user_driver: str = 'chrome'):
        BaseDisplay.__init__(self)
        self.url: str = url
        self.driver: webdriver = None
        self.user_driver: str = user_driver
        self.contract_address: str = contract_address
        self.capabilities = DesiredCapabilities.CHROME

    def _browser_options(self):
        """Chooses the browser options to use"""
        if self.user_driver == 'chrome':
            return webdriver.ChromeOptions()
        else:
            return False

    def _link(self, params: str):
        """Creates link for request"""
        return self.url + params

    def _prepare_options(self):
        """Prepares the browser options, like that the user agent is set"""
        if self._browser_options() is False:
            pass
        options = self._browser_options()
        options.add_argument(f'user-agent={user_agent()}')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        return options

    def by_collection_address(self):
        """Prepares the part of link with params for major link"""
        collection_by_address = '/collection/' + self.contract_address
        return self._link(collection_by_address)

    def __information_of_collection_by_devtools(self):
        """Info of collection by response from devtools"""
        logs_raw = self.driver.get_log("performance")
        logs = [json.loads(lr["message"])["message"] for lr in logs_raw]

        def log_filter(log_):
            return (
                    log_["method"] == "Network.responseReceived"
                    and "json" in log_["params"]["response"]["mimeType"])

        return filter(log_filter, logs)

    def response_information(self):
        """Outputs the information"""
        count = 0
        while count < 10:
            logs = self.__information_of_collection_by_devtools()
            for log in logs:
                if log["params"]["response"]["url"].endswith('/collections'):
                    response = self.driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": log["params"]["requestId"]})
                    return json.loads(response['body'])
            count += 1
            sleep(1)
        return False

    def start(self):
        """Starts the browser"""
        self.start_display()
        browser_options = self._prepare_options()
        self.capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        # service=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(desired_capabilities=self.capabilities, executable_path='/usr/local/bin/chromedriver',
                                       options=browser_options)
        return self.driver
