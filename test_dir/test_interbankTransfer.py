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
from page.interbankTransfer_page import InterBankTransferpage

class Test_test_peerTransfer:
    """
    测试跨行转账
    """
    def test_peerTransfer_case(self,browser,base_url):
        """
        名称：跨行转账
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入跨行收款账户、收款人姓名、转账金额，点击下一步，进入转账确认页面
        4、点击获取验证码按钮，并输入收到得正确验证码，点击确定
        5、跳转到转账成功页面
        断言：
        检查页面是否包含返回按钮
        """
        interBankTransferPage = InterBankTransferpage(browser)
        interBankTransferPage.get(base_url)
        sleep(2)
        if interBankTransferPage.firstPage_alert:
            print('调试信息！')
            interBankTransferPage.firstPage_sure_button.click()
        else:
            print('go on!')

        interBankTransferPage.firstPage_menu_button.click()
        interBankTransferPage.firstPage_intermenu_button.click()
        sleep(1)

        interBankTransferPage.firstPage_transaccount_input.send_keys("6214855510376144")
        interBankTransferPage.firstPage_transname_input.send_keys("张三")
        interBankTransferPage.firstPage_transbank_index.click()
        sleep(1)
        '''获取下拉框中值'''
        #indexlist = browser.find_elements_by_xpath("//ul/li[@role='menuitem']")
        indexlist = interBankTransferPage.firstPage_transbank_indexs
        try:
            len(indexlist) > 0
            for i in range(0,len(indexlist)):
                if indexlist[i].text in "中国银行":
                    indexlist[i].click()
                    break
        except:
            print("银行列表下拉框中未匹配到值！")
        finally:
            print("执行成功")
        sleep(2)

        interBankTransferPage.firstPage_yhwd_button.click()
        sleep(1)

        '''弹框dialog定位及操作'''
        #browser.switch_to_alert  #排除不是alert弹框
        #browser.switch_to_default_content()  #排除不是焦点问题，不一定
        #handles = browser.window_handles     #排除不是一个window

        interBankTransferPage.secendPage_yhwdkey_input.click()
        interBankTransferPage.secendPage_yhwdkey_input.send_keys("123")
        interBankTransferPage.secendPage_yhwdkey_button.click()
        sleep(1)
        yhwdlist = interBankTransferPage.secendPage_yhwdkeyvalue_indexs
        try:
            len(yhwdlist) > 0
            for i in range(0,len(yhwdlist)):
                if "杭州市城东支行" in yhwdlist[i].text:
                    yhwdlist[i].click()
                    exceptvalue = yhwdlist[i].text  #必须再下面操作步骤之前，下面步骤点击后会跳出当前页面，如果再执行会导致获取不到值
                    interBankTransferPage.secendPage_yhwdsure_button.click()
                    #print(exceptvalue)
                    break
        except:
            print("网点查询下拉框中未匹配到值！")
        finally:
            sleep(1)
            acctualvalue = interBankTransferPage.secendPage_yhwdkey_result.text
            assert acctualvalue == exceptvalue

        interBankTransferPage.firstPage_trsamount_button.send_keys("100")
        '''选择转账方式（单选框）'''
        transtypes = interBankTransferPage.firstPage_trsamount_types
        transtypes[1].click()
        interBankTransferPage.firstPage_trsamount_index.click()
        sleep(1)
        ytlists = interBankTransferPage.firstPage_trsamount_indexs
        ytlists[1].click()
        '''
        for i in range(0,len(ytlists)):
            if "往来款" in ytlists[i].text:
                ytlists[i].click()
                break
        '''
        sleep(1)
        interBankTransferPage.firstPage_next_button.click()






if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_interbankTransfer.py"])