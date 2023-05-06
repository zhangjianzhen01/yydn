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
        web.get('http://192.168.0.21:9091/#/copsummary')
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

    # @allure.feature('应付汇总-UI')
    # @allure.story('高级筛选')
    # @allure.title('订单号搜索')
    # def test_ddh():
    #     with allure.step('点击折叠框'):
    #         sleep(2)
    #         web.find_element('name', 'lls_10').click()
    #         sleep(2)
    #         allure.attach(web.get_screenshot_as_png(), '点击折叠框', allure.attachment_type.PNG)
    #     with allure.step('输入订单号'):
    #         web.find_element('name', 'lls_5').send_keys('XD22090149')
    #         sleep(2)
    #     with allure.step('下拉页面'):
    #         web.execute_script("window.scrollTo(0, 300)")
    #         sleep(2)
    #     with allure.step('点击搜索'):
    #         web.find_element('name', 'lls_99').click()
    #         sleep(5)
    #         allure.attach(web.get_screenshot_as_png(), '搜索订单号结果', allure.attachment_type.PNG)
    #
    #
    # @allure.feature('应付汇总-UI')
    # @allure.story('高级筛选')
    # @allure.title('查询字段-备注')
    # def test_bz():
    #     web.execute_script("window.scrollTo(0, 100)")
    #     sleep(2)
    #     with allure.step('重置'):
    #         web.find_elements(By.XPATH, "//span[normalize-space()='重置']")[1].click()
    #         sleep(2)
    #     with allure.step('点击备注'):
    #         sleep(2)
    #         web.find_element(By.XPATH, "//span[normalize-space()='备注']").click()
    #         sleep(4)
    #         allure.attach(web.get_screenshot_as_png(), '点击备注', allure.attachment_type.PNG)
    #     with allure.step('输入内容'):
    #         sleep(2)
    #         web.find_element('name', 'lls_8').send_keys('测试')
    #         sleep(2)
    #         allure.attach(web.get_screenshot_as_png(), '输入搜索内容', allure.attachment_type.PNG)
    #     with allure.step('点击搜索'):
    #         web.find_element('name', 'lls_99').click()
    #         web.execute_script("window.scrollTo(0, 300)")
    #         allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    #         sleep(3)
    #     with allure.step('点击订单号超链接'):
    #         web.find_element(By.LINK_TEXT, 'XD23020139').click()
    #         sleep(5)
    #     with allure.step('点击未税信息'):
    #         web.find_element(By.ID, 'tab-sixth').click()
    #         sleep(2)
    #         allure.attach(web.get_screenshot_as_png(), '未税信息备注页面', allure.attachment_type.PNG)
    #     with allure.step('刷新一次'):
    #         sleep(3)
    #         web.refresh()
    #         sleep(2)
    #     with allure.step('点击折叠框'):
    #         sleep(2)
    #         web.find_element('name', 'lls_10').click()
    #
    #
    # @allure.feature('应付汇总-UI')
    # @allure.story('高级筛选')
    # @allure.title('查询字段-摘要')
    # def test_zy():
    #     with allure.step('点击摘要'):
    #         sleep(2)
    #         web.find_element(By.XPATH, "//span[normalize-space()='摘要']").click()
    #         sleep(2)
    #         allure.attach(web.get_screenshot_as_png(), '点击摘要', allure.attachment_type.PNG)
    #     with allure.step('输入内容'):
    #         sleep(2)
    #         web.find_element('name', 'lls_8').send_keys('测试')
    #         sleep(2)
    #         allure.attach(web.get_screenshot_as_png(), '输入搜索内容', allure.attachment_type.PNG)
    #     with allure.step('点击搜索'):
    #         web.find_element('name', 'lls_99').click()
    #         web.execute_script("window.scrollTo(0, 300)")
    #         allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    #         sleep(3)
    #     with allure.step('点击订单号超链接'):
    #         web.find_element(By.LINK_TEXT, 'XD23030016').click()
    #         sleep(5)
    #     with allure.step('点击销售明细'):
    #         web.find_element(By.ID, 'tab-second').click()
    #         sleep(2)
    #         web.execute_script("window.scrollBy(0,500)")
    #         sleep(5)
    #         allure.attach(web.get_screenshot_as_png(), '销售明细页面', allure.attachment_type.PNG)
    #     with allure.step('刷新一次'):
    #         sleep(3)
    #         web.refresh()
    #         sleep(2)
    #     with allure.step('点击折叠框'):
    #         sleep(2)
    #         web.find_element('name', 'lls_10').click()

    sleep(2)
    web.find_element('name', 'lls_10').click()
    sleep(2)
    web.execute_script("window.scrollTo(0, 250)")


@allure.feature('应付汇总-UI')
@allure.story('高级筛选')
@allure.title('日期筛选')
def test_rqsx():
    sleep(2)
    with allure.step('点击收款日期'):
        web.find_element(By.XPATH, "//span[normalize-space()='收款日期']").click()
        sleep(2)
        allure.attach(web.get_screenshot_as_png(), '点击收款日期', allure.attachment_type.PNG)
    with allure.step('选择时间'):
        web.find_element(By.CLASS_NAME, 'el-input__icon.el-range__icon.el-icon-date').click()
        sleep(1)
        web.find_element(By.XPATH, "//span[normalize-space()='1']").click()
        sleep(1)
        web.find_element(By.XPATH, "//span[normalize-space()='16']").click()
        sleep(2)
        allure.attach(web.get_screenshot_as_png(), '选择时间', allure.attachment_type.PNG)
    with allure.step('点击搜索'):
        sleep(2)
        web.find_elements(By.XPATH, "//span[normalize-space()='搜索']")[1].click()
        sleep(2)
        web.execute_script("window.scrollTo(0, 300)")
        sleep(2)
        allure.attach(web.get_screenshot_as_png(), '收款日期搜索结果', allure.attachment_type.PNG)
    with allure.step('点击开票日期'):
        sleep(2)
        web.find_element(By.XPATH, "//span[normalize-space()='收款日期']").click()
        web.find_element(By.XPATH, "//span[normalize-space()='开票日期']").click()
        sleep(2)
    with allure.step('点击搜索'):
        web.find_elements(By.XPATH, "//span[normalize-space()='搜索']")[1].click()
        sleep(2)
        allure.attach(web.get_screenshot_as_png(), '开票搜索结果', allure.attachment_type.PNG)
    with allure.step('点击订单日期'):
        web.find_element(By.XPATH, "//span[normalize-space()='开票日期']").click()
        web.find_element(By.XPATH, "//span[normalize-space()='订单日期']").click()
        sleep(2)
    with allure.step('点击搜索'):
        web.find_elements(By.XPATH, "//span[normalize-space()='搜索']")[1].click()
        sleep(2)
        allure.attach(web.get_screenshot_as_png(), '订单日期搜索结果', allure.attachment_type.PNG)
    with allure.step('点击预计交货日期'):
        web.find_element(By.XPATH, "//span[normalize-space()='订单日期']").click()
        web.find_element(By.XPATH, "//span[normalize-space()='预计交货日期']").click()
        sleep(2)
    with allure.step('点击搜索'):
        web.find_elements(By.XPATH, "//span[normalize-space()='搜索']")[1].click()
        sleep(2)
        allure.attach(web.get_screenshot_as_png(), '预计交货日期搜索结果', allure.attachment_type.PNG)
        sleep(2)
    web.find_element(By.XPATH, "//span[normalize-space()='预计交货日期']").click()
    sleep(2)


@allure.feature('应付汇总-UI')
@allure.story('高级筛选')
@allure.title('金额筛选')
def test_jesx():
    with allure.step('点击未收款'):
        web.find_element(By.XPATH, "//span[normalize-space()='未收款']").click()
    with allure.step('输入金额最小值'):
        web.find_element('name', 'lls_121').send_keys('1')
    with allure.step('输入金额最大值'):
        web.find_element('name', 'lls_131').send_keys('300')
    web.find_element('name', 'lls_99').click()
    sleep(2)
    web.find_element(By.CLASS_NAME,'el-table__body-wrapper.is-scrolling-middle')
    sleep(5)
