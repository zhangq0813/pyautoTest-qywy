from poium import Page, PageElement, PageElements


class WsbaoTransInPage(Page):
    '''alert弹框'''
    basePage_alert = PageElement(xpath="/html/body/div[6]/div/span/div", describe="电子对账提示框")
    basePage_sure_button = PageElement(xpath="/html/body/div[6]/div/span/div/div/div/span/span/button[2]",
                                        describe="确定按钮")

    '''菜单按钮'''
    menu_transfer_button = PageElement(xpath="//li[@href='#/Transfer']", describe="转账汇款菜单")
    menu_account_button = PageElement(xpath="//li[@href='#/AccountManage/AccountQry']",describe="账户信息菜单")
    menu_batch_button = PageElement(xpath="//li[@href='#/BatchBusinessManage/RosterManager']", describe="批量业务菜单")
    menu_wsbao_button = PageElement(xpath="//li[@href='#/WSBao']", describe="余利宝菜单")
    menu_bills_button = PageElement(xpath="//li[@href='#/BillsManage/BillsQry']", describe="工单管理菜单")
    menu_membermanager_button = PageElement(xpath="//li[@href='#/MemberManage/CompanyInfo']", describe="会员中心菜单")

    '''#####页面对象#####'''
    '''首页'''
    firstPage_wsbaotransin_link = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.1.2.0.1.0.0']",
                                        describe="余利宝转入")


    '''录入页'''
    secondPage_wsbaotransin_input = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.1.0.0.$/=11.$/=12.$/=11.0']"
                                         , describe="转入金额")
    secondPage_wsbaotransin_output = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.1.0.0.$/=11.$/=13.$/=11.0']", describe="大写金额")
    secondPage_nextn_button = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.1.0.0.$/=12.$/=10']", describe="下一步")


    '''转入确认页面'''
    msurePage_verifycode_button = PageElement(xpath="//input[@data-seed='get_verify_code']", describe="获取验证码")
    msurePage_verifycode_input = PageElement(xpath="//input[@placeholder='请输入验证码']", describe="验证码输入框")
    msurePage_confirm_button = PageElement(xpath="//*[@value='确定']", describe="确定按钮")

    '''结果页'''
    result_msg = PageElement(xpath="//span[@data-reactid='.0.0.0.1.1.0.1.0.1.0.0.1.1.0.0']", describe="成功提示信息")

