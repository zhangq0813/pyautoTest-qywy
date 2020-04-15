from poium import Page, PageElement, PageElements


class DayBalanceQueryPage(Page):
    '''alert弹框'''
    basePage_alert = PageElement(xpath="/html/body/div[6]/div/span/div", describe="电子对账提示框")
    basePage_sure_button = PageElement(xpath="/html/body/div[6]/div/span/div/div/div/span/span/button[2]",
                                        describe="确定按钮")

    '''菜单按钮'''
    menu_transfer_button = PageElement(xpath="//li[@href='#/Transfer']", describe="转账菜单")
    menu_account_button = PageElement(xpath="//li[@href='#/AccountManage/AccountQry']",describe="账户菜单")

    '''#####页面对象#####'''
    '''首页'''
    firstPage_dayBalanceQuery_link = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.0.2.1.0.3']",
                                        describe="日终余额")
    '''查询结果页'''
    secondPage_startDate_button = PageElement(xpath="//input[@data-reactid='.0.0.0.1.0.0.0.0.0.0.$/=12.0.$=10']",
                                              describe="起始时间")
    #/html/body/div[6]/div/div/div[2]/table/tbody/tr[2]/td[4]/span
    #secondPage_startDate_iframe_button = PageElement(xpath="//input[@data-reactid='.1.0.1.0.1.$1.1:$10']",describe="2016-1-7")
    secondPage_startDate_iframe_button = PageElement(xpath="/html/body/div[6]/div/div/div[2]/table/tbody/tr[2]/td[4]/span",
                                                     describe="2016-1-7")
    secondPage_endDate_button = PageElement(xpath="//input[@data-reactid='.0.0.0.1.0.0.0.0.0.0.$/=14.0.$=10']",
                                              describe="结束时间")
    secondPage_endDate_iframe_button = PageElement(xpath="/html/body/div[7]/div/div/div[2]/table/tbody/tr[2]/td[3]/span",
                                                     describe="2016-1-8")

    secondPage_query_button = PageElement(xpath="//input[@data-reactid='.0.0.0.1.0.0.0.0.0.0.$/=15.$/=10']",
                                           describe="查询按钮")
    secondPage_endPage_button = PageElement(xpath="//*[@data-reactid='.0.0.0.1.0.0.0.1.1.0.2.2.0']", describe="尾页")
    secondPage_result_account = PageElement(
        xpath="//*[@data-reactid='.0.0.0.1.0.0.0.1.1.0.0.1.0.2.$2016-12-02.$accountNo.1']"
        , describe="结果账户")



