"""
@author:  张强
@data: 2020-4-15
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from commom.formatCurrency import formatCurrency
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.wsbaoTransOut_page import WsbaoTransOutPage


class Test_wsbaoTransOut:
    """余利宝转入"""

    def test_wsbaoTransOut_case(self, browser, base_url):
        """
        名称：余利宝转出
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        outputMon = '1000'
        wsbaoTransOutPage = WsbaoTransOutPage(browser)
        wsbaoTransOutPage.get(base_url)
        sleep(1)
        if wsbaoTransOutPage.basePage_alert:
            print('调试信息！')
            wsbaoTransOutPage.basePage_sure_button.click()
        else:
            print('go on!')

        wsbaoTransOutPage.menu_account_button.click()
        sleep(1)

        wsbaoTransOutPage.firstPage_wsbaotransout_link.click()
        sleep(1)
        antvalue = wsbaoTransOutPage.secondPage_wsbaotransout_ant.text
        '''通过字符拼接得到整数位'''
        '''
        list1 = antvalue.split('.')
        list2 = list1[0].split(",")
        antvaluelist = ''
        for i in range(0,len(list2)):
            antvaluelist = antvaluelist + list2[i]
        '''
        '''通过系统提供的join函数拼接字符串，更加灵活'''
        list1 = antvalue.split('.')
        list2 = list1[0].split(",")
        antvaluelist = ''.join(list2)


        assert int(antvaluelist) > 0

        wsbaoTransOutPage.secondPage_wsbaotransout_input.send_keys(outputMon)
        sleep(1)

        assert wsbaoTransOutPage.secondPage_wsbaotransout_output.text == formatCurrency(outputMon)

        wsbaoTransOutPage.secondPage_next_button.click()
        sleep(1)

        wsbaoTransOutPage.msurePage_verifycode_button.click()
        wsbaoTransOutPage.msurePage_verifycode_input.send_keys("123456")
        wsbaoTransOutPage.msurePage_confirm_button.click()
        sleep(1)

        assert "资金转出已提交" in wsbaoTransOutPage.result_msg.text


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_wsbaoTransOut.py"])
    #Test_reconciliation.test_reconciliation_case()
