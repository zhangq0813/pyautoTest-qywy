from poium import Page, PageElement, PageElements


class BillQueryPage(Page):
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
    firstPage_billquery_link = PageElement(xpath="//*[@href='#/BillsManage/BillsQry']", describe="工单查询菜单")

    '''查询页'''
    firstPage_status_combox = PageElement(xpath="//*[@class='ant-select-selection__rendered']", describe="审批状态")
    firstPage_status_comboxs = PageElements(xpath="//li[@role='menuitem']", describe="审批状态值")

    firstPage_date_comboxs = PageElements(xpath="//*[@class='ant-calendar-picker-input ant-input']", describe="日期控件")
    firstPage_startdate_tables = PageElements(xpath="//*[@class='ant-calendar-cell']", describe="具体日期")
    firstPage_enddate_tables = PageElements(xpath="//*[@class='ant-calendar-cell']", describe="具体日期")
    firstPage_query_button = PageElement(xpath="//input[@value='查询']", describe="查询")


    '''查询结果页'''
    secondPage_result_list = PageElements(xpath="//*[@class='ant-table-row ']", describe="查询结果列表")

