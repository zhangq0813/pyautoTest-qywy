from poium import Page, PageElement, PageElements


class OperatorModifyPage(Page):
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
    firstPage_OperatorManage_link = PageElement(xpath="//*[@href='#/MemberManage/OperatorManage']",describe="操作员管理")
    firstPage_primary_links = PageElements(xpath="//*[@class='ant-btn ant-btn-primary ant-btn-menu ']",describe="操作详情")
    firstPage_modify_link = PageElement(xpath="//div[@class='toggle-down-content']/ul/li[2]",describe="修改")

    '''设置页'''
    #secondPage_inline_checkbox = PageElements(xpath="//*[@class='ant-checkbox-inline']", describe="基础权限")
    '''为何实际上是2个对象，定位出来4个'''
    #secondPage_inline_checkbox = PageElements(xpath="//label[@class='ant-checkbox-inline']/span", describe="基础权限")
    '''下属方法定位正确'''
    #secondPage_inline_checkbox = PageElements(xpath="//label/span[starts-with(@class,'ant-checkbox')]", describe="基础权限")
    secondPage_inline_checkbox = PageElements(xpath="//label/span[contains(@class,'ant-checkbox')]", describe="基础权限")
    '''ends-with不对'''
    #secondPage_inline_checkbox = PageElements(xpath="//label/span[ends-with(@class,'ant-checkbox')]", describe="基础权限")

    secondPage_ant_switch = PageElement(xpath="//*[@class='ant-switch-inner']", describe="银企直联开关")
    '''获取得是4个主复选框'''
    #secondPage_tree_checkbox = PageElements(xpath="//ul[@class='ant-tree']/li/a", describe="账户权限")
    secondPage_tree_checkbox = PageElements(xpath="//ul[@class='ant-tree']/li/a", describe="账户权限")



    '''录入页'''
    thirdPage_alimit_input = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.0.0.1.0.0.0.$/=14.$/=11.0.$/=10']", describe="单笔限额")
    thirdPage_daylimit_input = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.0.0.1.0.0.0.$/=15.$/=11.0.$/=10']", describe="日累计限额")
    thirdPage_yearlimit_input = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.0.0.1.0.0.0.$/=16.$/=11.0.$/=10']", describe="月累计限额")
    thirdPage_next_button = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.0.0.1.0.0.0.$/=17.$/=10']", describe="下一步")
    #thirdPage_next_button = PageElement(xpath="//input[@value='下一步']", describe="下一步")

    '''限额确认页面'''
    msurePage_verifycode_button = PageElement(xpath="//input[@data-seed='get_verify_code']", describe="获取验证码")
    msurePage_verifycode_input = PageElement(xpath="//input[@placeholder='请输入验证码']", describe="验证码输入框")
    msurePage_confirm_button = PageElement(xpath="//*[@value='下一步']", describe="确定按钮")

    '''结果页'''
    result_msg = PageElement(xpath="//span[@data-reactid='.0.0.0.1.1.0.1.0.0.0.1.0.1.1']", describe="成功提示信息")

