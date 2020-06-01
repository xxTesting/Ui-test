from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.search import Search


class Market(BasePage):
    def goto_search(self):
        #点击搜索图标
        # self.find(By.ID,"com.xueqiu.android:id/action_search").click()
        return Search(self._driver)