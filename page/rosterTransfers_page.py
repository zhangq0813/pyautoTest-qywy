from poium import Page, PageElement, PageElements
import datetime


class RosterTransfersPage(Page):
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

    '''批量代发-名册代发'''
    firstPage_fileTransfers_button = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.0.$1.0.0']",describe="批量代发")
    firstPage_rosterTransfers_button = PageElement(xpath="//*[@data-page='roster_salary']",describe="名册代发")

    '''名册代发'''

    firstPage_rosterTransfers_labels = PageElements(xpath="//label/span[2]", describe="单选框list")
    firstPage_fileSummary_input = PageElement(xpath="//*[@name='fileSummary']", describe="摘要")
    firstPage_rosters_labels = PageElements(xpath="//div[@class='book-item']", describe="代发名册list")
    firstPage_next_button = PageElement(xpath="//*[@value='下一步']", describe="下一步")

    '''代发录入确认页面'''
    secondPage_verifycode_button = PageElement(xpath="//input[@data-seed='get_verify_code']", describe="获取验证码")
    secondPage_verifycode_input = PageElement(xpath="//input[@placeholder='请输入验证码']", describe="验证码输入框")
    secondPage_next_button = PageElement(xpath="//*[@value='下一步']", describe="下一步")

    '''结果页'''
    result_msg = PageElement(xpath="//*[@id='main_content']/div[2]/div/span/div[2]/div[3]/div[2]/span[2]", describe="交易笔数")
    result_sure_button = PageElement(xpath="//*[@value='返回']", describe="返回按钮")

