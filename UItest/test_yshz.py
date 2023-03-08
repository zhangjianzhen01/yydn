# web自动化基本代码
# 1.导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2.实例化浏览器对象：类名（） 用一个函数接收
drive = webdriver.Chrome()

# 3.打开网页:必须包含协议头（应收汇总路由）
drive.get('http://192.168.0.217:9900/?#/copsummary')

# 最大化窗口
drive.maximize_window()

# 清除账号输入框
drive.find_element('name', 'username').clear()
# 输入账号
drive.find_element('name', 'username').send_keys('caiwu')
# 输入密码
drive.find_element('name', 'password').send_keys('123456')
# 延时2秒后点击登录
sleep(2)
drive.find_element('name', 'login').click()
# 指定文件夹登录截图
drive.save_screenshot(R'D:\python代码仓库\yydn\UItest\screenshot\登录.png')
# 延时2秒，登录后截图
sleep(2)
drive.save_screenshot(R'D:\python代码仓库\yydn\UItest\screenshot\登录后.png')
# 点击左侧缩放
drive.find_element(By.ID, 'hamburger-container').click()

# 根据已收款搜索
drive.find_element('name', 'total_receive_amount_0').send_keys('1')
sleep(2)
drive.find_element('name', 'total_receive_amount_1').send_keys('1000')
sleep(2)
drive.find_element('name', 'setParams').click()
# 延时2秒下拉页面
sleep(2)
drive.execute_script("window.scrollTo(0, 250)")  # scroll down
# 搜索后截图
drive.save_screenshot(R'D:\python代码仓库\yydn\UItest\screenshot\已收款.png')
# 延时2秒
sleep(2)
# 点击重置
drive.find_element('name','toReset').click()
drive.find_element('name', 'sales_man').send_keys('罗')
sleep(2)
drive.find_element('name', 'setParams').click()
sleep(2)
drive.execute_script("window.scrollTo(0, 250)")  # scroll down
# 销售搜索后截图
drive.save_screenshot(R'D:\python代码仓库\yydn\UItest\screenshot\销售.png')
sleep(2)
