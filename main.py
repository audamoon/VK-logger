from modules.external.configurator import ChromeConfigurator, ProfileID
from modules.controllers.autologger import AutoLoggerController


def start():
    for profile_id in profile_ids:
        print("#" * 20)
        print(f"Начинаю выполнение программы для {profile_id}")
        driver = ChromeConfigurator(str(profile_id)).get_driver()
        controller = AutoLoggerController()
        controller.build(driver,"creds/service_account_creds.json", "1oeOIuft_E3A-UNrSaeV1yILYfbyB2OQGnOPF1uxYz_c")
        # controller.check_logged_accounts()
        try:
            controller.login_to_all_accounts(profile_id.replace("Profile ", ""))
            print("Ура все получилось B-)")
        except:
            print("С программой что-то не так :'(")
            pass
        # controller.bypass_accounts()
        print("Выхожу из браузера.")
        driver.quit()


profile_ids = ProfileID().get_ids()



while True:
    print("Добро пожаловать в программу для входа в аккаунты ВК (^_^)")
    print(f"Занесённые в программу профили: {profile_ids}")
    print("Пожалуйста, выберите опции (чтобы выйти введите 0):")
    print("1. Тестовый запуск :D ")
    user_input = input("Вы ввели: ")
    if "1" in user_input:
        start()
    else:
        break