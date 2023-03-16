# coding=gbk
# web自动化基本代码
# 1.导入模块


import allure, pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os

# 2.实例化浏览器对象：类名（） 用一个函数接收
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome(options=option)


@allure.feature('应付汇总-UI')
@allure.story('登录')
@allure.title('登录系统')
def test_dl():
    with allure.step('打开网页'):
        web.get('http://192.168.0.109:9628/#/nuclearprice/baojia')
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
        allure.attach(web.get_screenshot_as_png(), '登录前截图', allure.attachment_type.PNG)
        sleep(2)
        allure.attach(web.get_screenshot_as_png(), '登录后截图', allure.attachment_type.PNG)
    with allure.step("点击侧边栏收缩"):
        web.find_element(By.ID, 'hamburger-container').click()
        sleep(3)


def test_bjd():
    web.execute_script("window.scrollTo(0, 230)")
    sleep(2)
    with allure.step('点击新建报价'):
        sleep(2)
        web.find_element(By.XPATH, "//span[normalize-space()='新建报价']").click()
        sleep(2)
    with allure.step('输入报价单名称'):
        web.find_element('name','wjm_1').send_keys('今天的测试')
        sleep(2)
    with allure.step('选择客户'):
        web.find_element('name','toSearch').click()
        sleep(2)
    with allure.step('点击选择'):
        web.find_elements(By.LINK_TEXT, "选择")[2].click()
        sleep(2)



# def test_xsd():
#     web.execute_script("window.scrollTo(0, 230)")
#     sleep(2)
#     with allure.step('点击销售订单'):
#         web.find_element(By.XPATH, "//span[normalize-space()='XD23030036']").click()
#         sleep(2)
#     with allure.step('点击物流计划'):
#         web.find_element(By.ID, 'tab-logistics').click()
#         sleep(2)
#     with allure.step('新建计划'):
#         web.find_element(By.XPATH, "//span[normalize-space()='新建计划']").click()
#     with allure.step('点击地址列表'):
#         web.find_element(By.XPATH, "//span[normalize-space()='地址列表']").click()
#         sleep(4)
#     with allure.step('点击选择'):
#         web.find_element(By.XPATH, "//span[normalize-space()='选 择']").click()
#     sleep(5)
