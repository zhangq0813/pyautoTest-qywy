"""
@author:  张强
@data: 2020-4-13
"""
from time import sleep
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.transfer_page import Transferpage

class Test_transfer:
    """
    测试转账
    """
    def test_transfer_case(self,browser,base_url):
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
        transferPage = Transferpage(browser)
        transferPage.get(base_url)
        sleep(2)
        if transferPage.firstPage_alert:
            print('调试信息！')
            transferPage.firstPage_sure_button.click()
        else:
            print('go on!')
        transferPage.firstPage_menu_button.click()
        transferPage.firstPage_transaccount_input.send_keys("6214855510376144")
        transferPage.firstPage_transname_input.send_keys("京东公司")
        transferPage.firstPage_transamount_input.send_keys("100")
        transferPage.firstPage_next_button.click()
        sleep(1)
        transferPage.secondPage_verifycode_button.click()
        sleep(1)
        transferPage.secondPage_verifycode_input.send_keys('123456')
        transferPage.secondPage_confirm_button.click()
        sleep(1)
        assert transferPage.confirmPage_return_button.get_attribute("value") =="返回"

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_transfer.py"])