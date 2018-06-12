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
# --==================================================================

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
import time

class SaleseOrderAsignPage(Page):
    # 销售经理邀约审批
    sales_nav_loc = (By.XPATH,'//*[@id="wnav"]/div[4]/div[1]/div[1]') #销售管理
    sales_order_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[4]/div[2]/ul/li[4]/div/a/span[2]')#销售订单处理操作
    salseorder_list_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    sal_order_accpt_loc = (By.XPATH,'//*[@id="main"]/ul/li[1]') #待接单
    clt_name_loc = (By.ID,'txtCusInfo') #客户查询
    search_btn_loc = (By.XPATH,'//*[@id="main"]/form/div/div/div[2]/input[2]')#查询
    accpt_btn_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[10]/input[1]') #接单
    confirm_btn_loc = (By.CLASS_NAME,'layui-layer-btn0')#弹窗确认

    def gotoSalesOrderNeedAccptlist(self):
        '''销售订单待接单列表页'''
        self.click_element(*self.sales_nav_loc)
        self.click_element(*self.sales_order_menu_loc)
        self.setWaitTime(20)
        time.sleep(1)
        self.switchToOneFrameByXpath(self.salseorder_list_frame_loc)

#======================================================================================
    #待接单页面
    def getSalseOrder(self,value):
        self.value = value
        self.click_element(*self.sal_order_accpt_loc)
        self.input_value(self.clt_name_loc,value)
        self.click_element(*self.search_btn_loc)
        time.sleep(1)
        self.click_element(*self.accpt_btn_loc)
        self.switchWindow()
        self.click_element(*self.confirm_btn_loc)
    #接单
    def acceptSalseOrder(self,clt_name):
        self.clt_name = clt_name
        self.gotoSalesOrderNeedAccptlist()
        self.getSalseOrder(clt_name)
#================================================================================
    need_asign_tab_loc = (By.XPATH,'//*[@id="main"]/ul/li[2]')#待派单
    asign_odr_loc = (By.XPATH,'//*[@id="myTb"]/tbody/tr[2]/td[10]/input')#派单
    asg_detail_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    select_serv_mgr_loc = (By.ID,'chk0')#选择条线融服经理
    sel_reason_loc = (By.ID,'txtAssignReason0')#选择原因
    submit_btn_loc = (By.ID,'btnSubmit')#提交
    sub_comfirm_btn_loc = (By.CLASS_NAME,'layui-layer-btn0')

    #待派单
    def getNeedAsignSalseOrder(self,value):
        self.value = value
        self.click_element(*self.need_asign_tab_loc)
        self.input_value(self.clt_name_loc,value)
        self.click_element(*self.search_btn_loc)
        time.sleep(1)
        self.click_element(*self.asign_odr_loc)
        self.switchWindow()
        self.switchToOneFrameByXpath(self.asg_detail_frame_loc)
        self.click_element(*self.select_serv_mgr_loc)
        self.input_value(self.sel_reason_loc,'自动化测试：选择融服经理--企业')
        self.click_element(*self.submit_btn_loc)
        self.switchWindow()
        self.click_element(*self.sub_comfirm_btn_loc)

    #派单
    def asignSalesOrder(self,clt_name):
        self.clt_name = clt_name
        self.gotoSalesOrderNeedAccptlist()
        self.getNeedAsignSalseOrder(clt_name)

# ============================================================================================
    # 验证case的执行结果：  未完待续
