from poium import Page, PageElement, PageElements


class Translimitpage(Page):
    '''alert弹框'''
    basePage_alert = PageElement(xpath="/html/body/div[6]/div/span/div", describe="电子对账提示框")
    basePage_sure_button = PageElement(xpath="/html/body/div[6]/div/span/div/div/div/span/span/button[2]",
                                        describe="确定按钮")

    '''菜单按钮'''
    menu_account_button = PageElement(xpath="//li[@href='#/AccountManage/AccountQry']",describe="账户菜单")

    '''#####页面对象#####'''
    '''首页'''
    firstPage_limitset_link = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.0.2.1.0.1']",
                                        describe="转账限额")
    '''设置页'''
    secondPage_limitset_button = PageElement(xpath="//input[@data-seed='modify_transfer_quota']", describe="修改转账限额按钮")

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

