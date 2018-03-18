*** Settings ***
Library    Selenium2Library
Library   Dialogs
#Library   config/cfg
*** Test Cases ***
添加子BD
    [Documentation]     注册手机号并开户
    set selenium implicit wait      10
    open browser        https://wapescrow.tourongjia.com/#/login///         chrome
#输入手机号码---父BD的账号
    input text          css=#MobileNum          18367150822
    #点击下一步
    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div > div > button
    #输入密码
    input text          css=#PwdNum             m123456
    #点击登录
    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-content > div.scroll > form > div > div > button
    #点击账户
    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-tabs > div > a:nth-child(8)
    #休息一下
    execute manual step         是否继续执行
    #点击商户入驻
    click element       css=body > ion-nav-view > ion-side-menus > ion-side-menu-content > ion-nav-view > ion-view > ion-tabs > ion-nav-view > ion-view > ion-content > div.scroll > div.shopsWeal > ul > li:nth-child(3)
    #点击授权确认
#    click element       css=#react-placeholder > div > div:nth-child(2) > div > div > a.accredit_btn
    #点击BD团队管理
    click element       css=#react-placeholder > div > div > div > div.screen-content.mybusiness > div.mybusiness-menu > dl:nth-child(2)
    #点击添加子BD
    click element       css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.sub-merchant > div.fixed-bottom > a
#输入子BD的手机号
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div:nth-child(1) > span > input[type="tel"]
    ...                 18367151322
#输入子BD的姓名
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div:nth-child(2) > span > input[type="text"]
    ...                 驼祥子
    #输入身份证号码
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div:nth-child(3) > span > input[type="text"]
    ...                 450326198912241844

    #输入银行卡号
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div >div:nth-child(4) > span > input[type="tel"]
    ...                 6228483178200785674
    #选择开户行
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div:nth-child(5) > span
    #选择浙江省
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(11)
    #选择杭州市
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(1)
    #选择中国民生银行
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(12)
    #选择天目山支行
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(1)
    # 选择 添加商户
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.permission > div.content > ul > li:nth-child(1)
    #选择审核商户
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.permission > div.content > ul > li:nth-child(2)
    #选择提现
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.permission > div.content > ul > li:nth-child(3)
    #选择 发布商户福利
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.permission > div.content > ul > li:nth-child(4)
    #选择审核商户福利
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.permission > div.content > ul > li:nth-child(5)
    #添加区域
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.cell-item-add > div.cell-line > div > span > input[type="text"]
    execute manual step     是否继续
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.sub-business-warp > div > div.cell-control > button