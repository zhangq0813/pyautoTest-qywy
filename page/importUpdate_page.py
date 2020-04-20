from poium import Page, PageElement, PageElements


class ImportUpdatePage(Page):
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

    firstPage_importUpdate_button = PageElement(xpath="//*[@value='导入更新']",describe="导入更新")
    '''设置页'''
    secondPage_dialogUpload_button = PageElement(xpath="//*[@data-seed='roster_up_fild_upload']", describe="文件上传")

    secondPagee_next_button = PageElement(xpath="//*[@value='下一步']", describe="下一步按钮")

    '''结果页'''
    result_msg = PageElement(xpath="//*[@id='sucessDlg']/div[2]/div[2]/div/span", describe="成功提示信息")
    result_sure_button = PageElement(xpath="//*[@id='sucessDlg']/div[2]/div[3]/input", describe="知道了按钮")

