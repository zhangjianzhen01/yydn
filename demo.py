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


@allure.title('根据合同金额搜索')
def test_htje():
    with allure.step('输入最小值'):
        web.find_element('name', 'total_sales_amount_0').send_keys('1')
    with allure.step('输入最大值'):
        web.find_element('name', 'total_sales_amount_1').send_keys('300')
        sleep(2)
    with allure.step('点击搜索'):
        web.find_element('name', 'setParams').click()
    sleep(2)
    web.execute_script("window.scrollTo(0, 250)")  # scroll down
    allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    sleep(1)
    web.find_element('name', 'toReset').click()
    sleep(2)


@allure.title('根据已收款金额搜索')
def test_sk():
    with allure.step('输入最小值'):
        web.find_element('name', 'total_receive_amount_0').send_keys('1')
    with allure.step('输入最大值'):
        web.find_element('name', 'total_receive_amount_1').send_keys('300')
        sleep(2)
    with allure.step('点击搜索'):
        web.find_element('name', 'setParams').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    sleep(1)
    web.find_element('name', 'toReset').click()
    sleep(2)


@allure.title('根据未收款金额搜索')
def test_wsk():
    with allure.step('输入最小值'):
        web.find_element('name', 'total_not_receive_amount_0').send_keys('1')
    with allure.step('输入最大值'):
        web.find_element('name', 'total_not_receive_amount_1').send_keys('300')
        sleep(2)
    with allure.step('点击搜索'):
        web.find_element('name', 'setParams').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    sleep(1)
    web.find_element('name', 'toReset').click()
    sleep(2)


@allure.title('根据总可用预收款搜索')
def test_zkyysk():
    with allure.step('输入最小值'):
        web.find_element('name', 'total_pre_amount_0').send_keys('1')
    with allure.step('输入最大值'):
        web.find_element('name', 'total_pre_amount_1').send_keys('300')
        sleep(2)
    with allure.step('点击搜索'):
        web.find_element('name', 'setParams').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    sleep(1)
    web.find_element('name', 'toReset').click()
    sleep(2)


@allure.title('根据已开票金额搜索')
def test_ykp():
    with allure.step('输入最小值'):
        web.find_element('name', 'total_invoice_amount_0').send_keys('1')
    with allure.step('输入最大值'):
        web.find_element('name', 'total_invoice_amount_1').send_keys('300')
        sleep(2)
    with allure.step('点击搜索'):
        web.find_element('name', 'setParams').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    sleep(1)
    web.find_element('name', 'toReset').click()
    sleep(2)


@allure.title('根据未开票金额搜索')
def test_wkp():
    with allure.step('输入最小值'):
        web.find_element('name', 'total_not_invoice_amount_0').send_keys('1')
    with allure.step('输入最大值'):
        web.find_element('name', 'total_not_invoice_amount_1').send_keys('300')
        sleep(2)
    with allure.step('点击搜索'):
        web.find_element('name', 'setParams').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    sleep(1)
    web.find_element('name', 'toReset').click()
    sleep(2)


@allure.title('根据本月已收款搜索')
def test_byysk():
    with allure.step('输入最小值'):
        web.find_element('name', 'total_receive_amount_month_0').send_keys('1')
    with allure.step('输入最大值'):
        web.find_element('name', 'total_receive_amount_month_1').send_keys('300')
        sleep(2)
    with allure.step('点击搜索'):
        web.find_element('name', 'setParams').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    sleep(1)
    web.find_element('name', 'toReset').click()
    sleep(2)


@allure.title('根据逾期未收款搜索')
def test_yqwsk():
    with allure.step('输入最小值'):
        web.find_element('name', 'total_not_receive_amount_overdue_0').send_keys('1')
    with allure.step('输入最大值'):
        web.find_element('name', 'total_not_receive_amount_overdue_1').send_keys('300')
        sleep(2)
    with allure.step('点击搜索'):
        web.find_element('name', 'setParams').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    sleep(1)
    web.find_element('name', 'toReset').click()
    sleep(2)


@allure.title('根据开票已收款搜索')
def test_kpysk():
    with allure.step('输入最小值'):
        web.find_element('name', 'invoice_receive_amount_0').send_keys('1')
    with allure.step('输入最大值'):
        web.find_element('name', 'invoice_receive_amount_1').send_keys('300')
        sleep(2)
    with allure.step('点击搜索'):
        web.find_element('name', 'setParams').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    sleep(1)
    web.find_element('name', 'toReset').click()
    sleep(2)


@allure.title('根据开票未收款搜索')
def test_kpwsk():
    with allure.step('输入最小值'):
        web.find_element('name', 'invoice_not_receive_amount_0').send_keys('1')
    with allure.step('输入最大值'):
        web.find_element('name', 'invoice_not_receive_amount_1').send_keys('300')
        sleep(2)
    with allure.step('点击搜索'):
        web.find_element('name', 'setParams').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '搜索结果', allure.attachment_type.PNG)
    sleep(1)
    web.find_element('name', 'toReset').click()
    sleep(2)


# @allure.title('批量开票')
# def test_plkp():
#     with allure.step('批量开票'):
#         web.find_element('name', 'invoiceClick').click()
#     with allure.step('点击开票公司'):
#         web.find_element('name', 'invoice_company').click()
#         sleep(3)
#     with allure.step('选择开票公司'):
#         web.find_element('name', 'invoice_company_0').click()
#     sleep(5)


@allure.title('退款')
def test_tk():
    with allure.step('输入订单号'):
        web.find_element('name', 'business_no').send_keys('XD22090149')
        sleep(2)
    with allure.step('下拉页面'):
        web.execute_script("window.scrollTo(0, 250)")
    with allure.step('回车'):
        web.find_element('name', 'business_no').send_keys(Keys.ENTER)
    with allure.step('点击订单号'):
        sleep(2)
        web.find_element('name', 'business_no_0').click()
    with allure.step('点击退款信息'):
        sleep(2)
        web.find_element(By.ID, 'tab-fifth').click()
    sleep(2)
    allure.attach(web.get_screenshot_as_png(), '退款信息页面', allure.attachment_type.PNG)
    sleep(2)
    with allure.step('点击新增'):
        web.find_element('name', 'toAdd').click()
        sleep(2)
    with allure.step('选择退款方式'):
        web.find_element('name', 'refund_mode').click()
        sleep(3)
    with allure.step('选择华胄建设银行'):
        web.find_element('name', 'refund_mode_3').click()
        sleep(3)
    with allure.step('选择退款日期'):
        web.find_element('name', 'refund_time').click()
        sleep(3)
    web.find_element(By.XPATH, "//span[normalize-space()='9']").click()
    sleep(2)
    with allure.step("清空输入框"):
        web.find_element('name', 'refund_amount').clear()
    with allure.step('输入退款金额'):
        web.find_element('name', 'refund_amount').send_keys('188')
        sleep(2)
    with allure.step('点击保存'):
        web.find_element('name', 'sureDialog').click()
    sleep(3)
    allure.attach(web.get_screenshot_as_png(), '截图退款', allure.attachment_type.PNG)
    sleep(2)



