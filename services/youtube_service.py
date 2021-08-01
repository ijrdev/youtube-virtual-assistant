from random import randint
from selenium import webdriver
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from models.youtube import Youtube

class YoutubeService():
    __url: str = 'https://www.youtube.com/results?search_query='
    __browser: WebDriver = None

    @classmethod
    def execute(cls, text: str) -> None:
        if cls.__browser:
            cls.re_search_term(text)
        else:
            cls.init_browser(text)
            
            cls.search_term()

    @classmethod
    def search_term(cls) -> None:
        try:
            element_present: EC = EC.presence_of_element_located((By.ID, 'video-title'))

            videos_title: list = cls.__browser.find_elements_by_xpath("//*[@id='video-title']")
            
            WebDriverWait(cls.__browser, 5).until(element_present)
            
            if not videos_title:
                pass
            
            ActionChains(cls.__browser).move_to_element(videos_title[0]).click().perform()
        except Exception as ex:
            raise Exception('Unable to search the youtube video.')

    @classmethod
    def re_search_term(cls, term: str) -> None:
        try:
            search_input: dict = cls.__browser.find_element_by_id('search')
            search_button: dict = cls.__browser.find_element_by_id('search-icon-legacy')
            
            ActionChains(cls.__browser).move_to_element(search_input).click().key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).send_keys(term).perform()
            ActionChains(cls.__browser).move_to_element(search_button).click().perform()
            
            cls.search_term()
        except Exception as ex:
            raise Exception('Unable to research the youtube video.')

    @classmethod
    def init_browser(cls, term: str) -> None:
        try:
            cls.__browser: WebDriver = webdriver.Firefox(executable_path = GeckoDriverManager().install())
            
            cls.__browser.get(f'{cls.__url}{term}')
        except:
            raise Exception('Unable to open browser.')
