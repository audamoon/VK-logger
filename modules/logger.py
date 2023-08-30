from time import sleep
from random import uniform
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VKLogger:
    def __init__(self,  driver: Chrome):
        self.driver = driver

    def login(self, account_data:list):
        name = account_data[0]
        login = account_data[1]
        password = account_data[2]

        print(f"Вхожу в профиль {name}")

        self.__enter_login(self.driver, login)
        sleep(uniform(4,5))

        self.__find_captcha(self.driver)

        self.__cancel_sms(self.driver)
        sleep(uniform(4,5))

        self.__enter_password(self.driver,password)
        sleep(uniform(1,2))
        
        result = True
        
        return result
 
    def __enter_login(self, driver:Chrome, login:str):
        login_input = driver.find_element(By.XPATH, "//*[@id='index_email']")
        login_input.click()
        login_input.clear()
        login_input.send_keys(login)
        btn = driver.find_element(By.XPATH, "//button[contains(@class,'VkIdForm__signInButton')]")
        btn.click()

    def __find_captcha(self, driver:Chrome):
        try: 
            driver.find_element(By.XPATH,"//form[contains(@class,'vkc__Captcha__container')]")
            while True:
                sleep(10)
                try:
                    driver.find_element(By.XPATH,"//form[contains(@class,'vkc__Captcha__container')]")
                except:
                    break
            sleep(uniform(2,3))
        except:
            pass
   
    def __cancel_sms(self, driver:Chrome):
        try:
            btn = driver.execute_script('return document.querySelector(".vkc__PureButton__button.vkc__Link__link.vkc__Link__primary.vkc__Bottom__switchToPassword")')
            btn.click()
        except:
            pass

    def __enter_password(self,driver:Chrome,  password:str):
        pass_input = driver.find_element(By.XPATH, "//input[@placeholder='Введите пароль']")
        pass_input.click()
        pass_input.clear()
        pass_input.send_keys(password)
        btn = driver.find_element(By.CLASS_NAME, "vkuiButton__in")
        btn.click()
        
    def __is_success(self, driver:Chrome ,account_name:str):
            name = f"//*[contains(text(),'{account_name}')]"
            try:
                # WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, name)))
                driver.find_element(By.XPATH, name)
                return True
            except: 
                return False
