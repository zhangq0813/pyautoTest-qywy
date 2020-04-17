"""
@author:  张强
@data: 2020-4-17
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.receipt_page import ReceiptPage


class Test_receipt:
    """电子回单"""

    def test_receiptBill_case(self, browser, base_url):
        """
        名称：电子回单
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        receiptPage = ReceiptPage(browser)
        receiptPage.get(base_url)
        sleep(1)
        if receiptPage.basePage_alert:
            print('调试信息！')
            receiptPage.basePage_sure_button.click()
        else:
            print('go on!')

        receiptPage.menu_account_button.click()
        sleep(1)

        receiptPage.firstPage_receipt_link.click()
        sleep(1)

        assert receiptPage.resultPage_receipt_indexs

    def test_receiptDetail_case(self, browser, base_url):
        """
        名称：电子回单明细
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        receiptPage = ReceiptPage(browser)
        '''
        receiptPage.get(base_url)
        sleep(1)
        if receiptPage.basePage_alert:
            print('调试信息！')
            receiptPage.basePage_sure_button.click()
        else:
            print('go on!')
        '''
        receiptPage.menu_account_button.click()
        sleep(1)

        receiptPage.firstPage_receipt_link.click()
        sleep(1)
        receiptPage.resultPage_detail_button.click()
        sleep(1)

        assert not receiptPage.resultPage_detail_indexs

    def test_receiptHistory_case(self, browser, base_url):
        """
        名称：电子回单历史
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """

        receiptPage = ReceiptPage(browser)
        '''是否可以套用登录
        receiptPage.get(base_url)
        sleep(1)
        if receiptPage.basePage_alert:
            print('调试信息！')
            receiptPage.basePage_sure_button.click() 
        else:
            print('go on!')
        '''
        receiptPage.menu_account_button.click()
        sleep(1)

        receiptPage.firstPage_receipt_link.click()
        sleep(1)
        receiptPage.resultPage_history_button.click()
        sleep(1)

        assert receiptPage.resultPage_history_indexs


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_receipt.py"])
    #Test_reconciliation.test_reconciliation_case()
