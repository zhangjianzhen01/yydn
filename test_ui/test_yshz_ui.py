# web自动化基本代码
# 1.导入模块
from time import sleep

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2.实例化浏览器对象：类名（） 用一个函数接收
driver = webdriver.Chrome()


@allure.title('登录系统')
def test_dl():
    with allure.step('打开网页'):
        driver.get('http://192.168.0.21:9091/#/copsummary')
    with allure.step("最大化窗口"):
         driver.maximize_window()
    with allure.step("清空输入框"):
        driver.find_element('name', 'username').clear()
    with allure.step("输入账号"):
        driver.find_element('name', 'username').send_keys('admin')
    with allure.step("输入密码"):
         driver.find_element('name', 'password').send_keys('huazhou333')
    with allure.step("登录"):
        sleep(2)
        driver.find_element('name', 'login').click()
    # 指定文件夹登录截图
    driver.get_screenshot_as_file(R'D:\python代码仓库\yydn\test_ui\png\登录.png')
    # 延时2秒登录后截图
    sleep(2)
    driver.save_screenshot(R'D:\python代码仓库\yydn\test_ui\png\登录后.png')
    # 点击左侧缩放
    driver.find_element(By.ID, 'hamburger-container').click()


@allure.title('已收款搜索')
def test_ysk():
    # 根据已收款搜索
    driver.find_element('name', 'total_receive_amount_0').send_keys('1')
    sleep(2)
    driver.find_element('name', 'total_receive_amount_1').send_keys('1000')
    sleep(2)
    driver.find_element('name', 'setParams').click()
    # 延时2秒下拉页面
    sleep(2)
    driver.execute_script("window.scrollTo(0, 250)")  # scroll down
    # 搜索后截图
    driver.save_screenshot(R'D:\python代码仓库\yydn\test_ui\png\已收款.png')
    # 延时2秒
    sleep(2)
    # 点击重置
    driver.find_element('name', 'toReset').click()


@allure.title('销售搜索')
def test_xs():
    # 根据销售名字搜索
    driver.find_element('name', 'sales_man').send_keys('罗')
    # 延时2秒点击搜索
    sleep(2)
    driver.find_element('name', 'setParams').click()
    # 延时2秒下拉页面
    sleep(2)
    driver.execute_script("window.scrollTo(0, 250)")  # scroll down
    # 销售搜索后截图
    driver.save_screenshot(R'D:\python代码仓库\yydn\test_ui\png\销售.png')
    sleep(2)
    # 点击重置
    driver.find_element('name', 'toReset').click()


@allure.title('未收款搜索')
def test_wsk():
    # 根据未收款搜索
    driver.find_element('name', 'total_not_receive_amount_0').send_keys('1')
    sleep(2)
    driver.find_element('name', 'total_not_receive_amount_1').send_keys('1000')
    sleep(2)
    driver.find_element('name', 'setParams').click()
    # 延时2秒下拉页面
    sleep(2)
    driver.execute_script("window.scrollTo(0, 250)")  # scroll down
    # 搜索后截图
    driver.save_screenshot(R'D:\python代码仓库\yydn\test_ui\png\未收款.png')
    # 延时2秒
    sleep(2)
    # 点击重置
    driver.find_element('name', 'toReset').click()
    sleep(3)

# 定义执行文件
# if __name__ == '__main__':
#     pytest.main(['-sv', 'test_yshz.py'])
