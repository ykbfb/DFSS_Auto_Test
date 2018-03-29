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
#    pop_new_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
import time

class RefundPage(Page):
    # 合同管理
    contract_tab_loc = (By.XPATH,'//*[@id="bottomTabs_htgl"]/a')
    botom_frame_loc = 'bottomTabs_Content_Iframe'
    def clickContractTab(self):
        self.click_element(*self.contract_tab_loc)
        self.scrollToElement('id',self.botom_frame_loc) # 页面跳转到底部【客户详情】所在的位置--相当于滚动条
        self.switchToOneFrame(self.botom_frame_loc) # 切换到底部【客户详情】的iframe

    # 退款
    member_refund_loc = (By.PARTIAL_LINK_TEXT,"退款") #会员费退款按钮
    pop_new_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    def openRefundPage(self):
        self.click_element(*self.member_refund_loc)
        time.sleep(1)
        self.switchWindow()
        time.sleep(1)
        self.switchToOneFrameByXpath(self.pop_new_frame_loc)

    # 填写会员费退费
    refund_amt_loc = (By.ID,'refundAmount')#退款金额
    moveto_refund_amt_loc = 'refundAmount'
    bank_loc = (By.ID,'txtBank')#开户网点
    account_loc = (By.ID,'txtAccount')#银行账户
    material_loc = (By.ID,'ccb1')#资料
    refund_reason_loc = (By.ID,'txtRefundReason')#退款原因
    moveto_refund_reason_loc = 'txtRefundReason'
    submit_loc = (By.ID,'btnSub')#提交

    def inputRefundDetail(self):
        self.scrollToElement('id',self.moveto_refund_amt_loc)
        self.input_value(self.refund_amt_loc,100)
        self.input_value(self.bank_loc,'自动化测试：自动化测试银行茉莉花支行')
        self.input_value(self.account_loc,'8888888888888888888')
        self.click_element(*self.material_loc)
        self.scrollToElement('id',self.moveto_refund_reason_loc)
        self.input_value(self.refund_reason_loc,'自动化测试： 会员费退费')
        self.click_element(*self.submit_loc)
        time.sleep(1)
        self.close_alert()

    #顾问创建会员费退费
    def createRefund(self):
        self.clickContractTab()
        self.openRefundPage()
        self.inputRefundDetail()

#=====================================================================================================================
    #销售总监审批
    sales_manage_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]')#销售管理
    refund_apprv_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[17]/div/a/span[2]')#新退费审批--总监
    moveto_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[17]/div/a/span[2]'
    refund_apprv_frame_loc = '//*[@id="tabs"]/div[2]/div[2]/div/iframe'
    clt_name_loc = (By.ID,'clientOrLinkmanEq')#客户名称/联系人
    d_search_loc = (By.ID,'btnSearch')#查询
    approve_loc = (By.XPATH,'//*[@id="MyCltByPage"]/tbody/tr[2]/td[13]/input')#审批

    def approveRefund_Director(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.sales_manage_loc)
        self.scrollToElement('xpath',self.moveto_refund_loc)
        self.click_element(*self.refund_apprv_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.d_search_loc)
        time.sleep(1)
        self.click_element(*self.approve_loc)
        self.switchWindow()
        self.inputApproveDetail_Dir()


    #审批详情页
    refund_pop_frame_loc = "//iframe[contains(@id, 'layui-layer-iframe')]"
    apprv_memo_loc = (By.ID,'txtOpnion')#审批意见
    moveto_apprv_memo = 'txtOpnion'#审批意见
    dir_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[39]/td[2]/input[1]')#通过
    apprv_confirm_loc = (By.CLASS_NAME,'layui-layer-btn0')

    def inputApproveDetail_Dir(self):
        '''总监输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_apprv_memo)
        self.input_value(self.apprv_memo_loc,'自动化测试：审批新退费')
        self.click_element(*self.dir_appvpass_loc)
        self.switchWindow()
        self.click_element(*self.apprv_confirm_loc)

#=================================================================================================================
    #分总审批新退费
    div_sales_manage_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[1]/div[1]')#分总--【销售管理】
    moveto_div_refund_loc = '//*[@id="wnav"]/div[2]/div[2]/ul/li[17]/div/a/span[2]'#新退费审批
    div_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[2]/div[2]/ul/li[17]/div/a/span[2]')#

    def approveRefund_DivManager(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.div_sales_manage_loc)
        self.scrollToElement('xpath',self.moveto_div_refund_loc)
        self.click_element(*self.div_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.d_search_loc)
        time.sleep(1)
        self.click_element(*self.approve_loc)
        self.switchWindow()
        self.inputApproveDetail_Div()

    div_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[42]/td[2]/input[1]')#通过
    def inputApproveDetail_Div(self):
        '''分总输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_apprv_memo)
        self.input_value(self.apprv_memo_loc,'自动化测试：分总审批新退费')
        self.click_element(*self.div_appvpass_loc)
        self.switchWindow()
        self.click_element(*self.apprv_confirm_loc)

#=================================================================================================================
    #分公司财务审批新退费
    casher_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]')#出纳
    moveto_fin_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[13]/div/a/span[2]'
    fin_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[2]/ul/li[13]/div/a/span[2]')#新退费审批
    fin_apprv_loc = (By.XPATH,'//*[@id="MyCltByPage"]/tbody/tr[2]/td[14]/input')#审批

    def approveRefund_Finance(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.casher_menu_loc)
        self.scrollToElement('xpath',self.moveto_fin_refund_loc)
        self.click_element(*self.fin_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.d_search_loc)
        time.sleep(1)
        self.click_element(*self.fin_apprv_loc)
        self.switchWindow()
        self.inputApproveDetail_Fin()

    receipt_no_loc = (By.ID,'firstRefundToken') #收据编号
    moveto_receipt_no_loc = 'firstRefundToken'
    fin_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[46]/td[2]/input[1]')#通过
    def inputApproveDetail_Fin(self):
        '''分公司财务输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_receipt_no_loc)
        self.input_value(self.receipt_no_loc,'YYKK888')
        self.input_value(self.apprv_memo_loc,'自动化测试：分公司财务审批新退费')
        self.click_element(*self.fin_appvpass_loc)
        self.switchWindow()
        self.click_element(*self.apprv_confirm_loc)

#=============================================================================================
    #总部应收会计审批新退费
    accountant_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[3]/div[1]/div[1]')#付款专员
    moveto_acc_refund_loc = '//*[@id="wnav"]/div[3]/div[2]/ul/li[6]/div/a/span[2]'
    acc_refund_loc =(By.XPATH, '//*[@id="wnav"]/div[3]/div[2]/ul/li[6]/div/a/span[2]')#新退费申请

    def approveRefund_Accountant(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.accountant_menu_loc)
        self.scrollToElement('xpath',self.moveto_acc_refund_loc)
        self.click_element(*self.acc_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.d_search_loc)
        time.sleep(1)
        self.click_element(*self.fin_apprv_loc)
        self.switchWindow()
        self.inputApproveDetail_Acc()

    acc_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[48]/td[2]/input[1]')#通过
    def inputApproveDetail_Acc(self):
        '''总部应收会计输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_apprv_memo)
        self.input_value(self.apprv_memo_loc,'自动化测试：总部应收会计审批新退费')
        self.click_element(*self.acc_appvpass_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.apprv_confirm_loc)

#=============================================================================================
    #CFO审批新退费
    CFO_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[4]/div[1]/div[1]')#CFO
    CFO_refund_loc = (By.XPATH,'//*[@id="wnav"]/div[4]/div[2]/ul/li[8]/div/a/span[2]')#新退费审批

    def approveRefund_CFO(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.CFO_menu_loc)
        self.click_element(*self.CFO_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        time.sleep(1)
        self.click_element(*self.d_search_loc)
        time.sleep(1)
        self.click_element(*self.approve_loc)
        self.switchWindow()
        self.inputApproveDetail_CFO()

    CFO_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[51]/td[2]/input[1]')#通过
    def inputApproveDetail_CFO(self):
        '''分总输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_apprv_memo)
        self.input_value(self.apprv_memo_loc,'自动化测试：CFO审批新退费')
        self.click_element(*self.CFO_appvpass_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.apprv_confirm_loc)

#=============================================================================================
    #总部付款出纳审批新退费
    center_cashier_menu_loc = (By.XPATH,'//*[@id="wnav"]/div[5]/div[1]/div[1]')#钱智总部付款出纳
    cash_refund_loc =(By.XPATH, '//*[@id="wnav"]/div[5]/div[2]/ul/li[6]/div/a/span[2]')#新退费申请

    def approveRefund_Cashier(self,clt_name):
        self.clt_name = clt_name
        self.click_element(*self.center_cashier_menu_loc)
        self.click_element(*self.cash_refund_loc)
        self.setWaitTime(5)
        self.switchToOneFrameByXpath(self.refund_apprv_frame_loc)
        self.input_value(self.clt_name_loc,clt_name)
        self.click_element(*self.d_search_loc)
        time.sleep(1)
        self.click_element(*self.fin_apprv_loc)
        self.switchWindow()
        self.inputApproveDetail_Cash()

    cashier_appvpass_loc = (By.XPATH,'//*[@id="main"]/div[1]/table/tbody/tr[54]/td[2]/input[1]')#通过
    def inputApproveDetail_Cash(self):
        '''总部付款出纳输入审批意见'''
        self.switchToOneFrameByXpath(self.refund_pop_frame_loc)
        self.scrollToElement('id',self.moveto_apprv_memo)
        self.input_value(self.apprv_memo_loc,'自动化测试：总部付款出纳审批新退费')
        self.click_element(*self.cashier_appvpass_loc)
        self.switchWindow()
        time.sleep(1)
        self.click_element(*self.apprv_confirm_loc)
# ============================================================================================
    # 验证case的执行结果：  未完待续
