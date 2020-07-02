from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """BasePage封装所有页面的公有方法，例如url、driver、find_element"""
    # 构造函数里面的参数就是类的所有参数
    def __init__(self,selenuime_driver,base_url):
        self.driver = selenuime_driver
        self.url = base_url

    # 定义一个私有方法，其他类不能调用该方法
    def _open(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    # 定义open()方法，调用_open()方法
    def open(self):
        self._open(self.url)

    # 重写find_element()方法，参数为任意数量的（带*的参数）
    # 此方法是为了保证元素是可见的
    def find_emelemt(self,*loc):
        try:
            # 保证元素可见
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("页面中没有%s元素"%(self.loc))

    # 定义script()方法，用于执行JS脚本，比方上上传文件啥的
    def script(self,src):
        self.driver.excute_script(src)

    # 定义页面跳转方法，比方说有的页面有frame嵌套
    def switch_frame(self,loc):
        return self.driver.switch_to_frame(loc)

    # 重新定义send_keys()方法，为了保证搜索按钮是否存在，还有有的输入框中默认有值，要清空
    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            # getattr方法相当于实现了self.loc
            loc = getattr(self,"_%s"%loc)
            # 是否存在搜索按钮
            if click_first:
                self.find_emelemt(*loc).click()
            # 清空搜索框中的值，并输入需要搜索的值
            if clear_first:
                self.find_emelemt(*loc).clear()
                self.find_emelemt(*loc).send_keys(value)

        except:
            print("页面上未找到%s元素"%(self.loc))