*** Settings ***
Library     pylib.WebOp
Library     Selenium2Library
Library     Dialogs
*** Test Cases ***
测试
    [Documentation]   测试一下
    #设置隐式等待时间
    set selenium implicit wait      10
    #访问网址
    open browser        https://wapescrow.tourongjia.com/#/login///      chrome
    #点击登录注册
#    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-tabs > ion-nav-view > ion-view > ion-content > div.scroll > div.userinfo > div.noLogin > div.lor
#输入注册的手机号码
    input text          css=#MobileNum
    ...                 15921215097
    #点击下一步
    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div > div > button
    execute manual step     是否已经输入验证码
    #点击免费获取
    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div:nth-child(3) > div.yz_r > a
    #休息一下
    execute manual step     是否继续
    database            15921215095
    #输入密码
    input text          css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div:nth-child(4) > span > input
    ...                 m123456


