from time import sleep
import pytest
import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.mobileModify_page import MobileModifyPage

class Test_mobileModify:
    """个人信息修改 """

    def test_balanceQueryy_case(self,browser,base_url):
        """
        名称：个人信息修改
        步骤：
        1、打开浏览器,输入测试网址
        2、点击转账菜单按钮，跳转到转账录入页面
        3、输入账户，进入账户总览页面
        断言：
        检查页面中年利率是否反显年利率且大于0
        """
        mobileModifyPage = MobileModifyPage(browser)
        mobileModifyPage.get(base_url)
        sleep(2)
        if mobileModifyPage.basePage_alert:
            print('调试信息！')
            mobileModifyPage.basePage_sure_button.click()
        else:
            print('go on!')
        sleep(1)
        mobileModifyPage.menu_membermanager_button.click()
        sleep(1)

        '''首页'''
        mobileModifyPage.firstPage_personalmessage_link.click()
        sleep(1)
        mobileModifyPage.firstPage_mobilemodify_button.click()
        sleep(1)

        '''修改页'''
        newmobile = '13812457896'
        mobileModifyPage.secondPage_mobilemodify_input.send_keys(newmobile)
        mobileModifyPage.secondPage_save_button.click()
        sleep(1)

        '''确认页'''
        acctualmsg = mobileModifyPage.thirdPage_msuremobile_input.text
        assert acctualmsg == newmobile
        mobileModifyPage.thirdPage_msure_button.click()
        sleep(1)

        '''结果页'''
        assert '手机号修改已提交' in mobileModifyPage.result_msg.text

if __name__ == "__main__":
    pytest.main(['-v','-s','test_mobileModify.py'])

