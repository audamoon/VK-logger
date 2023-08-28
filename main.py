from modules.external.configurator import ChromeConfigurator
from modules.controllers.vk import VKController
from modules.controllers.google_sheet import GoogleSheetController


from time import sleep
from random import uniform

driver = ChromeConfigurator().get_driver()

vk_controller = VKController(driver)

sheet_controller = GoogleSheetController()
sheet_controller.start_service(
    "creds/service_account_creds.json", "1oeOIuft_E3A-UNrSaeV1yILYfbyB2OQGnOPF1uxYz_c")

sheet_mgr = sheet_controller.manager
vk_main_page = "https://vk.com/"


def check_logged_accounts():
    names = sheet_mgr.reader.read_range("A2:A")
    driver.get(vk_main_page)
    for name in names:
        if vk_controller.finder.find_certain_account(name[0]) == False:
            sheet_controller.write_word_by_name(name[0],"TRUE","F")
        else:
            sheet_controller.write_word_by_name(name[0],"FALSE","F")

def login_to_ten_accounts():
    names = sheet_controller.get_names_to_login()
    accounts_data = sheet_controller.get_all_login_data(names)
    i = 0
    for account_data in accounts_data:
        if i > 10:
            break
        try:
            driver.get(vk_main_page + "login")
            is_login_success =  vk_controller.login(account_data)
            to_sheet = str(not is_login_success).upper()
            if is_login_success == True:
                sheet_controller.write_word_by_name(account_data[0],to_sheet,"F")
                sleep(uniform(4, 8))
                vk_controller.logout()
                sleep(uniform(1, 4))
                i += 1
            else:
                pass
        except:
            sheet_controller.write_word_by_name(account_data[0],"Что-то пошло не так","G")

def bypass_accounts():
    names = sheet_controller.get_names_to_bypass()
    driver.get(vk_main_page)
    for name in names:
        try:
            if vk_controller.choose_account(name) != False:
                sleep(uniform(5, 10))
                sheet_controller.mark_success_bypass(name)
                vk_controller.logout()
                sleep(uniform(1, 4))
        except:
            continue


            
# check_logged_accounts()
# login_to_ten_accounts()
# bypass_accounts()

