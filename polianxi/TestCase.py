from unittest import TestCase
import unittest
from selenium import webdriver
from time import sleep
from Page import SearchPage
class CaseRun(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        sleep(2)
        self.url = "https://www.baidu.com/"
        sleep(2)
        self.content = "日期"
    # 测试步骤
    def test_search(self):
        bing_page = SearchPage(self.driver,self.url)
        bing_page.open()
        sleep(1)
        bing_page.search_content(self.content)
        sleep(2)
        bing_page.btn_click()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()