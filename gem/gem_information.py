from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_tools import BaseDisplay
from selenium_tools import user_agent

URL = 'https://gem.xyz'


class Gem(BaseDisplay):
    def __init__(self, contract_address: str, url: str = URL, user_driver: str = 'chrome'):
        BaseDisplay.__init__(self)
        self.url: str = url
        self.driver: webdriver = None
        self.user_driver: str = user_driver
        self.contract_address: str = contract_address

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
            return False
        options = self._browser_options()
        options.add_argument(f'user-agent={user_agent()}')
        return options

    def by_collection_address(self):
        """Prepares the part of link with params for major link"""
        collection_by_address = '/collection/' + self.contract_address
        return self._link(collection_by_address)

    def initial_information_by_tag(self, byxpath: bool = True) -> dict:
        """Responds with the initial information of the gem as a dictionary"""
        if byxpath is True:
            name_collection = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div').text
            price_change = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/span[2]').text
            floor_price = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/span[3]/span[2]').text
            return {'price_change': f'24h: {price_change}', 'floor_price': floor_price, 'name_collection': name_collection}

    def start(self):
        """Starts the browser"""
        self.start_display()
        browser_options = self._prepare_options()
        self.driver = webdriver.Chrome(executable_path='chromedriver', options=browser_options)
        return self.driver
