from poium import Page, PageElement, PageElements


class BillCheckPage(Page):
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
    firstPage_billcheck_link = PageElement(xpath="//*[@href='#/BillsManage/BillsCheck']", describe="工单审批菜单")

    '''查询页'''
    firstPage_check_list = PageElements(xpath="//*[@class='ant-checkbox']", describe="审批列表")
    firstPage_billcheck_button = PageElement(xpath="//*[@data-seed='batch-workbulls-check']", describe="批量审批")

    '''查询结果页'''
    secondPage_reject_index = PageElement(xpath="//*[@value='REJECT']", describe="全部拒绝单选框")
    secondPage_rejecttxt_index = PageElement(xpath="//*[@placeholder='请输入拒绝原因']", describe="拒绝原因")

    '''验证码验证页面'''
    secondPage_verifycode_button = PageElement(xpath="//input[@data-seed='get_verify_code']", describe="获取验证码")
    secondPage_verifycode_input = PageElement(xpath="//input[@placeholder='请输入验证码']", describe="验证码输入框")
    secondPage_next_button = PageElement(xpath="//*[@value='确定']", describe="确定")

    '''结果页面'''
    thirdPage_result_msg = PageElement(xpath="//*[@id='content']/div[2]/span/div",describe="反显信息")