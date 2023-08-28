class VKLogger:
    def __init__(self,driver) -> None:
        self.driver = driver
    def is_save_btn_on(self):
        if self.driver.execute_script('el = document.querySelector(".VkIdCheckbox__checkboxOn");if (window.getComputedStyle(el).display != "block"){return el}') == None:
            return True 
        else:
            return False