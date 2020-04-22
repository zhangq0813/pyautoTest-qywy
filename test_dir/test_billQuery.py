"""
@author:  张强
@data: 2020-4-23
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.billQuery_page import BillQueryPage


class Test_billQuery:
    """工单查询"""

    def test_billQuery_case(self, browser, base_url):
        """
        名称：工单查询
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        billQueryPage = BillQueryPage(browser)
        billQueryPage.get(base_url)
        sleep(1)
        if billQueryPage.basePage_alert:
            print('调试信息！')
            billQueryPage.basePage_sure_button.click()
        else:
            print('go on!')

        billQueryPage.menu_bills_button.click()
        sleep(1)

        billQueryPage.firstPage_billquery_link.click()
        sleep(1)

        '''审批状态'''
        billQueryPage.firstPage_status_combox.click()
        status = billQueryPage.firstPage_status_comboxs
        for i in range(0,len(status)):
            if status[i].text =='成功':
                status[i].click()
                break
        sleep(1)

        '''日期操作'''
        dates = billQueryPage.firstPage_date_comboxs
        dates[0].click()
        sleep(1)
        startdates = billQueryPage.firstPage_startdate_tables
        for l in range(0,len(startdates)):
            if startdates[l].get_attribute("title") == "2016年1月7日":
                startdates[l].click()
        sleep(1)

        dates[1].click()
        sleep(1)
        enddates = billQueryPage.firstPage_enddate_tables
        endclick = []
        for s in range(0, len(enddates)):
            if enddates[s].get_attribute("title") == "2016年1月9日":
                endclick.append(enddates[s])
        endclick[1].click()
        sleep(1)
        billQueryPage.firstPage_query_button.click()
        sleep(1)

        '''结果页面'''
        assert len(billQueryPage.secondPage_result_list) > 0


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_billQuery.py"])
