from poium import Page, PageElement, PageElements


class DetailQueryPage(Page):
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
    firstPage_detailquery_link = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.0.$1.0.0']",
                                        describe="交易明细查询")


    '''查询页'''
    secondPage_trsType_index = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.0.1.$0.0.0.0.0.$/=15.$/=11.$selection.0']",
                                        describe="交易类型")
    secondPage_trsType_indexs = PageElements(xpath="//li[@role='menuitem']", describe="交易类型列表")

    secondPage_startDate_button = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.0.1.$0.0.0.0.0.$/=12.0.$=10']",
                                        describe="起始时间")
    #secondPage_startDate_table_button = PageElement(xpath="//table/tbody/tr[2]/td[4]/span",
    #                                    describe="2016-1-7")
    #secondPage_startDate_table_buttons = PageElements(xpath="//*[@class='ant-calendar-date' and @text()='7']",
    #                                                describe="2016-1-7")
    secondPage_startDate_table_buttons = PageElements(xpath="//td[@class='ant-calendar-cell']",
                                                      describe="2016-1-7")

    secondPage_endDate_button = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.0.1.$0.0.0.0.0.$/=14.0.$=10']",
                                        describe="结束时间")
    secondPage_endDate_table_buttons = PageElements(xpath="//td[@class='ant-calendar-cell']",
                                                      describe="2016-1-9")
    secondPage_query_button = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.0.1.$0.0.0.0.0.$/=17.$/=10']",
                                        describe="查询")

    '''同属性元素list'''
    # list_dolinks = PageElements(class_name="dft margL20 cyan", describe="操作按钮")
    list_dolinks = PageElements(xpath="//a[@class='cyan display-in margL10']", describe="详情按钮")

    list_msgs = PageElements(xpath="//*[@class='col-8 tefL fontz']", describe="返回信息列表")

