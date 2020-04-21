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
from page.fileTransfers_page import FileTransfersPage


class Test_fileTransfers:
    """批量代发-文件代发"""

    def test_fileTransfers(self, browser, base_url):
        """
        名称：批量代发-文件代发
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
        fileTransfersPage = FileTransfersPage(browser)
        fileTransfersPage.get(base_url)
        sleep(1)
        if fileTransfersPage.basePage_alert:
            print('调试信息！')
            fileTransfersPage.basePage_sure_button.click()
        else:
            print('go on!')

        fileTransfersPage.menu_batch_button.click()
        sleep(1)

        fileTransfersPage.firstPage_fileTransfers_button.click()
        sleep(1)

        '''信息录入页面'''
        fileTransfersPage.firstPage_num_input.send_keys(trsNums)
        fileTransfersPage.firstPage_ant_input.send_keys(trsAnt)
        lables = fileTransfersPage.firstPage_filetrs_labels
        lables[1].click()
        fileTransfersPage.firstPage_delayPayDate_input.click()
        sleep(1)
        fileTransfersPage.firstPage_delayPayDate_table.click()
        sleep(1)
        lables[3].click()
        sleep(1)
        fileTransfersPage.firstPage_fileSummary_input.send_keys(fileSummary)
        fileTransfersPage.firstPage_rcUpload_link.click()
        sleep(1)
        system("D:\自动化测试\pytest-yt-qywy\win32\dialogUpload.exe")
        sleep(1)
        fileTransfersPage.firstPage_next_button.click()
        sleep(1)

        '''验证码页面'''
        fileTransfersPage.secondPage_verifycode_button.click()
        fileTransfersPage.secondPage_verifycode_input.send_keys('123456')
        fileTransfersPage.secondPage_next_button.click()
        sleep(1)

        '''结果页面'''
        assert fileTransfersPage.result_msg.text == trsNums+'笔'
        fileTransfersPage.result_sure_button.click()




if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_fileTransfers.py"])
