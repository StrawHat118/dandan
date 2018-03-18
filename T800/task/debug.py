#coding=utf-8
from selenium import webdriver
from setting import executable_path

driver = webdriver.Chrome(executable_path)
driver.get('http://blog.csdn.net/maybe_frank/article/details/79374866')
#滑动测试

while True:
    js ="var q=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    js = "var q=document.documentElement.scrollTop=0"
    driver.execute_script(js)