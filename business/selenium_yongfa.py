# web自动化基本代码
# 1.导入模块
import allure, pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# 2.实例化浏览器对象：类名（） 用一个函数接收
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome(options=option)

# span点击
web.find_element(By.XPATH, "//span[normalize-space()='x']").click()
# 多span同名
web.find_elements(By.XPATH, "//span[normalize-space()='x']")[1].click()  # [x]是列表中第几个，从0开始
# 纯文本点击跳转
web.find_element(By.LINK_TEXT, "XXXXXXXXXXX").click()
# 输入内容
web.find_element('name', 'refund_amount').send_keys('188')
# 清除输入框
web.find_element('name', 'sureDialog').clear()
# 点击元素名name的按键
web.find_element('name', 'sureDialog').click()
# 截图
allure.attach(web.get_screenshot_as_png(), '截图退款', allure.attachment_type.PNG)
# 下拉页面
web.execute_script("window.scrollTo(0, 250)")
# 回车
web.find_element('name', 'business_no').send_keys(Keys.ENTER)
# 键盘操作
'https://www.jianshu.com/p/48c95a77bd45'
# allure定制报告
'https://zhuanlan.zhihu.com/p/455445067'

# pytest没有log
'--capture=sys'

# 安装jinkins
'https://mp.weixin.qq.com/s/a0JOuiqLsUMcQSEjZ4uGTg'
# nginx+allure策略
'https://www.cnblogs.com/xiongjianwen/p/17025269.html'
# 生成报告命令
'pytest .\demo.py -sv --alluredir=./result --capture=sys'
'allure generate .\result\ -o .\BG  --clean'
