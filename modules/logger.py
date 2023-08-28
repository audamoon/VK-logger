from time import sleep
from random import uniform
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class VKLogger:
    def __init__(self,  driver: Chrome):
        self.driver = driver

    def login(self, account_data:list):
        name = account_data[0]
        login = account_data[1]
        password = account_data[2]

        save_btn = self.__is_save_btn_on()
        if save_btn != True:
            save_btn.click()
            sleep(uniform(1,2))

        self.__enter_login(login)
        sleep(uniform(2,3))
    
        self.__find_captcha()
        
        self.__check_sms()

        sleep(uniform(2,3))
        
        self.__enter_password(password)
        sleep(uniform(5,10))

        return self.__is_success(name)

    def __is_save_btn_on(self):
        btn = self.driver.execute_script('el = document.querySelector(".VkIdCheckbox__checkboxOn");if (window.getComputedStyle(el).display != "block"){return el}')
        if btn == None:
            return True 
        else:
            return btn
    
    def __find_captcha(self):
        try: 
            self.driver.find_element(By.XPATH,"//form[contains(@class,'vkc__Captcha__container')]")
            while True:
                sleep(10)
                try:
                    self.driver.find_element(By.XPATH,"//form[contains(@class,'vkc__Captcha__container')]")
                except:
                    break
            sleep(uniform(2,3))
        except:
            pass

    def __enter_login(self, login:str):
        login_input = self.driver.find_element(By.ID, "index_email")
        login_input.click()
        login_input.clear()
        login_input.send_keys(login)
        btn = self.driver.find_element(By.XPATH, "//button[contains(@class,'VkIdForm__signInButton')]")
        btn.click()

    def __check_sms(self):
        try:
            self.driver.find_element(By.XPATH("//span[text()='Войти при помощи пароля']/parent::button")).click()
        except:
            pass

    def __enter_password(self, password:str):
        pass_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Введите пароль']")
        pass_input.click()
        pass_input.clear()
        pass_input.send_keys(password)
        btn = self.driver.find_element(By.CLASS_NAME, "vkuiButton__in")
        btn.click()
        
    def __is_success(self,account_name):
        try:
            self.driver.find_element(By.XPATH,f"//*[text()='{account_name}']")
            return True
        except:
            return False

