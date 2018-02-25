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
from test_case.page_obj.ApproveChannelResultPage import ChannalResultApprovalPage
from test_case.page_obj.base import *
from data.TestData import Data
import time


class ServiceOrderTests(myunit.MyTest):
    global current_time
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    # 登录融管系统
    def user_login_verify(self, username="yanghongyuan", password="123456", city="suzhou"):
        login(self.driver).user_login(username, password, city)

    # 融服接单订单
    def test_0001_ApproveChannalResult(self):
        self.user_login_verify()
        chan_appr_page = ChannalResultApprovalPage(self.driver)
        chan_appr_page.approveChannalResult(Data.cmp_name)

        # self.assertEqual(my_order.search_by_fuzzy(), '需求书修改有限公司')
        functions.insert_img(self.driver, current_time + "__myOrder_fuzzysearch.png")
        chan_appr_page.close()