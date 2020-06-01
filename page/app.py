import yaml
from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self._driver is None:
            desired_caps = {
                "platformName": "Android",
                "automationName": "UIAutomator2",
                "platformVersion": "6",
                "deviceName": "127.0.0.1:7555",
                # "udid":yaml.safe_load("../page/configuation.yaml")['caps']['udid'],
                "appPackage": self._package,
                "appActivity":self._activity,
                "noReset": True,
                "skipDeviceInitialization": True,
                "unicodeKeyBoard": True,
                "resetKeyBoard": True
            }
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        else:
            self._driver.start_activity(self._package,self._activity)

        self._driver.implicitly_wait(10)

        return self

    def main(self) -> Main:
        return Main(self._driver)
