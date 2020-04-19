from poium import Page,PageElement,PageElements

class AlipayTransferpage(Page):
    '''alert弹框'''
    firstPage_alert = PageElement(xpath="/html/body/div[6]/div/span/div",describe = "电子对账提示框")
    firstPage_sure_button = PageElement(xpath="/html/body/div[6]/div/span/div/div/div/span/span/button[2]",describe="确定按钮")

    '''菜单按钮'''
    firstPage_menu_button = PageElement(xpath="//li[@href='#/Transfer']",describe="转账菜单")
    firstPage_intermenu_button = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.1.1.0.1.1.0.0.$1']",describe="跨行转账")
    firstPage_alipaymenu_button = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.1.1.0.1.1.0.0.$2']",describe="支付宝转账")

    '''转账信息'''
    '''录入页面'''
    firstPage_transaccount_input = PageElement(name="payeeAccNo",describe="收款账号")
    firstPage_transname_input = PageElement(name="payeeAccName",describe="收款账户名")

    '''付款信息'''
    firstPage_trsamount_input = PageElement(xpath="//*[@name='trsAmount']",describe='转账金额')
    firstPage_trsamount_index = PageElement(xpath="//span[@data-reactid='.0.0.0.1.1.0.1.0.1.1.0.1.1.1.$0.0.1.0.0.$/=1a.$/=11.0.$/=10.$selection.0']"
                                            ,describe="付款用途")
    firstPage_trsamount_indexs = PageElements(xpath="//div/ul/li[@role='menuitem']",describe="付款用途列表")
    firstPage_next_button = PageElement(xpath="//input[@data-seed='alipay-next']",describe="下一步")

                                         
    '''转账确认页面'''
    secondPage_verifycode_button = PageElement(xpath="//input[@data-seed='get_verify_code']",describe="获取验证码")
    secondPage_verifycode_input = PageElement(xpath="//input[@placeholder='请输入验证码']",describe="验证码输入框")
    secondPage_confirm_button = PageElement(xpath="//*[@value='确定']",describe="确定按钮")

    '''结果页'''
    confirmPage_return_msg = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.1.0.1.1']",describe="反显信息")
