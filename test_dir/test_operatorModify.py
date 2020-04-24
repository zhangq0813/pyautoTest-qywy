"""
@author:  张强
@data: 2020-4-23
"""
import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.operatorModify_page import OperatorModifyPage


class Test_operatorModify:
    """操作员管理"""

    def test_operatorModify_case(self, browser, base_url):
        """
        名称：操作员管理
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        operatorModifyPage = OperatorModifyPage(browser)
        operatorModifyPage.get(base_url)
        sleep(1)
        if operatorModifyPage.basePage_alert:
            print('调试信息！')
            operatorModifyPage.basePage_sure_button.click()
        else:
            print('go on!')

        '''进入菜单'''
        operatorModifyPage.menu_membermanager_button.click()
        sleep(1)
        operatorModifyPage.firstPage_OperatorManage_link.click()
        sleep(1)

        '''选择数据点击修改'''
        primarylist = operatorModifyPage.firstPage_primary_links
        for i in range(0,len(primarylist)):
            if '226640000053663162631' in primarylist[i].get_attribute("data-reactid"):
                primarylist[i].click()
                break
        sleep(1)
        operatorModifyPage.firstPage_modify_link.click()
        sleep(1)

        '''修改页面'''
        '''基础权限，只勾选录入权限'''
        inlinelist = operatorModifyPage.secondPage_inline_checkbox
        if inlinelist[0].get_attribute("class") == 'ant-checkbox':
            inlinelist[0].click()
        if inlinelist[1].get_attribute("class") != 'ant-checkbox':
            inlinelist[1].click()



        status = inlinelist[0].is_selected()
        status1 = inlinelist[1].is_selected()
        #status2 = inlinelist[2].is_selected()

        sleep(1)
        billCheckPage.firstPage_billcheck_button.click()
        sleep(1)
        '''下面操作错误，list[1]操作后，共有属性变化，原来list[3]会变成list[4]'''
        #billCheckPage.firstPage_check_list[1].click()
        #billCheckPage.firstPage_check_list[3].click()

        '''切换窗体'''
        hl = browser.current_window_handle
        handles = browser.window_handles
        for i in range(0,len(handles)):
            if handles[i] != hl:
                browser.switch_to_window(handles[i])
                break
        sleep(1)
        '''批量操作页'''
        billCheckPage.secondPage_reject_index.click()
        billCheckPage.secondPage_rejecttxt_index.send_keys("1234565")
        billCheckPage.secondPage_verifycode_button.click()
        billCheckPage.secondPage_verifycode_input.send_keys("123456")
        billCheckPage.secondPage_next_button.click()
        sleep(1)

        '''结果页面'''
        assert '工单审批提交成功' in billCheckPage.thirdPage_result_msg.text


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_billCheck.py"])
