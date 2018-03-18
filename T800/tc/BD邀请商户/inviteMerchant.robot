*** Settings ***
Library    Selenium2Library
Library   Dialogs
#Library   config/cfg
*** Test Cases ***
邀请商户
    [Documentation]     注册手机号并开户
    set selenium implicit wait      10
    open browser        https://wapescrow.tourongjia.com/#/login///         chrome
#输入手机号码---BD注册号码
    input text          css=#MobileNum          18367150812
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
    #点击商户管理
    click element       css=#react-placeholder > div > div > div > div.screen-content.mybusiness > div.mybusiness-menu > dl:nth-child(1)
#    click element       css=#react-placeholder > div > div > div > div.screen-content.mybusiness > div.mybusiness-menu.menu-three > dl:nth-child(1) > dd > img
    #点击添加商户
    click element       css=#react-placeholder > div > div > div:nth-child(2) > div.screen-content.sub-merchant > div.fixed-bottom
#输入商户名
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(2) > div.-value > input[type="text"]
    ...                 辽南铁骑
    #输入商户电话
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(3) > div.-value > input[type="text"]
    ...                 010-12345678
    #输入logo和商户地址
    execute manual step     请输入商户logo和商户地址
    #输入商户地址
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(5) > div > input[type="text"]
    ...                 龙翔桥地铁站B出口
    #所属分类
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(6) > div.-value > input[type="text"]
    #选择 美食
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-container > div > div.picker-column > div > div:nth-child(2)
    #选择 确定
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div:nth-child(3) > div > div > div.picker-header > a.sure
    #输入商户面积
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(7) > div.-value > input[type="number"]
    ...                 1024
    #输入员工人数
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(8) > div.-value > input[type="tel"]
    ...                 2048
    #添加商户宣传图片
    execute manual step     请添加商户宣传图片
    #输入商户介绍
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(1) > div:nth-child(10) > div.-textarea > textarea
    ...                 这是一个商户
#输入商户手机号---商户注册号码
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(1) > div.-value > input[type="tel"]
    ...                 18367150082
#输入法人姓名
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(2) > div.-value > input[type="text"]
    ...                 李成桂
#输入法人手机
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(3) > div.-value > input[type="tel"]
    ...                 18367150052
    #添加法人身份证
    execute manual step      请添加法人身份证照片
#输入持卡人姓名
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(5) > div.-value > input[type="text"]
    ...                 商汤
#输入银行卡号
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(6) > div.-value > input[type="tel"]
    ...                 6228483178500897857
    sleep               1
    #点击开户行
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(7) > div.-value
    #点击 浙江省
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(11)
    #点击浙江省杭州市
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(1)
    #点击 中国民生银行
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(12)
    #点击 天目山支行
    click element       css=#react-placeholder > div > div > div:nth-child(4) > div.screen-content.classification > ul > li:nth-child(1)
    #上传营业执照图片
    execute manual step     请上传营业执照图片
    #输入营业执照编号
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(2) > div:nth-child(8) > div.-value > input[type="text"]
    ...                 123456789012345678
    #输入邀请注册奖励
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(3) > div.add-line > div > div:nth-child(2) > div.-value > input[type="number"]
    ...                 12
    #输入首投奖励
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(3) > div:nth-child(2) > div > div:nth-child(2) > div.-value > input[type="number"]
    ...                 23
    #输入 福利券结算比例
    input text          css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.tab-panel > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(2) > div.-value > input[type="number"]
    ...                 34
    #稍微休息
    execute manual step  是否继续
    #点击 提交审核
    click element       css=#react-placeholder > div > div > div:nth-child(3) > div.screen-content.-m-add > div.add-btn > a.add-btn-fr