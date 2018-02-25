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

class NewContractPage(Page):
    # 合同管理
    contract_tab_loc = (By.XPATH,'//*[@id="bottomTabs_htgl"]/a')
    botom_frame_loc = 'bottomTabs_Content_Iframe'
    def clickContractTab(self):
        self.find_element(*self.contract_tab_loc).click()
        self.scrollToElement('id',self.botom_frame_loc) # 页面跳转到底部【客户详情】所在的位置--相当于滚动条
        self.switchToOneFrame(self.botom_frame_loc) # 切换到底部【客户详情】的iframe

    # 创建及输入合同详情
    newContract_loc = (By.ID,'span4')    #新合同
    createNewContract_loc = (By.ID,'btnCreateContract')  #创建合同
    contract_frame_loc = '//*[@id="layui-layer-iframe3"]' #创建合同页面的frame
    def openNewContractPage(self):
        self.find_element(*self.newContract_loc).click()
        self.setWaitTime(20)
        self.find_element(*self.createNewContract_loc).click()
        self.switchWindow()
        self.switchToOneFrame2(self.contract_frame_loc)

    #输入合同详情
    VIP_contract_type_loc = (By.ID,'contractType1') #债权会员合同
    BPO_contract_type_loc = (By.ID,'contractType2') #债权外包合同
    contract_code_loc = 'selContract'#合同号
    def inputContractDetail_VIP(self,index=0):
        self.index = index
        self.find_element(*self.VIP_contract_type_loc).click()
        self.getDropdownMenu3(self.contract_code_loc,index)

    def inputContractDetail_BPO(self,index=0):
        self.index = index
        self.find_element(*self.BPO_contract_type_loc).click()
        self.getDropdownMenu3(self.contract_code_loc,index)

    #选择合同客户名称
    contract_name_loc = 'selType'
    def selectContractName(self,index=0):
        self.index = index
        self.getDropdownMenu3(self.contract_code_loc,index)

    #预估额度
    predit_loanAmt_loc = (By.ID,'txtPreditAmount')
    def inputPreLoanAmt(self,value=100):
        self.value = value
        self.find_element(*self.predit_loanAmt_loc).clear()
        self.find_element(*self.predit_loanAmt_loc).send_keys(value)

    #意向金
    intention_Amt_loc = (By.ID,'txtFee')
    def inputIntentionAmt(self,value=5000):
        self.value = value
        self.find_element(*self.intention_Amt_loc).clear()
        self.find_element(*self.intention_Amt_loc).send_keys(value)

    #输入合同起始日期
    contract_startDate_loc = 'txtServiceStart'
    def selectConStartDate(self,value='2018-01-20'):
        self.value = value
        self.getDateTimePicker(self.contract_startDate_loc,value)

    #备注
    contract_memo_loc = (By.ID,'txtMemo')
    def inputContractMo(self,value='测试创建新合同!'):
        self.value = value
        self.find_element(*self.contract_memo_loc).clear()
        self.find_element(*self.contract_memo_loc).send_keys(value)

    #上传合同附件
    getWay = 'id'
    elem1 = 'btnUpFile'
    elem2 = 'btnUpFile2'
    elem3 = 'btnUpFile3'
    file_path = 'F:\PyhtonTest\girl.jpg'
    uploadBtn = (By.ID,'btnUp')
    uploadBtn2 = (By.ID, 'btnUp2')
    uploadBtn3 = (By.ID, 'btnUp3')
    def uploadContractFile(self):
        self.uploadFile(self.getWay,self.elem1,self.file_path)  # 特批事项附件
        self.find_element(*self.uploadBtn).click()
        self.setWaitTime(30)
        self.uploadFile(self.getWay,self.elem2,self.file_path)  # 营业执照/法人资料附件
        self.find_element(*self.uploadBtn2).click()
        self.setWaitTime(30)
        self.uploadFile(self.getWay,self.elem3,self.file_path)  # 合同原件附件
        self.find_element(*self.uploadBtn3).click()
        self.setWaitTime(30)

    #提交合同
    save_loc = (By.ID,'btnSave')
    def submitContract(self):
        self.find_element(*self.save_loc).click()

#=============================================================================================================================================
#====转会员
    popWinMax_loc = (By.XPATH,'//*[@id="layui-layer3"]/span[1]/a[2]')
    change_VIPContract_loc = (By.PARTIAL_LINK_TEXT,"转会员") #转会员按钮
    def openChangeToVIPContract(self):
        self.find_element(*self.newContract_loc).click()
        self.find_element(*self.change_VIPContract_loc).click()
        self.switchWindow()
        # self.find_element(*self.popWinMax_loc).click()
        # self.switchToOneFrame2(self.contract_frame_loc)


#==============================================================================================================================================
#==============================================================================================================================================

    # 创建会员合同
    def createVIPContract(self):
        self.clickContractTab()
        self.openNewContractPage()
        self.inputContractDetail_VIP()
        self.selectContractName()
        self.selectConStartDate()
        self.inputPreLoanAmt()
        self.inputContractMo()
        self.uploadContractFile()
        self.submitContract()
        time.sleep(3)
        self.close_alert()

    # 创建外包合同
    def createBPOContract(self):
        self.clickContractTab()
        self.openNewContractPage()
        self.inputContractDetail_BPO()
        self.selectContractName()
        self.selectConStartDate()
        self.inputPreLoanAmt()
        self.inputIntentionAmt()
        self.inputContractMo()
        self.uploadContractFile()
        self.submitContract()
        time.sleep(3)
        self.close_alert()


    # 外包合同转会员
    def BPOContractTransToVIP(self):
        self.clickContractTab()
        self.openChangeToVIPContract()
        self.selectContractName()
        self.selectConStartDate()
        self.inputPreLoanAmt()
        self.inputContractMo()
        self.uploadContractFile()
        self.submitContract()
        time.sleep(3)
        self.close_alert()

# ============================================================================================
    # 验证case的执行结果：  未完待续
