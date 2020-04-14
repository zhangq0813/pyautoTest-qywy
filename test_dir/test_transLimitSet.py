"""
@author:  张强
@data: 2020-4-13
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath
from selenium import webdriver

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.transLimitSet_page import Translimitpage


class Test_transLimitSet:
    """百度搜索"""

    def test_transLimitSet_case(self, browser, base_url):
        """
        名称：转账明细查询
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        transLimitSetPage = Translimitpage(browser)
        transLimitSetPage.get(base_url)
        sleep(1)
        if transLimitSetPage.basePage_alert:
            print('调试信息！')
            transLimitSetPage.basePage_sure_button.click()
        else:
            print('go on!')

        transLimitSetPage.menu_account_button.click()
        sleep(1)

        transLimitSetPage.firstPage_limitset_link.click()
        sleep(2)
        a = browser.current_window_handle
        b = browser.window_handles
        #切换窗口
        for handle in b:
            if handle != a:
                browser.switch_to_window(handle)

                transLimitSetPage.secondPage_limitset_button.click()
                #browser.find_element_by_xpath("//*[@id='main_content']/div/div/div[3]/form/div[2]/input").click()
                sleep(1)
                transLimitSetPage.thirdPage_alimit_input.clear()
                transLimitSetPage.thirdPage_alimit_input.send_keys("200")
                transLimitSetPage.thirdPage_daylimit_input.clear()
                transLimitSetPage.thirdPage_daylimit_input.send_keys("5000")
                transLimitSetPage.thirdPage_yearlimit_input.clear()
                transLimitSetPage.thirdPage_yearlimit_input.send_keys("10000")
                transLimitSetPage.thirdPage_next_button.click()
                sleep(1)

                transLimitSetPage.msurePage_verifycode_button.click()
                transLimitSetPage.msurePage_verifycode_input.send_keys("123456")
                transLimitSetPage.msurePage_confirm_button.click()
                sleep(1)
                resultmsg = transLimitSetPage.result_msg.text
                assert "已提交" in resultmsg

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_transLimitSet.py"])
