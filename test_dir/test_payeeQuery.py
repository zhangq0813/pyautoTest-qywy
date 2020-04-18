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
from page.payeeQuery_page import PayeeQuerypage

class Test_test_payeeQuery:
    """
    测试收款人查找
    """
    def test_payeeQuery_case(self,browser,base_url):
        """
        名称：收款人查找
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        queryvalue = '罗贯中'
        payeeQueryPage = PayeeQuerypage(browser)
        payeeQueryPage.get(base_url)
        sleep(2)
        if payeeQueryPage.firstPage_alert:
            print('调试信息！')
            payeeQueryPage.firstPage_sure_button.click()
        else:
            print('go on!')

        payeeQueryPage.firstPage_menu_button.click()

        payeeQueryPage.firstPage_payeequery_input.send_keys(queryvalue)
        sleep(1)
        resultlist = payeeQueryPage.firstPage_payeequery_lists

        for i in range(0,len(resultlist)):
            assert queryvalue in resultlist[i].text

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_payeeQuery.py"])