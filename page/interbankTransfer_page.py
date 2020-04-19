from poium import Page,PageElement,PageElements

class InterBankTransferpage(Page):
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
    '''收款信息'''
    firstPage_transbank_index = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.1.1.0.1.1.1.$0.0.1.0.0.$/=12.$/=10.$/=11.0.$/=10.$selection.0.2.0.0']")
    firstPage_transbank_indexs = PageElements(xpath="//ul/li[@role='menuitem']",describe="收款银行")
    firstPage_yhwd_button = PageElement(xpath="//*[@data-seed='dept_show_query_btn']",describe="查询网点")

    '''网点查询弹框页面'''
    #secendPage_yhwdkey_input = PageElement(xpath="//input[@data-reactid='.5.$dialog.0.1.0.0.1.0.0']",describe="网点关键字") #id会变化
    secendPage_yhwdkey_input = PageElement(xpath="//input[@class='transfer-content-popup-input radius marg0']", describe="网点关键字")
    secendPage_yhwdkey_button = PageElement(xpath="//input[@value='搜索']",describe="网点搜素")
    secendPage_yhwdkeyvalue_indexs = PageElements(xpath="//*[@class='bank-item fontz']",describe="网点搜索结果")
    secendPage_yhwdsure_button = PageElement(xpath="//*[@data-seed='model_ok_btn']",describe="网点搜索确认按钮")
    secendPage_yhwdkey_result = PageElement(xpath="//p[@data-reactid='.0.0.0.1.1.0.1.0.1.1.0.1.1.1.$0.0.1.0.0.$/=12.$/=11.$/=11.$/=10']",describe="网点反显")

    '''付款信息'''
    firstPage_trsamount_button = PageElement(xpath="//*[@name='trsAmount']",describe='转账金额')
    firstPage_trsamount_types = PageElements(xpath="//*[@class='ant-radio']",describe="到账方式")
    firstPage_trsamount_index = PageElement(xpath="//span[@data-reactid='.0.0.0.1.1.0.1.0.1.1.0.1.1.1.$0.0.1.0.0.$/=1a.$/=11.0.$/=10.$selection.0']",describe="付款用途")
    firstPage_trsamount_indexs = PageElements(xpath="//div/ul/li[@role='menuitem']",describe="付款用途列表")
    firstPage_next_button = PageElement(xpath="//input[@data-seed='cross-next']",describe="下一步")

                                         
    '''转账确认页面'''
    thirdPage_verifycode_button = PageElement(xpath="//input[@data-seed='get_verify_code']",describe="获取验证码")
    thirdPage_verifycode_input = PageElement(xpath="//input[@placeholder='请输入验证码']",describe="验证码输入框")
    sthirdPage_confirm_button = PageElement(xpath="//*[@value='确定']",describe="确定按钮")

    '''结果页'''
    confirmPage_return_msg = PageElement(xpath="//*[@data-reactid='.0.0.0.1.1.0.1.0.1.0.1.1']",describe="反显信息")
