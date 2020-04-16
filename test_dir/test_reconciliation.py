"""
@author:  张强
@data: 2020-4-15
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.reconciliation_page import ReconciliationPage


class Test_reconciliation:
    """百度搜索"""

    def test_reconciliation_case(self, browser, base_url):
        """
        名称：跨行实时转账
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        reconciliationPage = ReconciliationPage(browser)
        reconciliationPage.get(base_url)
        sleep(1)
        if reconciliationPage.basePage_alert:
            print('调试信息！')
            reconciliationPage.basePage_sure_button.click()
        else:
            print('go on!')

        reconciliationPage.menu_account_button.click()
        sleep(1)

        reconciliationPage.firstPage_reconciliation_link.click()
        sleep(1)

        #reconciliationPage.secondPage_reconciliation_select
        reconciliationPage.secondPage_startDate_button.click()
        reconciliationPage.secondPage_startDate_table_button.click()
        #reconciliationPage.secondPage_endDate_button.click()
        #reconciliationPage.secondPage_endDate_table_button.click()
        reconciliationPage.secondPage_query_button.click()
        sleep(1)
        #lista = browser.find_elements_by_class_name("dft margL20 cyan")
        #lista = reconciliationPage.list_dolinks
        #txt = lista[0].getattribute("data-mtr-brsym")
        #txt1 = lista[0].get_attribute("data-mtr-brsym")
        '''
        for dolink in lista:
            if dolink.get_attribute("data-mtr-brsym") == '201601' and dolink.get_attribute(
                        "data-mtr-brs-status") == '03':
                dolink.click()

        '''
        '''
        for dolink in reconciliationPage.list_dolinks:
            try:
                if dolink.get_attribute("data-mtr-brsym") == '201601' and dolink.get_attribute(
                        "data-mtr-back-status") == '04':
                    dolink.click()
                    hl = browser.current_window_handle
                    handles = browser.window_handles
                    for handle in handles:
                        if handle != hl:
                            browser.switch_to_window(handle)
                            sleep(1)
                            assert reconciliationPage.resultPage_msg.text == '2016年01月电子对账单'
                else:
                    print("未查找到dolink对象")
            except:
                    print("未查找到dolink对象")
        '''

        for dolink in reconciliationPage.list_dolinks:
            if dolink.get_attribute("data-mtr-brsym") == '201601' and dolink.get_attribute(
                    "data-mtr-back-status") == '04' and dolink.text =='查看明细':
                dolink.click()
                hl = browser.current_window_handle
                handles = browser.window_handles
                for handle in handles:
                    if handle != hl:
                        browser.switch_to_window(handle)
                        sleep(1)
                        print("成功跳转")
                        assert reconciliationPage.resultPage_msg.text == '2016年01月电子对账单'
                        break
                break
            else:
                 print("未查找到dolink对象")



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_reconciliation.py"])
    #Test_reconciliation.test_reconciliation_case()
