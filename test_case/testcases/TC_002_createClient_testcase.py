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
from test_case.page_obj.createClientPage import createClient
from test_case.page_obj.myClientsPage import myClient
from data.TestData import Data
import time


class createNewClient(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales, password="123456", city=Data.city):
        login(self.driver).user_login(username, password, city)

    # 测试创建客户-电话号码已经存在
    def aa_test_1_verify_mobileNo_isExist(self):
        self.user_login_verify()
        new_client = createClient(self.driver)
        new_client.setWaitTime(2)
        new_client.open_rapidOperation()
        new_client.open_newClient()
        new_client.switchToNewClientFrame()
        new_client.inputMobile('12589756835')
        new_client.checkMobileIsDuplicate()
        # self.assertEqual(new_client.check_num_isExist(), '该客户已经归属当前登录用户')
        functions.insert_img(self.driver, current_time + "__Client_isExist.png")
        new_client.close()

    #测试创建客户
    def test_2_create_newClient(self):
        self.user_login_verify()
        new_client = createClient(self.driver)
        new_client.setWaitTime(2)
        new_client.open_rapidOperation()
        new_client.open_newClient()
        new_client.switchToNewClientFrame()
        new_client.inputMobile(Data.lnk_moblie)
        new_client.checkMobileIsDuplicate()
        #self.assertEqual(new_client.check_num_isExist(), '验证通过')
        functions.insert_img(self.driver, current_time + "__Client_isNotExist.png")
        new_client.selectCltExeStatus()
        new_client.selectLoanArea()
        new_client.saveClient()
        time.sleep(1)
        functions.insert_img(self.driver, current_time + "__Client_isCreateSuccess.png")
        time.sleep(20)

        # #关闭创建页面，返回我的客户
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        # self.assertEqual(new_client.check_client_createSucess(), '')
        functions.insert_img(self.driver, current_time + "__CheckClient_isCreateSuccess.png")
        my_client.setWaitTime(2)
        my_client.close()



if __name__ == '__main__':
    unittest.main()


