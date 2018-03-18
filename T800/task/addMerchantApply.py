#coding=utf-8
from selenium import webdriver
import Operation
mobileNumber = '15557138261'
merchantName = u"饿了么"
LegalPersonName = u"王守仁"
LegalPersonNumber = '15557138362'

Operation.OpenBrowser()
Operation.IntoBackground()
Operation.MerchantManagement_apply(mobileNumber,merchantName,LegalPersonName,LegalPersonNumber)
