"""
@author:  张强
@data: 2020-4-20
"""
from time import sleep
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.alipayTransfer_page import AlipayTransferpage

class Test_test_alipayTransfer:
    """
    测试支付宝转账
    """
    def test_alipayTransfer_case(self,browser,base_url):
        """
        名称：支付宝转账
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        alipayTransferPage = AlipayTransferpage(browser)
        alipayTransferPage.get(base_url)
        sleep(2)
        if alipayTransferPage.firstPage_alert:
            print('调试信息！')
            alipayTransferPage.firstPage_sure_button.click()
        else:
            print('go on!')

        alipayTransferPage.firstPage_menu_button.click()
        alipayTransferPage.firstPage_alipaymenu_button.click()
        sleep(1)

        alipayTransferPage.firstPage_transaccount_input.send_keys("6214855510376144")
        alipayTransferPage.firstPage_transname_input.send_keys("张三")
        alipayTransferPage.firstPage_trsamount_input.send_keys("100")
        alipayTransferPage.firstPage_trsamount_index.click()
        sleep(1)
        '''获取下拉框中值'''
        indexlist = alipayTransferPage.firstPage_trsamount_indexs
        for i in range(0,len(indexlist)):
            if "奖金" in indexlist[i].text:
                indexlist[i].click()
                break

        alipayTransferPage.firstPage_next_button.click()
        sleep(1)
        '''验证码校验页面'''
        alipayTransferPage.secondPage_verifycode_button.click()
        alipayTransferPage.secondPage_verifycode_input.send_keys("123456")
        alipayTransferPage.secondPage_confirm_button.click()
        sleep(1)

        assert '单笔转账录入成功' in alipayTransferPage.confirmPage_return_msg.text


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_alipayTransfer.py"])