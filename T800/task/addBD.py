#coding=utf-8
from selenium import  webdriver
import Operation
MobileNumeber = '15921015491'
Name = u"刘基"
IdentityNumber = '432922198008015828'
bankCard = '6226220615841342'
# MobileNumeber,Name,IdentityNumber,bankCard
Operation.OpenBrowser()
Operation.IntoBackground()
Operation.BdManaage(MobileNumeber,Name,IdentityNumber,bankCard)