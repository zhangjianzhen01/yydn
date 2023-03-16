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


@allure.title('登录系统')
def test_dl():
    with allure.step('打开网页'):
        web.get('http://192.168.0.217:9900/?#/copsummary')
    with allure.step("最大化窗口"):
        web.maximize_window()
    with allure.step("清空输入框"):
        web.find_element('name', 'username').clear()
    with allure.step("输入账号"):
        web.find_element('name', 'username').send_keys('admin')
    with allure.step("输入密码"):
        web.find_element('name', 'password').send_keys('huazhou333')
    with allure.step("登录"):
        sleep(2)
        web.find_element('name', 'login').click()
    # 截图登录前
    allure.attach(web.get_screenshot_as_png(), '登录前截图', allure.attachment_type.PNG)
    # 截图登录后
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '登录后截图', allure.attachment_type.PNG)
    # 点击左侧缩放
    web.find_element(By.ID, 'hamburger-container').click()


@allure.title('未税')
def test_ws():
    with allure.step('输入订单号'):
        web.find_element('name', 'business_no').send_keys('XD23010056')
        sleep(2)
    with allure.step('下拉页面'):
        web.execute_script("window.scrollTo(0, 250)")
    with allure.step('回车'):
        web.find_element('name', 'business_no').send_keys(Keys.ENTER)
    with allure.step('点击订单号'):
        sleep(2)
        web.find_element('name', 'business_no_0').click()
    with allure.step('点击未税信息'):
        sleep(2)
        web.find_element(By.ID, 'tab-sixth').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '未税信息页面', allure.attachment_type.PNG)
    sleep(2)
    with allure.step('点击新增'):
        web.find_element(By.XPATH, "//span[contains(., '新增')]").click()
        sleep(2)
    # with allure.step("清空输入框"):
    #     web.find_element('name', 'refund_amount').clear()
    # with allure.step('输入退款金额'):
    #     web.find_element('name', 'refund_amount').send_keys('188')
    #     sleep(2)
    # with allure.step('点击保存'):
    #     web.find_element('name', 'sureDialog').click()
    # sleep(3)
    # allure.attach(web.get_screenshot_as_png(), '截图退款', allure.attachment_type.PNG)
    # sleep(2)
