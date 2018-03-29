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
from test_case.page_obj.RefundPage import RefundPage
from data.TestData import Data
import time


class RefundTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username=Data.sales, password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)

    # 顾问创建新退款
    def aa_test_1_createRefund_SALES(self):
        self.user_login_verify()
        my_client = myClient(self.driver)
        my_client.gotoMyClientList_All(Data.lnk_moblie)
        my_client.setWaitTime(2)
        self.assertEqual(my_client.search_by_fuzzy(), Data.cmp_name)
        functions.insert_img(self.driver, current_time + "__myClient_fuzzysearch.png")
        my_client.setWaitTime(2)

        refund = RefundPage(self.driver)
        refund.createRefund()
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #总监新退费审批
    def aa_test_2_approveRefund_Director(self):
        self.user_login_verify(username='pengxiaoli',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveRefund_Director(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #分总新退费审批
    def aa_test_3_approveRefund_DivManager(self):
        self.user_login_verify(username='renyuan',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveRefund_DivManager(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #分公司财务新退费审批
    def aa_test_4_approveRefund_Finance(self):
        self.user_login_verify(username='sunquan',password='123456',city='suzhou')

        refund = RefundPage(self.driver)
        refund.approveRefund_Finance(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #分公司财务新退费审批
    def aa_test_5_approveRefund_Accantant(self):
        self.user_login_verify(username='duanxuesa',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveRefund_Accountant(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #CFO新退费审批
    def aa_test_6_approveRefund_CFO(self):
        self.user_login_verify(username='lingju',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveRefund_CFO(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

    #总部付款出纳新退费审批
    def test_7_approveRefund_Cash(self):
        self.user_login_verify(username='yangshuai',password='123456',city='shanghai')

        refund = RefundPage(self.driver)
        refund.approveRefund_Cashier(Data.cmp_name)
        #self.assertEqual(my_client.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myClient_orderCreateCMP.png")
        refund.close()

if __name__ == '__main__':
    unittest.main()


