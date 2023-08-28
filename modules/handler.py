from selenium.webdriver import Chrome
from modules.actions import ScriptActions


class VKHandler:
    def __init__(self,driver:Chrome) -> None:
        self.driver = driver
    
    def make_action(self, attribute_object:ScriptActions, element, is_logout=False):
        attribute_object.make_action(self.driver, element, is_logout)