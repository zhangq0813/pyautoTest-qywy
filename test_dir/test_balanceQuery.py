from time import sleep
import pytest
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.balanceQuerypage_page import BalanceQuerypage

class Test_balanceQuery:

    def test_balanceQueryy_case(self,browser,base_url):
        """
        名称：账户余额查询
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入账户，进入账户总览页面
        断言：
        检查页面中年利率是否反显年利率且大于0
        """
        balanceQueryPage = BalanceQuerypage(browser)
        balanceQueryPage.get(base_url)
        sleep(2)
        if not balanceQueryPage.firstPage_alert:
            print('调试信息！')
            balanceQueryPage.firstPage_sure_button.click()
        else:
            print('go on!')
        sleep(1)
        balanceQueryPage.firstPage_accountmenu_button.click()
        sleep(1)
        lv = balanceQueryPage.firstPage_yearlv_text.text
        strlv = "".join(lv.split("%"))  #以%分割字符串成列表，然后重新组合成新字符串，中间用空字符连接
        #assert strlv =='0.35'
        assert float(strlv) > 0

if __name__ == "__main__":
    pytest.main(['-v','-s','test_balanceQuery.py'])

