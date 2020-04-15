from poium import Page, PageElement, PageElements


class ReconciliationPage(Page):
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
    firstPage_reconciliation_link = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.0.$2.0.0']",
                                        describe="电子对账")

    '''对账页'''
    secondPage_reconciliation_select = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.0.0.0.1.1.$selection.0']",
                                             describe="对账类型")
    secondPage_startDate_button = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.0.0.1.0.1.0.$=10']",
                                              describe="起始时间")
    secondPage_startDate_table_button = PageElement(xpath="/html/body/div[7]/div/div/div[2]/table/tbody/tr[1]/td[5]/span",
                                                     describe="2016-1-1")
    secondPage_endDate_button = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.0.0.1.0.3.0.$=10']",
                                              describe="结束时间")
    secondPage_endDate_table_button = PageElement(xpath="/html/body/div[8]/div/div/div[2]/table/tbody/tr[2]/td[4]/span",
                                                     describe="2016-2-7")
    secondPage_query_button = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.0.0.1.1.0']", describe="查询")

    '''同属性元素list'''
    list_dolinks = PageElements(class_name="dft margL20 cyan", describe="操作按钮")

    '''结果页面'''
    resultPage_msg = PageElement(xpath="//*[@data-reactid='.0.0.0.1.0.0.0.0.0']", describe="反显信息")




