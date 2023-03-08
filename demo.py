# web自动化基本代码
# 1.导入模块
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2.实例化浏览器对象：类名（） 用一个函数接收
driver = webdriver.Chrome()

# 3.打开网页:必须包含协议头（应收汇总路由）
driver.get('http://www.baidu.com')

# 最大化窗口
driver.maximize_window()
sleep(2)

# 输入北京时间
driver.find_element(By.ID, 'kw').send_keys('北京时间')
# 点击百度一下
sleep(2)
driver.find_element(By.ID, 'su').click()
# 延时2秒截图搜索内容
sleep(2)
driver.save_screenshot('搜索内容.png')
# 延时2秒下拉页面
sleep(2)
driver.execute_script("window.scrollTo(0, 250)")  # scroll down
sleep(3)
# 回退
driver.back()
# 前进
driver.forward()
# 获取本页url
a = driver.current_url
print(a)
