from poium import Page,PageElement,PageElements

class PayeeQuerypage(Page):
    '''alert弹框'''
    firstPage_alert = PageElement(xpath="/html/body/div[6]/div/span/div",describe = "电子对账提示框")
    firstPage_sure_button = PageElement(xpath="/html/body/div[6]/div/span/div/div/div/span/span/button[2]",describe="确定按钮")

    '''菜单按钮'''
    firstPage_menu_button = PageElement(xpath="//li[@href='#/Transfer']",describe="转账菜单")

    '''#####页面对象#####'''
    '''录入页面'''
    firstPage_payeequery_input = PageElement(xpath="//input[@data-reactid='.0.0.0.1.1.0.1.0.1.1.0.0.0.0']",describe="账户搜索框")
    firstPage_payeequery_lists = PageElements(xpath="//div[@class='card-item-inner ']",describe="搜索结果")

