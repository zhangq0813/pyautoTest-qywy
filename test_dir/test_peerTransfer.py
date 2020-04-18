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
from page.peerTransfer_page import PeerTransferpage

class Test_test_peerTransfer:
    """
    测试行内转账
    """
    def test_peerTransfer_case(self,browser,base_url):
        """
        名称：行内转账
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        peerTransferPage = PeerTransferpage(browser)
        peerTransferPage.get(base_url)
        sleep(2)
        if peerTransferPage.firstPage_alert:
            print('调试信息！')
            peerTransferPage.firstPage_sure_button.click()
        else:
            print('go on!')

        peerTransferPage.firstPage_menu_button.click()
        peerTransferPage.firstPage_transaccount_input.send_keys("6214855510376144")
        peerTransferPage.firstPage_transname_input.send_keys("京东公司")
        peerTransferPage.firstPage_transamount_input.send_keys("100")
        peerTransferPage.firstPage_next_button.click()
        sleep(1)
        peerTransferPage.secondPage_verifycode_button.click()
        sleep(1)
        peerTransferPage.secondPage_verifycode_input.send_keys('123456')
        peerTransferPage.secondPage_confirm_button.click()
        sleep(1)
        assert peerTransferPage.confirmPage_return_button.get_attribute("value") =="返回"

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_peerTransfer.py"])