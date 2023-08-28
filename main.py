from modules.external.configurator import ChromeConfigurator
from modules.controllers.autologger import AutoLoggerController
from time import sleep
from random import uniform

driver = ChromeConfigurator().get_driver()

controller = AutoLoggerController()
controller.build(driver,"creds/service_account_creds.json", "1oeOIuft_E3A-UNrSaeV1yILYfbyB2OQGnOPF1uxYz_c")
controller.check_logged_accounts()
controller.login_to_all_accounts()
controller.bypass_accounts()