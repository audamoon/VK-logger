import re


class ScriptActions():
    def make_action(self, driver, element, *args): raise NotImplementedError


class OnClicK(ScriptActions):
    def make_action(self, driver, element, *args):
        onclick = element.get_attribute("onclick")
        driver.execute_script(re.sub("return", "", onclick))


class Href(ScriptActions):
    def make_action(self, driver, element, is_logout: bool = False):
        href = element.get_attribute("href")
        if is_logout:
            driver.get(re.sub("(lrt.+&)", "", href))
        return