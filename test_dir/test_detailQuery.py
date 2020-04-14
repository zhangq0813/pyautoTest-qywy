from time import sleep
import pytest
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.detailQuery_page import Detailquerypage

class Test_detailQuery:

    def test_detailquery_case(self,browser,base_url):
        """
        名称：账户余额查询
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入账户，进入账户总览页面
        断言：
        检查页面中年利率是否反显年利率且大于0
        """
        detailQueryPage = Detailquerypage(browser)
        detailQueryPage.get(base_url)
        sleep(2)
        if not detailQueryPage.firstPage_alert:
            print('调试信息！')
            detailQueryPage.firstPage_sure_button.click()
        else:
            print('go on!')

        detailQueryPage.firstPage_accountmenu_button.click()
        sleep(1)
        lv = detailQueryPage.firstPage_yearlv_text.text
        strlv = "".join(lv)
        assert strlv.split('%')='0.35'
        #assert float(strlv.split('%'))/100 > 0

if __name__ == "__main__":
    pytest.main(['-v','-s','test_detailQuery.py'])

