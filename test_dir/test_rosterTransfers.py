"""
@author:  张强
@data: 2020-4-20
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from os import system

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.rosterTransfers_page import RosterTransfersPage


class Test_rosterTransfers:
    """批量代发-名册代发"""

    def test_rosterTransfers(self, browser, base_url):
        """
        名称：批量代发-名册代发
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
        rosterTransfersPage = RosterTransfersPage(browser)
        rosterTransfersPage.get(base_url)
        sleep(1)
        if rosterTransfersPage.basePage_alert:
            print('调试信息！')
            rosterTransfersPage.basePage_sure_button.click()
        else:
            print('go on!')

        rosterTransfersPage.menu_batch_button.click()
        sleep(1)

        rosterTransfersPage.firstPage_fileTransfers_button.click()
        rosterTransfersPage.firstPage_rosterTransfers_button.click()
        sleep(1)

        '''信息录入页面'''
        rostertrslabels = rosterTransfersPage.firstPage_rosterTransfers_labels
        rosterlables = rosterTransfersPage.firstPage_rosters_labels
        rostertrslabels[0].click()
        rostertrslabels[3].click()
        rosterTransfersPage.firstPage_fileSummary_input.send_keys(fileSummary)
        rosterlables[0].click()
        rosterTransfersPage.firstPage_next_button.click()
        sleep(1)

        '''验证码页面'''
        rosterTransfersPage.secondPage_verifycode_button.click()
        rosterTransfersPage.secondPage_verifycode_input.send_keys('123456')
        rosterTransfersPage.secondPage_next_button.click()
        sleep(1)

        '''结果页面'''
        assert rosterTransfersPage.result_msg.text == '3笔'
        rosterTransfersPage.result_sure_button.click()




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_rosterTransfers.py"])
