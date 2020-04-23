from poium import Page, PageElement, PageElements


class MobileModifyPage(Page):
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

    '''首页'''
    firstPage_personalmessage_link = PageElement(xpath="//*[@href='#/MemberManage/AdministratorInfo']", describe="个人信息链接")
    firstPage_mobilemodify_button = PageElement(xpath="//*[@id='main_content']/div[2]/div/div/div/div/div[2]/input", describe="个人信息修改")

    '''设置页'''
    secondPage_mobilemodify_input = PageElement(xpath="//*[@id='mobilePhone']", describe="变更手机号码")
    secondPage_save_button = PageElement(xpath="//*[@id='main_content']/div[2]/div/div/div[2]/input", describe="保存手机号码")

    '''确认页'''
    thirdPage_msuremobile_input = PageElement(
        xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.0.0.1.0.1.2.1']",
                                                                          describe="回显手机号")
    thirdPage_msure_button = PageElement(xpath="//input[@value='确定']", describe="确定")

    '''结果页'''
    result_msg = PageElement(xpath="//*[@id='content']/div[2]/span/div/span[1]", describe="成功提示信息")

