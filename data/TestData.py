# coding=utf-8
# -*- conding=utf-8 -*-
# encoding: utf-8

'''
Created on 2018-01-04
@author: Administrator
'''
import random

class Data:

    lnk_moblie = '10000000076'
    cmp_name = '需求书修改有限公司76'

    #合同打回、作废原因
    ctr_reject_memo = '自动化测试打回合同'
    ctr_discar_memo = '自动化测试作废合同'
    ContractCode = 'WB05122017000329'

    #意向单
    org_name = '平安普惠'
    prd_name = '车主贷'
    credit_manager = '张安林'

    #融资喜报审批
    chanl_clt_name = '需求书修改有限公司'
    fin_clt_name = 'AAC16110700195有限公司'

    #客户释放公海
    share_phone1 = random.randint(10000000000, 19999999999)
    share_phone2 = random.randint(10000000000, 19999999999)
    share_phone3 = random.randint(10000000000, 19999999999)

    #删除客户
    delete_phone1 = random.randint(10000000000, 19999999999)
    delete_phone2 = random.randint(10000000000, 19999999999)

    #划转至大项目部
    move_client_phone = random.randint(10000000000, 19999999999)