# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

# --==================================================================
# By 函数的属性：
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"
#---------------------------------------------------------------------
#定位动态id、name元素
# driver.find_element_by_xpath("//iframe[contains(@id, 'layui-layer-iframe')]")
# driver.find_element_by_xpath("//div[starts-with(@id, 'btn-attention')]")
# driver.find_element_by_xpath("//div[ends-with(@id, 'btn-attention')]")
# --==================================================================

from selenium.webdriver.common.by import By
from .base import Page
import time

class ChannalResultApprovalPage(Page):
    #融资订单管理
    loanmanage_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]') #融资管理
    channalresult_appr_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[5]/div/a/span[2]')#融资喜报审批
    chan_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    channalresult_cmpname_loc = (By.ID,'querycode')#按客户名称、联系人姓名
    chan_search_loc = (By.ID,'Button4')

    #放款喜报（总监）-待审批
    def approveChannalResult(self,value):
        self.value = value
        self.click_element(*self.loanmanage_nav_loc)
        self.waitElmentUntill(10,self.channalresult_appr_loc)
        self.click_element(*self.channalresult_appr_loc)
        self.switchToOneFrame2(self.chan_frame_loc)
        self.waitElmentUntill(20,self.channalresult_cmpname_loc)
        self.input_value(self.channalresult_cmpname_loc,value)
        self.click_element(*self.chan_search_loc)



