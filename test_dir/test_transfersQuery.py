"""
@author:  张强
@data: 2020-4-20
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.transfersQuery_page import TransfersQueryPage


class Test_transfersQuery:
    """批量查询"""

    def test_transfersQuery_case(self, browser, base_url):
        """
        名称：批量查询
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        transfersQueryPage = TransfersQueryPage(browser)
        transfersQueryPage.get(base_url)
        sleep(1)
        if transfersQueryPage.basePage_alert:
            print('调试信息！')
            transfersQueryPage.basePage_sure_button.click()
        else:
            print('go on!')

        transfersQueryPage.menu_batch_button.click()
        sleep(1)

        transfersQueryPage.firstPage_transfersQuery_button.click()
        sleep(1)

        '''批量类型'''
        transfersQueryPage.firstPage_trstype_combox.click()
        trstypes = transfersQueryPage.firstPage_trstype_comboxs
        for i in range(0,len(trstypes)):
            if trstypes[i].text =='批量代发':
                trstypes[i].click()
                break
        sleep(1)
        '''交易渠道'''
        transfersQueryPage.firstPage_trschannel_combox.click()
        trschannels = transfersQueryPage.firstPage_trschannel_comboxs
        for j in range(0, len(trschannels)):
            if trschannels[j].text == '企业网银':
                trschannels[j].click()
                break
        sleep(1)
        '''处理状态'''
        transfersQueryPage.firstPage_trsstatus_combox.click()
        trsstatus = transfersQueryPage.firstPage_trsstatus_comboxs
        for k in range(0, len(trsstatus)):
            if trsstatus[k].text == '成功':
                trsstatus[k].click()
                break
        sleep(1)
        '''日期操作'''
        dates = transfersQueryPage.firstPage_date_combox
        dates[0].click()
        sleep(1)
        startdates = transfersQueryPage.firstPage_startdate_tables
        for l in range(0,len(startdates)):
            if startdates[l].get_attribute("title") == "2016年1月7日":
                startdates[l].click()
        sleep(1)

        dates[1].click()
        sleep(1)
        enddates = transfersQueryPage.firstPage_enddate_tables
        endclick = []
        for s in range(0, len(enddates)):
            if enddates[s].get_attribute("title") == "2016年1月9日":
                endclick.append(enddates[s])
        endclick[1].click()
        sleep(1)
        transfersQueryPage.firstPage_query_button.click()
        sleep(1)
        transfersQueryPage.firstPage_download_label.click()
        transfersQueryPage.firstPage_download_link.click()
        sleep(1)
        hl = browser.current_window_handle
        handles = browser.window_handles
        for p in range(0,len(handles)):
            if handles[p] != hl:
                browser.switch_to_window(handles[p])
                break

        '''下载页'''
        transfersQueryPage.secondPage_accountno_input.send_keys("111")
        transfersQueryPage.secondPage_accountame_input.send_keys("222")
        transfersQueryPage.secondPage_query_button.click()
        sleep(1)
        transfersQueryPage.secondPage_download_button[0].click()
        sleep(1)

        '''结果确认页面'''
        hln = browser.current_window_handle
        handlesn = browser.window_handles
        for h in range(0, len(handlesn)):
            if handlesn[h] != hl and handlesn[h] != hln:
                browser.switch_to_window(handlesn[h])
                break
        transfersQueryPage.thirdPage_sure_button.click()
        sleep(1)

        '''结果页面'''
        assert '电子回单下载申请成功' in transfersQueryPage.fourthPage_msg.text


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_detailQuery.py"])
