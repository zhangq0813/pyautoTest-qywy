"""
@author:  张强
@data: 2020-4-20
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.detailQuery_page import DetailQueryPage


class Test_detailQuery:
    """交易明细查询"""

    def test_detailQuery_case(self, browser, base_url):
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
        detailQueryPage = DetailQueryPage(browser)
        detailQueryPage.get(base_url)
        sleep(1)
        if detailQueryPage.basePage_alert:
            print('调试信息！')
            detailQueryPage.basePage_sure_button.click()
        else:
            print('go on!')

        detailQueryPage.menu_account_button.click()
        sleep(1)

        detailQueryPage.firstPage_detailquery_link.click()
        sleep(1)
        '''起始时间'''
        detailQueryPage.secondPage_startDate_button.click()
        sleep(1)
        startdates = detailQueryPage.secondPage_startDate_table_buttons
        sevendates = []
        for i in range(0,len(startdates)):
            if startdates[i].get_attribute("title") == "2016年1月7日":
                sevendates.append(startdates[i])
        sevendates[0].click()

        '''结束时间'''
        detailQueryPage.secondPage_endDate_button.click()
        enddates = detailQueryPage.secondPage_endDate_table_buttons
        ninedates = []
        for j in range(0, len(enddates)):
            if enddates[j].get_attribute("title") == "2016年1月9日":
                ninedates.append(enddates[j])
        ninedates[1].click()

        '''交易类型'''
        detailQueryPage.secondPage_trsType_index.click()
        trstypes = detailQueryPage.secondPage_trsType_indexs
        for k in range(0,len(trstypes)):
            if "结息" in trstypes[k].text:
                trstypes[k].click()
                break
        detailQueryPage.secondPage_query_button.click()
        sleep(1)

        '''结果列表取第一条点击详情'''
        dolinks = detailQueryPage.list_dolinks
        dolinks[0].click()
        sleep(1)
        '''对话框取值'''
        assert detailQueryPage.list_msgs[0].text == '8888 8880 3184 5595'



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_detailQuery.py"])
