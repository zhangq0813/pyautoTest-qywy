from poium import Page, PageElement, PageElements


class WsbaoAutoPage(Page):
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

    '''余利宝链接'''
    firstPage_wsbaoAuto_link = PageElement(xpath="//*[@href='#/WSBao/ChangeIntoOut/collection']", describe="余利宝菜单链接")

    '''设置页'''
    secondPage_padding_button = PageElement(xpath="//*[@class='padding-b0 ant-radio']", describe="超过单选框按钮")
    secondPage_padding_input = PageElement(xpath="//*[@name='amountTwo']", describe="超过金额输入框")
    secondPage_submit_input = PageElement(xpath="//input[@value='保存设置']", describe="保存设置")

    '''验证码校验页面'''
    msurePage_verifycode_button = PageElement(xpath="//input[@data-seed='get_verify_code']", describe="获取验证码")
    msurePage_verifycode_input = PageElement(xpath="//input[@placeholder='请输入验证码']", describe="验证码输入框")
    msurePage_confirm_button = PageElement(xpath="//*[@value='确 定']", describe="确定按钮")

    '''结果页'''
    result_msg = PageElement(xpath="//*[@id='sucessDlg']/div[2]/div[2]/div", describe="成功提示信息")

