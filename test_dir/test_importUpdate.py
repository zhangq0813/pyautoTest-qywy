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
from page.importUpdate_page import ImportUpdatePage


class Test_importUpdate:
    """交易明细查询"""

    def test_importUpdate_case(self, browser, base_url):
        """
        名称：交易明细查询
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        importUpdatePage = ImportUpdatePage(browser)
        importUpdatePage.get(base_url)
        sleep(1)
        if importUpdatePage.basePage_alert:
            print('调试信息！')
            importUpdatePage.basePage_sure_button.click()
        else:
            print('go on!')

        importUpdatePage.menu_batch_button.click()
        sleep(1)

        importUpdatePage.firstPage_importUpdate_button.click()
        sleep(1)
        '''打开文件上传窗体'''
        importUpdatePage.secondPage_dialogUpload_button.click()
        sleep(1)
        system(r"C:\Users\Zhangq\PycharmProjects\pyautoTest-qywy\win32\dialogUpload.exe")
        sleep(1)
        importUpdatePage.secondPagee_next_button.click()
        sleep(1)
        assert importUpdatePage.result_msg.text == '更新名册成功1'
        importUpdatePage.result_sure_button.click()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_importUpdate.py"])
