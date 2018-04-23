# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2018-01-04
@author: Administrator
'''
import unittest, sys

sys.path.append("./model")
sys.path.append("./page_obj")
from test_case.models import myunit, functions
from test_case.page_obj.loginPage import login
from test_case.page_obj.myClientsPage import myClient
from test_case.page_obj.createIntviewPage import NewIntviewPage
from data.TestData import Data
import time


class ContractTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales, password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)


    # 创建已来访邀约
    def AA_test_0001_createIntview(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)

        intview_page = NewIntviewPage(self.driver)
        intview_page.createIntview()
        # self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__createIntview.png")
        my_client.close()

    # 创建DC访邀约
    def test_0002_createIntview_DC(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)

        intview_page = NewIntviewPage(self.driver)
        intview_page.createIntview_DC()
        # self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__createDCIntview.png")
        my_client.close()

    # 修改邀约
    def test_0003_modifyIntview(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)

        intview_page = NewIntviewPage(self.driver)
        intview_page.modifyIntview()
        # self.assertEqual(my_client.search_by_fuzzy(),'大坤哥自动化')
        functions.insert_img(self.driver, current_time + "__modifyIntview.png")
        my_client.close()


if __name__ == '__main__':
    unittest.main()

