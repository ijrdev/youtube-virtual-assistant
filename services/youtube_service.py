from sys import exit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from services.audio_service import AudioService
from consts.start import START
from consts.play import PLAY
from consts.pause import PAUSE
from consts.stop import STOP

class YoutubeService():
    __url: str = 'https://www.youtube.com/results?search_query='
    __browser: WebDriver = None

    @classmethod
    def execute(cls, action: int, text: str) -> None:
        if cls.__browser:
            cls.__re_search_term(action, text)
        else:
            cls.__init_browser()
            
            cls.__search_term(text)

    @classmethod
    def __search_term(cls, term: str) -> None:
        try:
            cls.__browser.get(f'{cls.__url}{term}')
            
            cls.__select_video()
        except Exception:
            AudioService.execute_audio('error')
            
            cls.__browser.close()
        
            exit(0)

    @classmethod
    def __re_search_term(cls, action: int, term: str) -> None:
        try:
            if action:
                if action == START:
                    cls.__start_video(term)
                elif action == PLAY or action == PAUSE:
                    cls.__play_pause_video()
                elif action == STOP:
                    cls.__stop_video()
        except Exception:
            AudioService.execute_audio('error')
            
            cls.__browser.close()
        
            exit(0)

    @classmethod
    def __init_browser(cls) -> None:
        try:
            cls.__browser: WebDriver = webdriver.Firefox(executable_path = GeckoDriverManager().install())
        except Exception:
            AudioService.execute_audio('error')
            
            cls.__browser.close()
        
            exit(0)
        
    @classmethod
    def __select_video(cls) -> None:
        element_present: EC = EC.presence_of_element_located((By.ID, 'logo-icon'))
        
        WebDriverWait(cls.__browser, 5).until(element_present)
        
        video_title: WebElement = cls.__browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
        
        ActionChains(cls.__browser).move_to_element(video_title).click().perform()
        
    @classmethod
    def __start_video(cls, term: str) -> None:
        cls.__browser.get(f'{cls.__url}{term}')
            
        cls.__select_video()    
    
    @classmethod
    def __play_pause_video(cls) -> None:
        element_present: EC = EC.presence_of_element_located((By.ID, 'logo-icon'))
        
        WebDriverWait(cls.__browser, 5).until(element_present)
        
        video_button_play_pause: WebElement = cls.__browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[1]/video')
        
        ActionChains(cls.__browser).move_to_element(video_button_play_pause).click().perform()
    
    @classmethod
    def __stop_video(cls) -> None:
        AudioService.execute_audio('stop')
        
        cls.__browser.close()
        
        exit(0)