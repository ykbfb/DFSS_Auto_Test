#coding=utf-8
#-*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2017年5月12日

@author: Administrator
'''
#--==================================================================
#By 函数的属性：
#     ID = "id"
#     XPATH = "xpath"
#     LINK_TEXT = "link text"
#     PARTIAL_LINK_TEXT = "partial link text"
#     NAME = "name"
#     TAG_NAME = "tag name"
#     CLASS_NAME = "class name"
#     CSS_SELECTOR = "css selector"
#--==================================================================

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from .loginPage import login
from time import sleep


class callDetail(Page):            
    
    #记录详情
    record_detail_loc = (By.ID,"txtCallMemo")    
#     record_detail_loc = (By.XPATH,'//*[@id="txtCallMemo"]')
    
    #已将股权
    cmp_share_loc = (By.ID,'lbgq')
    #已加微信
    add_Wechat_loc = (By.ID,'lbIsWechatFriend')
    #未接听
    no_respone_loc = (By.XPATH,'//*[@id="customerDefaultMemo"]/div[1]')
    #忙碌中
    on_busy_loc = (By.XPATH,'//*[@id="customerDefaultMemo"]/div[2]')
    #暂无意向
    no_attempt_loc = (By.XPATH,'//*[@id="customerDefaultMemo"]/div[3]')
    #新增来访
    add_new_visit_loc = (By.ID,'btnAddInterview')
    #保存新增来访
    save_new_visit_loc = (By.ID,'btnSaveInterview')
    #来访时间
    visit_time_loc = (By.ID,'txtComing')
    #客户标签
    clt_flag_loc = (By.XPATH,'//*[@id="cltKeyWords"]/span[1]')
    #客户类型： 企业主
    clt_cmp_loc = (By.ID,'r1')        
    #客户类型： 个体户
    clt_personal_loc = (By.ID,'r2')  
    #客户类型： 工薪族
    clt_emp_loc = (By.ID,'r3')  
    #客户类型： 其他
    clt_other_loc = (By.ID,'r4')
    #需求额度
    required_amount_loc = (By.ID,'txtRequierMoney')
    #房产总额
    house_amount_loc = (By.ID,'txtHouseBuyAmount')      
    #车产总额
    car_amount_loc = (By.ID,'txtCarBuyAmount')
    #对公流水
    public_loc = (By.ID,'selToPublic')    
    #对私流水
    private_loc = (By.ID,'selToPrivate') 
    #有保单
    has_policy_loc  = (By.ID,'rbHasPolicy1')   
    #无保单
    no_policy_loc  = (By.ID,'rbHasPolicy2')     
    #保单有断缴
    stop_policy_loc = (By.ID,'rbHasStopPayPolicy1')
    #保单没有段缴
    no_stop_policy_loc = (By.ID,'rbHasStopPayPolicy2')
    #已缴纳月数
    policy_months_loc = (By.ID,'txtPolicyPaiedMonths')
    #保单每月缴纳金额
    policy_per_mon_loc = (By.ID,'txtPolicyPayAmountPerMonth')
    
    #保存按钮
    call_save_loc = (By.ID,'btnImgSave')
    #保存&下一通按钮
    call_save_next_loc = (By.ID,'btnNext')


    #记录详情
    def inputCallDetail(self,value):
        self.find_element(*self.record_detail_loc).send_keys(value)
    #已将股权
    def checkCompanyShare(self):
        self.find_element(*self.cmp_share_loc).click()    
    #已加微信
    def addWechat(self):
        self.find_element(*self.add_Wechat_loc).click() 
    #未接听
    def checkNoRespone(self):
        self.find_element(*self.no_respone_loc).click() 
    #忙碌中
    def checkOnBusy(self):
        self.find_element(*self.on_busy_loc).click() 
    #暂无意向
    def checkNoAttempt(self):
        self.find_element(*self.no_attempt_loc).click() 
    #新增来访
    def addNewVisit(self):
        self.find_element(*self.add_new_visit_loc).click() 
    #保存来访记录    
    def saveVisit(self): 
        self.find_element(*self.save_new_visit_loc).click()        
    #选择来访时间
    def setVisittime(self,t_id,visit_time_value):
        #将时间控件字段置为空
        jStr1 = "$('input[id=" 
        jStr2 = "]').attr('readonly',false)"
        js = jStr1 + s_id + jStr2      
        self.script(js)  
        self.find_element(*self.visit_time_loc).send_keys(visit_time_value)
    
    #客户标签
    def selectCltFlag(self):
        self.find_element(*self.clt_flag_loc).click()
    #客户类型：企业主
    def selectCltTpyeCMP(self):
        self.find_element(*self.clt_cmp_loc).click()
    #客户类型：个体户
    def selectCltPerson(self):
        self.find_element(*self.clt_personal_loc).click()
    #客户类型：工薪族
    def selectCltEMP(self):
        self.find_element(*self.clt_emp_loc).click()
    #客户类型：其他
    def selectCltOther(self):
        self.find_element(*self.clt_other_loc).click()
    #需求额度
    def inputRequiredAmt(self,r_value):
        self.find_element(*self.required_amount_loc).send_keys(r_value)
    #房产总额
    def inputHouseAmt(self,h_value):
        self.find_element(*self.house_amount_loc).send_keys(h_value)    
    #车产总额
    def inputCarAmt(self,c_value):
        self.find_element(*self.car_amount_loc).send_keys(c_value)
        
    #对公流水    
    def getToPublic(self,pub_index): 
        option=self.find_element(*self.public_loc)
        Selection(option).select_by_index(pub_index)
    #对私流水    
    def getToPrivite(self,pri_index): 
        option=self.find_element(*self.private_loc)
        Selection(option).select_by_index(pri_index)       

    #有保单
    def getHasPolicy(self):
        self.find_element(*self.has_policy_loc).click()
    #无保单
    def getNoPolicy(self):
        self.find_element(*self.no_policy_loc).click()
    #保单有断缴
    def getStopPolicy(self):
        self.find_element(*self.stop_policy_loc).click()        
    #保单无断缴
    def getStopPolicy(self):
        self.find_element(*self.no_stop_policy_loc).click()
    #已缴保单月数
    def inputPolicyMonths(self,m_value):
        self.find_element(*self.policy_months_loc).send_keys(m_value) 
    #保单每月缴纳金额
    def inputPolicyPerAmt(self,per_value):
        self.find_element(*self.policy_per_mon_loc).send_keys(per_value) 

    #保存通话记录
    def saveCallDetail(self):
        self.find_element(*self.call_save_loc).click()    
    #保存并拨打下一通
    def saveCallAndNext(self):
        self.find_element(*self.call_save_next_loc).click()    
    
    
    #双击选中的客户: 打开拨打详情
    def dubleClickClient(self):
        clt_call_detail=self.find_element(*self.duble_click_search_loc)
        ActionChains(self.driver).double_click(clt_call_detail).perform()  #双击
    #修改客户
    def modifyClient(self):
        modify = self.find_element(*self.duble_click_search_loc) 
        ActionChains(self.driver).context_click(modify).perform() #右击
        self.find_element(*self.modify_loc).click()         
    
    #选中右键操作       
    
#--===========================================================================================
    #初始化拨打详情页面
    def init_callDetailPage(self,frame1='//*[@id="tabs"]/div[2]/div[2]/div/iframe',frame2='//*[@id="HomePage_ReMake_TPCltCall_Id"]',value = '',t_id='',visit_time_value='',r_value='',h_value='',c_value='',pub_index='',pri_index='',m_value='',per_value=''):
        self.switchFrame(frame1,frame2)
#         self.switchWindow()
        self.inputCallDetail(value)
        self.checkCompanyShare()
        self.addWechat()
        self.checkNoRespone()
        self.checkOnBusy()
        self.checkNoAttempt()
        self.addNewVisit()
        self.saveVisit()
        #选择来访时间
        self.setVisittime(t_id,visit_time_value)
        self.selectCltFlag()
        #客户类型：企业主
        self.selectCltTpyeCMP()

        #客户类型：个体户
        self.selectCltPerson()
        #客户类型：工薪族
        self.selectCltEMP()
        #客户类型：其他
        self.selectCltOther()

        #需求额度
        self.inputRequiredAmt(r_value)

        #房产总额
        self.inputHouseAmt(h_value)
   
        #车产总额
        self.inputCarAmt(c_value)

        #对公流水    
        self.getToPublic(pub_index)
        #对私流水    
        self.getToPrivite(pri_index)   

        #有保单
        self.getHasPolicy()

        #无保单
        self.getNoPolicy()

        #保单有断缴
        self.getStopPolicy()
     
        #保单无断缴
        self.getStopPolicy()

        #已缴保单月数
        self.inputPolicyMonths(m_value)
    
        #保单每月缴纳金额
        self.inputPolicyPerAmt(per_value)


        #保存通话记录
        self.saveCallDetail()
     
        #保存并拨打下一通
        self.saveCallAndNext()
  
        self.driver.implicitly_wait(10)
        
    
    #验证case的执行结果    
    user_login_success_loc = (By.XPATH,'//*[@id="Main_Page"]/div[1]/div/div/span[2]/label') 
    
    #登录成功
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
   