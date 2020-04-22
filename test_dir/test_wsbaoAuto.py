"""
@author:  张强
@data: 2020-4-20
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.wsbaoAuto_page import WsbaoAutoPage


class Test_wsbaoAuto:
    """余利宝自动归集"""

    def test_wsbaoAuto_case(self, browser, base_url):
        """
        名称：余利宝自动归集
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        wsbaoAutoPage = WsbaoAutoPage(browser)
        wsbaoAutoPage.get(base_url)
        sleep(1)
        if wsbaoAutoPage.basePage_alert:
            print('调试信息！')
            wsbaoAutoPage.basePage_sure_button.click()
        else:
            print('go on!')

        wsbaoAutoPage.menu_wsbao_button.click()
        sleep(1)
        '''余利宝主页'''
        wsbaoAutoPage.firstPage_wsbaoAuto_link.click()
        sleep(1)

        '''设置页面'''
        wsbaoAutoPage.secondPage_padding_button.click()
        sleep(1)
        wsbaoAutoPage.secondPage_padding_input.send_keys('10000')
        sleep(1)
        wsbaoAutoPage.secondPage_submit_input.click()
        sleep(1)

        '''验证码校验页面'''
        wsbaoAutoPage.msurePage_verifycode_button.click()
        wsbaoAutoPage.msurePage_verifycode_input.send_keys("123456")
        wsbaoAutoPage.msurePage_confirm_button.click()
        sleep(1)

        '''结果页'''
        assert '修改自动转入录入成功' in wsbaoAutoPage.result_msg.text

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_wsbaoAuto.py"])
