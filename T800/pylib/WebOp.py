#coding=utf-8
from selenium import webdriver
from setting import executable_path
import time

import pyodbc
cnxn = pyodbc.connect('driver={Mysql ODBC 5.3 Unicode Driver};server=192.168.10.80;port=3306;database=tourongjia;\
                      uid=root;pwd=tourongjia123!')
cursor = cnxn.cursor()
num = '15921215094'

driver = webdriver.Chrome(executable_path)
driver.implicitly_wait(10)
class   WebOp():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def register(self,num):
    #进入投融家登录入口页面
        driver.get('https://wapescrow.tourongjia.com/#/accountInfo')
        time.sleep(5)
    #点击 登录 注册
        driver.find_element_by_css_selector('body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-tabs > ion-nav-view > ion-view > ion-content > div.scroll > div.userinfo > div.noLogin > div.lor').click()
    #输入手机号码
        driver.find_element_by_css_selector('#MobileNum').send_keys(num)
    #点击 下一步
        driver.find_element_by_css_selector('body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div > div > button').click()
        time.sleep(9)
    #点击 免费获取，获取验证码
        driver.find_element_by_css_selector('body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div:nth-child(3) > div.yz_r > a').click()
    #获取验证码
    def database(self,num):
        cursor.execute("SELECT code FROM fi_mobile_validate_code WHERE mobile =? order by ctime DESC", num)
        ret = cursor.fetchone()
        print ret
        code = ret[0]
#     #输入验证码

        driver.find_element_by_css_selector('body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div:nth-child(3) > div.yz_l > input').send_keys(code)
#     #输入密码
#         driver.find_element_by_css_selector('body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div:nth-child(4) > span > input').send_keys('m123456')
#     #点击注册
#         driver.find_element_by_css_selector('body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div.trj-btn-box > button').click()
#
#     #点击 账户
#         driver.find_element_by_css_selector('body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-tabs > div > a:nth-child(8)').click()
#         time.sleep(3)
#     #点击商户入驻
#         driver.find_element_by_css_selector('body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-tabs > ion-nav-view > ion-view > ion-content > div.scroll > div.shopsWeal > ul > li:nth-child(3)').click()
# # register()