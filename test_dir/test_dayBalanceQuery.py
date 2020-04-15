from time import sleep
import pytest
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.dayBalanceQuery_page import DayBalanceQueryPage

class Test_dayBalanceQuery:

    def test_dayBalanceQuery_case(self,browser,base_url):
        """
        名称：日终余额设置
        步骤：
        1、打开浏览器,输入测试网址
        2、点击账户信息菜单按钮，跳转到账户页面
        3、点击日终余额按钮，进入日终余额查询页面
        4、输入账户，开始结束时间，点击查询
        5、点击尾页图标，跳转到尾页
        断言：
        检查页面账户是否反显步骤4中录入的账户，且信息保持一致
        """
        dayBalanceQueryPage = DayBalanceQueryPage(browser)
        dayBalanceQueryPage.get(base_url)
        sleep(2)
        if not dayBalanceQueryPage.basePage_alert:
            print('调试信息！')
            dayBalanceQueryPage.basePage_sure_button.click()
        else:
            print('go on!')

        dayBalanceQueryPage.menu_account_button.click()
        sleep(1)
        dayBalanceQueryPage.firstPage_dayBalanceQuery_link.click()
        sleep(1)
        hd = browser.current_window_handle
        handles = browser.window_handles
        for handle in handles:
            if handle != hd:
                browser.switch_to_window(handle)
                dayBalanceQueryPage.secondPage_startDate_button.click()
                dayBalanceQueryPage.secondPage_startDate_iframe_button.click()
                dayBalanceQueryPage.secondPage_endDate_button.click()
                dayBalanceQueryPage.secondPage_endDate_iframe_button.click()
                dayBalanceQueryPage.secondPage_query_button.click()
                sleep(1)
                dayBalanceQueryPage.secondPage_endPage_button.click()
                sleep(1)
                assert dayBalanceQueryPage.secondPage_result_account.text == '8888880000008881'

if __name__ == "__main__":
    pytest.main(['-v','-s','test_dayBalanceQuery.py'])

