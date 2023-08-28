from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class VKFinder:
    def __init__(self,driver:Chrome) -> None:
        self.driver = driver

    def __get_all_accounts(self):
        return self.driver.find_elements(By.XPATH, "//button[@class='index_user_row _row inl_bl']")

    def find_certain_account(self, account_name:str):
        accounts = self.__get_all_accounts()
        for account in accounts:
            account_name_from_vk = account.get_attribute("aria-label")
            if account_name == account_name_from_vk:
                return account
        return False
            
    def find_logout(self):
        logout_btn = self.driver.find_element(By.ID, "top_logout_link")
        return logout_btn