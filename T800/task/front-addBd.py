#coding=utf-8
from selenium import webdriver
from setting import executable_path
import time

driver = webdriver.Chrome(executable_path)
driver.implicitly_wait(10)
num = '15921015491'
def addBD():
    driver.get('https://wapescrow.tourongjia.com/#/login///')
    #登录栏输入手机号码
    driver.find_element_by_css_selector('#MobileNum').send_keys(num)
    #点击下一步
    driver.find_element_by_css_selector('body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div > div > button').click()
    #输入密码
    driver.find_element_by_css_selector('#PwdNum').send_keys('m123456')
    #点击 登录
    driver.find_element_by_css_selector('body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div > div > button').click()
addBD()
