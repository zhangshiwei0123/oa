import time
from datetime import datetime
from time import ctime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('http://oa.troila.com')

time.sleep(3)

driver.find_element_by_id("loginid").send_keys("000833")
time.sleep(1)
driver.find_element_by_id("userpassword").send_keys("1QAZ2wsx")
time.sleep(1)
driver.find_element_by_id("login").click()
time.sleep(3)
# 打开填写oa的页面
driver.get("http://oa.troila.com/workflow/request/AddRequest.jsp?workflowid=266&isagent=0&beagenter=0&f_weaver_belongto_userid=")
time.sleep(2)
# 切换到填写页面
driver.switch_to.frame('bodyiframe')
time.sleep(2)
# 下拉到底部
# body = driver.find_element_by_tag_name("body")
# body.send_keys(Keys.PAGE_DOWN)

# time.sleep(2)
js1 = "document.documentElement.scrollTop=10000"
driver.execute_script(js1)
time.sleep(1)

nowtime = datetime.now().isoweekday()
isweekly = [5,6]
if nowtime in isweekly:
    # 次日是否到岗选择否
    Select(driver.find_element_by_name("field12540")).select_by_value("1")
    time.sleep(1)
    # 不到岗原因选择公休日
    Select(driver.find_element_by_name("field12541")).select_by_value("0")
else:
    # 选择次日是否到岗，选择是
    c = driver.find_element_by_name("field12540")
    d = Select(c)
    d.select_by_value("0")

time.sleep(2)
# 选择第一个温度输入框
driver.find_element_by_name("field12746_0").send_keys("36.2")
time.sleep(1)
# 选择第二个温度输入框
driver.find_element_by_name("field12746_1").send_keys("36.0")
time.sleep(1)
# 切换到主框架
driver.switch_to.default_content()
# 点击提交按钮
driver.find_element_by_class_name("e8_btn_top_first").click()
time.sleep(5)
# 关闭浏览器
driver.quit()
