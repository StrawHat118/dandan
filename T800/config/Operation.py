#coding=utf-8
import time

from selenium import webdriver

from pylib.setting import executable_path

#增加chrome的配置项
# driverOption = webdriver.ChromeOptions()
# driverOption.add_argument(r"user-data-dir=C:\Users\ThinkPad\AppData\Local\Google\Chrome\User Data\Profile 3")
# driver = webdriver.Chrome(executable_path,0,chrome_options=driverOption)
driver = webdriver.Chrome(executable_path)
driver.implicitly_wait(10)

#打开浏览器
def OpenBrowser():
    driver.get('http://testadmin.golexiao.com')
#进入后台
def IntoBackground():
    driver.find_element_by_id('userNo').send_keys('15921705491')
    driver.find_element_by_id('pwd').send_keys('lx888888')
    driver.find_element_by_id('login_btn').click()
#进入BD管理
#进入商户管理
def MerchantManagement_apply(mobileNumber,merchantName,LegalPersonName,LegalPersonNumber):
    #点击商户管理
    driver.find_element_by_css_selector('#menuGroup > div:nth-child(2) > div.panel-header.accordion-header > div.panel-tool > div').click()
    #点击商户入驻申请
    driver.find_element_by_css_selector('#menu135 > li:nth-child(3) > div > span.tree-title').click()
    #进入frame
    driver.switch_to.frame('work_frame')
    time.sleep(2)
    #点击新增商户
    driver.find_element_by_css_selector('body > div.func_tool_area > a').click()
    #添加客户手机号码
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2) > input').send_keys(mobileNumber)
    #添加商户名
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2) > input').send_keys(merchantName)
    #添加门店电话
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2) > input').send_keys(10101010)
    #填写商户地址--点击下拉框
    driver.find_element_by_css_selector('#province_list_combobox > span > span').click()
    #选中浙江省
    driver.find_element_by_css_selector('body > div.panel.xcombobox-panel > div > div:nth-child(12)').click()
    #点击下拉框
    driver.find_element_by_css_selector('#city_list_combobox > span > span').click()
    #选中杭州市
    driver.find_element_by_css_selector('body > div:nth-child(16) > div > div:nth-child(2)').click()
    #点击下拉框
    driver.find_element_by_css_selector('#district_list_combobox > span > span').click()
    #选中拱墅区
    driver.find_element_by_css_selector('body > div:nth-child(17) > div > div:nth-child(5)').click()
    #填写详细地址
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(5) > td:nth-child(2) > input').send_keys(u"大关路100号")
    #点击分类下拉框
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(6) > td:nth-child(2) > span > span > span').click()
    #选中美食
    driver.find_element_by_css_selector('body > div:nth-child(18) > div > div:nth-child(4)').click()
    #填写员工人数
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(7) > td:nth-child(2) > input').send_keys(100)
    #填写商户面积
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(8) > td:nth-child(2) > input').send_keys(100)
    #填写商户介绍
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(9) > td:nth-child(2) > textarea').send_keys(u"ALL IN AI")
    #填写法人姓名
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(10) > td:nth-child(2) > input').send_keys(LegalPersonName)
    #填写法人手机
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(11) > td:nth-child(2) > input').send_keys(LegalPersonNumber)
    #填写营业执照编号
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(12) > td:nth-child(2) > input').send_keys(u"YYZZ10101010")
    #填写持卡人姓名
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(13) > td:nth-child(2) > input').send_keys(LegalPersonName)
    #填写银行卡号
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(1) > tbody > tr:nth-child(14) > td:nth-child(2) > input').send_keys('6228483178200785674')
    #选中省份列表
    driver.find_element_by_css_selector('#bank_province_list_combobox > span > span').click()
    #选中浙江省
    driver.find_element_by_css_selector('body > div:nth-child(19) > div > div:nth-child(12)').click()
    #选中城市列表
    driver.find_element_by_css_selector('#bank_city_list_combobox > span > span').click()
    #选中杭州市
    driver.find_element_by_css_selector('body > div:nth-child(20) > div > div:nth-child(2)').click()
    #bug弹窗
    driver.find_element_by_css_selector('body > div:nth-child(21) > div.messager-body.panel-body.panel-body-noborder.window-body > div.messager-button > a').click()
    #输入银行列表
    driver.find_element_by_css_selector('#bank_list_combobox > span > span').click()
    #选中中国民生银行
    driver.find_element_by_css_selector('body > div:nth-child(21) > div > div:nth-child(5)').click()
    #选中支行列表
    driver.find_element_by_css_selector('#sub_bank_list_combobox > span > span').click()
    #选中城西支行
    driver.find_element_by_css_selector('body > div:nth-child(22) > div > div:nth-child(3)').click()
    #填写邀请注册奖励
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(5) > tbody > tr:nth-child(2) > td:nth-child(2) > input').send_keys('10')
    #填写邀请首投奖励
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(5) > tbody > tr:nth-child(4) > td:nth-child(2) > input').send_keys('0')
    #填写福利券结算比例
    driver.find_element_by_css_selector('#merchant_add_form > table:nth-child(5) > tbody > tr:nth-child(6) > td:nth-child(2) > input').send_keys('0')

def BdManaage(MobileNumeber,Name,IdentityNumber,bankCard):
    #点击BD管理
    driver.find_element_by_css_selector('#menuGroup > div:nth-child(1) > div.panel-header.accordion-header > div.panel-tool > div').click()
    #点击BD人员管理
    driver.find_element_by_css_selector('#menu134 > li:nth-child(1) > div > span.tree-title').click()
    #进入frame
    driver.switch_to.frame('work_frame')
    time.sleep(2)
    #点击新增
    driver.find_element_by_css_selector('body > div.func_tool_area > a:nth-child(1) > span > span').click()
    #输入手机号
    driver.find_element_by_css_selector('#bd_add_form > table:nth-child(3) > tbody > tr:nth-child(1) > td:nth-child(2) > input').send_keys(MobileNumeber)
    #输入姓名
    driver.find_element_by_css_selector('#bd_add_form > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2) > input').send_keys(Name)
    #输入身份证号码
    driver.find_element_by_css_selector('#bd_add_form > table:nth-child(3) > tbody > tr:nth-child(3) > td:nth-child(2) > input').send_keys(IdentityNumber)
    #输入银行卡号
    driver.find_element_by_css_selector('#bd_add_form > table:nth-child(3) > tbody > tr:nth-child(4) > td:nth-child(2) > input').send_keys(bankCard)
    #点击开户行省份--省列表
    driver.find_element_by_css_selector('#add_bank_province_list_combobox > span > span').click()
    #选中浙江省
    driver.find_element_by_css_selector('body > div.panel.xcombobox-panel > div > div:nth-child(11)').click()
    #点击开户行--市列表
    driver.find_element_by_css_selector('#add_bank_city_list_combobox > span > span').click()
    #选中杭州市
    # driver.find_element_by_css_selector('body > div:nth-child(18) > div > div.combobox-item.combobox-item-selected').click()
    #点击银行列表
    driver.find_element_by_css_selector('#add_bank_list_combobox > span > span').click()
    #选中民生银行
    driver.find_element_by_css_selector('body > div:nth-child(17) > div > div:nth-child(4)').click()
    #点击支行列表
    driver.find_element_by_css_selector('#add_sub_bank_list_combobox > span > span').click()
    #选中城西支行
    driver.find_element_by_css_selector('body > div:nth-child(18) > div > div:nth-child(2)').click()
    #点击负责区域列表-省
    driver.find_element_by_css_selector('#add_province_list_combobox > span > span').click()
    #选中浙江省
    driver.find_element_by_css_selector('body > div:nth-child(19) > div > div:nth-child(12)').click()
    #点击负责区域列表-市
    driver.find_element_by_css_selector('#add_city_list_combobox > span > span').click()
    #选中杭州市
    driver.find_element_by_css_selector('body > div:nth-child(20) > div > div:nth-child(2)').click()
    #点击负责区域列表-区
    driver.find_element_by_css_selector('#add_district_list_combobox > span > span').click()
    #选中拱墅区
    driver.find_element_by_css_selector('body > div:nth-child(21) > div > div:nth-child(5)').click()
    #点击添加区域
    driver.find_element_by_css_selector('#bd_add_form > table:nth-child(3) > tbody > tr:nth-child(7) > td:nth-child(2) > a:nth-child(4) > span > span').click()
    #点击提交审核
    driver.find_element_by_css_selector('#save > span > span').click()

    #选中拱墅区

#进入福利券管理
#进入宣传管理
#进入合作平台管理
#进入用户管理
#进入配置管理
#进入财务管理