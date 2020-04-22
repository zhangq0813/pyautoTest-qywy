"""
@author:  张强
@data: 2020-4-22
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from os import system

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.transfers_page import TransfersPage


class Test_transfers:
    """批量转账"""

    def test_transfers(self, browser, base_url):
        """
        名称：批量转账
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        trsNums = '100'
        trsAnt = '10000'
        fileSummary = '20201010代发工资'
        transfersPage = TransfersPage(browser)
        transfersPage.get(base_url)
        sleep(1)
        if transfersPage.basePage_alert:
            print('调试信息！')
            transfersPage.basePage_sure_button.click()
        else:
            print('go on!')

        transfersPage.menu_batch_button.click()
        sleep(1)

        transfersPage.firstPage_transfers_button.click()
        sleep(1)

        '''信息录入页面'''
        transfersPage.firstPage_num_input.send_keys(trsNums)
        transfersPage.firstPage_ant_input.send_keys(trsAnt)
        transfersPage.firstPage_fileSummary_input.send_keys(fileSummary)
        transfersPage.firstPage_upload_link.click()
        sleep(1)
        system("D:\win32\dialogUpload.exe")
        sleep(1)
        transfersPage.firstPage_next_button.click()
        sleep(1)

        '''验证码页面'''
        transfersPage.secondPage_verifycode_button.click()
        transfersPage.secondPage_verifycode_input.send_keys('123456')
        transfersPage.secondPage_next_button.click()
        sleep(1)

        '''结果页面'''
        assert transfersPage.result_msg.text == trsNums
        transfersPage.result_sure_button.click()




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_transfers.py"])
