from poium import Page,PageElement,PageElements

class BalanceQuerypage(Page):


    firstPage_alert = PageElement(xpath="/html/body/div[6]/div/span/div",describe = "电子对账提示框")
    firstPage_sure_button = PageElement(xpath="/html/body/div[6]/div/span/div/div/div/span/span/button[2]",describe="确定按钮")
    firstPage_accountmenu_button = PageElement(xpath="//li[@href='#/AccountManage/AccountQry']",describe="账户菜单")
    firstPage_yearlv_text = PageElement(xpath="//span[@data-reactid='.0.0.0.1.1.0.1.0.0.4.0.0.0.1.1.1']",describe="活期利率")

