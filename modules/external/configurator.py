import undetected_chromedriver as uc
import os


class ChromeConfigurator():

    __user_path = (os.environ['LOCALAPPDATA'] + "\\Google\\Chrome\\User Data\\Profile1")

    def __init__(self):
        self.__set_driver()

    def __set_driver(self):
        self.__options = uc.ChromeOptions()
        self.__options.add_argument(f"--user-data-dir={self.__user_path}")
        self.__driver = uc.Chrome(
            browser_executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe",
            options=self.__options)

    def get_driver(self):
        return self.__driver