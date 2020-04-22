from poium import Page, PageElement, PageElements
import datetime


class TransfersQueryPage(Page):
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

    '''批量查询'''
    firstPage_transfersQuery_button = PageElement(xpath="//*[@href='#/BatchBusinessManage/BatchQuery']",describe="批量查询")

    '''条件录入'''
    firstPage_trstype_combox = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.0.0.0.$/=10.$/=11.$/=11']",
                                        describe="批量类型")
    firstPage_trschannel_combox = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.0.0.0.$/=10.$/=12.$/=11']",
                                        describe="交易渠道")
    firstPage_trsstatus_combox = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.0.0.0.$/=11.$/=10.$/=11']",
                                        describe="处理状态")
    firstPage_date_combox = PageElements(xpath="//*[@class='ant-calendar-picker-input ant-input ant-input-lg']",
                                             describe="日期控件")

    #firstPage_trschannel_comboxs = PageElement(xpath="//div[data-reactid='.3.0']/ul/li[@role='menuitem']",
    #                                           describe="交易渠道")
    firstPage_trstype_comboxs = PageElements(xpath="//ul/li[@role='menuitem']",
                                           describe="下拉类型")
    firstPage_trschannel_comboxs = PageElements(xpath="//ul/li[@role='menuitem']",
                                           describe="下拉类型")
    firstPage_trsstatus_comboxs = PageElements(xpath="//ul/li[@role='menuitem']",
                                           describe="下拉类型")

    firstPage_startdate_tables = PageElements(xpath="//*[@role='gridcell']",describe="开始日期")
    firstPage_enddate_tables = PageElements(xpath="//*[@role='gridcell']",describe="结束日期")


    '''代发录入确认页面'''
    firstPage_download_label = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.1.1.0.0.1.0.2.$2016041810270000760512.$10.1.0']",
                                               describe="下载链接")
    firstPage_download_link = PageElement(link_text="下载单笔回单")
    firstPage_query_button = PageElement(xpath="//*[@value='查询']", describe="查询按钮")


    '''下载页'''
    secondPage_accountno_input = PageElement(xpath="//*[@id='accountNo']",describe="收款卡号")
    secondPage_accountame_input = PageElement(xpath="//*[@id='accountName']",describe="收款户名")
    secondPage_query_button = PageElement(xpath="//*[@value='查询']", describe="查询按钮")
    secondPage_download_button = PageElements(xpath="//*[@data-seed='batch_item_download_receipt']", describe="回单下载按钮")

    '''结果确认页面'''
    thirdPage_sure_button = PageElement(xpath="//*[@value='确定下载']", describe="确定下载")

    '''结果验证页面'''
    fourthPage_msg = PageElement(xpath="//*[@class='TrsContFont']", describe="下载成功信息")



