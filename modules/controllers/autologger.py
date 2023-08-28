
from modules.controllers.vk import VKController
from modules.controllers.google_sheet import GoogleSheetController
from selenium.webdriver import Chrome

from time import sleep
from random import uniform


class AutoLoggerController:
    vk_main_page = "https://vk.com/"

    def build(self,driver:Chrome, path_to_creds: str, sheet_id: str):
        self.driver = driver
        self.vk_controller = VKController(self.driver)
        self.sheet_controller = GoogleSheetController()
        self.sheet_controller.start_service(path_to_creds, sheet_id)

    def check_logged_accounts(self):
        names = self.sheet_controller.get_all_names()

        self.driver.get(self.vk_main_page)

        for name in names:
            if self.vk_controller.finder.find_certain_account(name) == False:
                self.sheet_controller.write_word_by_name(name,"TRUE","F")
            else:
                self.sheet_controller.write_word_by_name(name,"FALSE","F")

    def login_to_all_accounts(self):
        names = self.sheet_controller.get_names_to_login()

        accounts_data = self.sheet_controller.get_all_login_data(names)

        for account_data in accounts_data:
            self.driver.get(self.vk_main_page)
            is_login_success =  self.vk_controller.login(account_data)
            value_to_sheet = str(not is_login_success).upper()
            if is_login_success == True:
                self.sheet_controller.write_word_by_name(account_data[0],value_to_sheet,"F")
                sleep(uniform(4, 8))
                self.vk_controller.logout()
                sleep(uniform(1, 4))


    def bypass_accounts(self):
        names = self.sheet_controller.get_names_to_bypass()
        self.driver.get(self.vk_main_page)
        for name in names:
            if self.vk_controller.choose_account(name) != False:
                sleep(uniform(5, 10))
                self.sheet_controller.mark_success_bypass(name)
                self.vk_controller.logout()
                sleep(uniform(1, 4))