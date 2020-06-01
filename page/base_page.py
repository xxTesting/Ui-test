import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from page.wrapper import handle_black


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement

        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator,value)
        return element

    def finds(self, locator, value: str = None):
        elements: list

        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def steps(self,path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"],step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()