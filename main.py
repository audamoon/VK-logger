from modules.external.configurator import ChromeConfigurator
from modules.controllers.vk import VKController
from modules.controllers.google_sheet import GoogleSheetController


from time import sleep
from random import uniform

driver = ChromeConfigurator().get_driver()
controller = VKController(driver)

# sheet_mgr = GoogleSheetController()
# sheet_mgr.start_service("creds/service_account_creds.json","1oeOIuft_E3A-UNrSaeV1yILYfbyB2OQGnOPF1uxYz_c")

# names = sheet_mgr.get_names_to_login()
# b = sheet_mgr.get_all_login_data(names)
# print(b)
# vk_main_page = "https://vk.com/"

# driver.get(vk_main_page)

vk_login_page = "https://vk.com/login"
driver.get(vk_login_page)

print(controller.logger.is_save_btn_on())
# sleep(uniform(1, 3))

# for name in names:
#     controller.choose_account(name)
#     sleep(uniform(5, 10))

#     controller.logout()
#     sleep(uniform(1, 4))