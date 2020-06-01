from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.market import Market


class Main(BasePage):
    def goto_market(self):
        #进入行情页面
        self.find(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return Market(self._driver)

    # def goto_search(self):
    #     # self.find(By.ID,'com.xueqiu.android:id/tv_search').click()
    #     self.steps("../page/main.yaml")
    #
    # def goto_windows(self):
    #     self.find(By.ID, "post_status").click()
    #     self.find(By.ID, 'tv_search').click()

