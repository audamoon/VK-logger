from modules.finder import VKFinder
from modules.handler import VKHandler
from modules.common.attribute import ActionType
from modules.logger import VKLogger
import re


class VKController:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.finder = VKFinder(self.driver)
        self.handler = VKHandler(self.driver)
        self.logger = VKLogger(self.driver)

    def choose_account(self, account_name):
        account = self.finder.find_certain_account(account_name)
        self.handler.make_action(ActionType.ONCLICK, account)

    def logout(self):
        btn = self.finder.find_logout()
        self.handler.make_action(ActionType.HREF, btn, True)

    def login(self):
        return self.logger.is_save_btn_on()