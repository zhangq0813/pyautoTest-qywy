from poium import Page, PageElement, PageElements


class ReceiptPage(Page):
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
    firstPage_receipt_link = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.0.$3.0.0']",
                                        describe="电子回单")
    '''回单table页'''
    resultPage_receipt_indexs = PageElements(xpath="//*[@class='tableWord']", describe="回单编号列表")

    '''交易明细table页'''
    resultPage_detail_button = PageElement(xpath="//li[@data-reactid='.0.0.0.1.1.0.1.0.0.0.0.$1']",
                                           describe="交易明细table")
    resultPage_detail_indexs = PageElements(xpath="//*[@class='tableWord']", describe="明细编号列表")

    '''历史明细table页'''
    resultPage_history_button = PageElement(xpath="//li[@data-reactid='.0.0.0.1.1.0.1.0.0.0.0.$2']",
                                           describe="交易明细table")
    resultPage_history_indexs = PageElements(xpath="//*[@class='tableWord']", describe="历史编号列表")


