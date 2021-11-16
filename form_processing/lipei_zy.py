# -*- encoding: utf-8 -*-
'''
@File    :   lipei_zy.py
@Time    :   2021/11/16 13:30:42
@Author  :   James 
@Desc    :   处理理赔自营数据
@Version :   1.0
'''

import pandas as pd
import numpy as np
from functools import reduce
def process(file):
    df = pd.read_excel(file,sheet_name="Sheet")
    ill_info = df['疾病'].str.partition("|",expand=True)
    ill_info.columns = ['ICD10','分隔符','疾病名称']
    del ill_info['分隔符']
    df1 = pd.concat([ill_info,df['赔案件数'],df['预估金额']],axis=1)
    df1.to_excel('自营.xlsx', sheet_name='Sheet1',index=None)
    jb_info = df1.groupby(by='ICD10')['疾病名称'].apply(lambda x:'.'.join(x)).reset_index()
    # 处理合并后
    jb_info = jb_info['疾病名称'].str.partition('.',expand=True)
    ill_info.columns = ['ICD10','分隔符','疾病名称']
    je_info = df1.groupby(by='ICD10')['预估金额'].sum().reset_index()
    js_info = df1.groupby(by='ICD10')['赔案件数'].sum().reset_index()
    dfs = [jb_info,je_info,js_info]
    df_final = reduce(lambda left,right: pd.merge(left,right,how='inner',on="ICD10"), dfs)
    # 按照案件数排序
    df_final = df_final.sort_values(by=['赔案件数'],ascending=False)
    df_final.to_excel('自营.xlsx', sheet_name='Sheet2',index=None)

def main():
    process("C:\\Users\\CPIC\\Desktop\\自营数据明细bak.xlsx")

if __name__ == '__main__':
    main()
