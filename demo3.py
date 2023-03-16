# coding=gbk
# web�Զ�����������
# 1.����ģ��


import allure, pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os

# 2.ʵ��������������������� ��һ����������
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome(options=option)


@allure.feature('Ӧ������-UI')
@allure.story('��¼')
@allure.title('��¼ϵͳ')
def test_dl():
    with allure.step('����ҳ'):
        web.get('http://192.168.0.109:9628/#/nuclearprice/baojia')
    with allure.step("��󻯴���"):
        web.maximize_window()
    with allure.step("��������"):
        web.find_element('name', 'username').clear()
    with allure.step("�����˺�"):
        web.find_element('name', 'username').send_keys('admin')
    with allure.step("��������"):
        web.find_element('name', 'password').send_keys('huazhou333')
    with allure.step("��¼"):
        sleep(2)
        web.find_element('name', 'login').click()
        allure.attach(web.get_screenshot_as_png(), '��¼ǰ��ͼ', allure.attachment_type.PNG)
        sleep(2)
        allure.attach(web.get_screenshot_as_png(), '��¼���ͼ', allure.attachment_type.PNG)
    with allure.step("������������"):
        web.find_element(By.ID, 'hamburger-container').click()
        sleep(3)


def test_bjd():
    web.execute_script("window.scrollTo(0, 230)")
    sleep(2)
    with allure.step('����½�����'):
        sleep(2)
        web.find_element(By.XPATH, "//span[normalize-space()='�½�����']").click()
        sleep(2)
    with allure.step('���뱨�۵�����'):
        web.find_element('name','wjm_1').send_keys('����Ĳ���')
        sleep(2)
    with allure.step('ѡ��ͻ�'):
        web.find_element('name','toSearch').click()
        sleep(2)
    with allure.step('���ѡ��'):
        web.find_elements(By.LINK_TEXT, "ѡ��")[2].click()
        sleep(2)



# def test_xsd():
#     web.execute_script("window.scrollTo(0, 230)")
#     sleep(2)
#     with allure.step('������۶���'):
#         web.find_element(By.XPATH, "//span[normalize-space()='XD23030036']").click()
#         sleep(2)
#     with allure.step('��������ƻ�'):
#         web.find_element(By.ID, 'tab-logistics').click()
#         sleep(2)
#     with allure.step('�½��ƻ�'):
#         web.find_element(By.XPATH, "//span[normalize-space()='�½��ƻ�']").click()
#     with allure.step('�����ַ�б�'):
#         web.find_element(By.XPATH, "//span[normalize-space()='��ַ�б�']").click()
#         sleep(4)
#     with allure.step('���ѡ��'):
#         web.find_element(By.XPATH, "//span[normalize-space()='ѡ ��']").click()
#     sleep(5)
