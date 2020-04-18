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
from page.wsbaoTransIn_page import WsbaoTransInPage


class Test_wsbaoTransIn:
    """余利宝转入"""

    def test_wsbaoTransIn_case(self, browser, base_url):
        """
        名称：余利宝转入
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        inputMon = '1000'
        wsbaoTransInPage = WsbaoTransInPage(browser)
        wsbaoTransInPage.get(base_url)
        sleep(1)
        if wsbaoTransInPage.basePage_alert:
            print('调试信息！')
            wsbaoTransInPage.basePage_sure_button.click()
        else:
            print('go on!')

        wsbaoTransInPage.menu_account_button.click()
        sleep(1)

        wsbaoTransInPage.firstPage_wsbaotransin_link.click()
        sleep(1)

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@data-reactid='.0.0.0.1.1.0.1.0.1.0.0.$/=11.$/=12.$/=11.0']")))

        wsbaoTransInPage.secondPage_wsbaotransin_input.send_keys('1000')
        sleep(1)
        assert wsbaoTransInPage.secondPage_wsbaotransin_output.text == formatCurrency(inputMon)
        wsbaoTransInPage.secondPage_nextn_button.click()
        sleep(1)

        wsbaoTransInPage.msurePage_verifycode_button.click()
        wsbaoTransInPage.msurePage_verifycode_input.send_keys("123456")
        wsbaoTransInPage.msurePage_confirm_button.click()
        sleep(1)

        assert "资金转入已提交" in wsbaoTransInPage.result_msg.text


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_wsbaoTransIn.py"])
    #Test_reconciliation.test_reconciliation_case()
