import xlrd,sys
import os, ast
import unittest
from loguru import logger
from config import globalparam
import inspect
from pprint import pprint


PATH = globalparam.data_path  # 运行配置

def get_excel_dict(path, index=0):
    paralList={}
    dirs = os.listdir(path)
    for filename in dirs:
        workbook=xlrd.open_workbook(os.path.join(globalparam.data_path,filename))  # 打开文件
        sheet=workbook.sheets()[index]  # sheet索引从0开始
        firstRowDataList=sheet.row_values(0)#第一行数据
        file_dict = []
        for rownum in range(1, sheet.nrows):#循环每一行数据
            list = sheet.row_values(rownum)
            dict={}
            dictTestCaseName={}
            for caseData in list:
                dict[firstRowDataList[list.index(caseData)]] =caseData #每一行数据与第一行数据对应转为字典
                #json.dumps(json.loads(caseData), ensure_ascii=False)
            dictTestCaseName[list[0]] = dict#转为字典后与用例名字对应转为字典
            file_dict.append(dictTestCaseName)
        paralList[filename.split('.')[0]] = file_dict#将处理后的数据放入列表里
    return paralList

def get_test_case_data(data_info, model,testCaseName):
    testData = data_info[model]
    getTestCaseDatalist = []
    for data in testData:
        if (list(data.keys())[0]) == testCaseName:
            getTestCaseDatadict = {}
            getTestCaseDatadict['data'] = ast.literal_eval(data[testCaseName]['data'])
            getTestCaseDatadict['assertion'] =  ast.literal_eval(data[testCaseName]['assertion'])
            getTestCaseDatadict['case_name'] = data[testCaseName]['case_name']
            getTestCaseDatalist.append(getTestCaseDatadict)
    return getTestCaseDatalist

if  os.path.exists(PATH):  # 如果路径不存在，创建路径
    data_info = get_excel_dict(PATH)
else:
    data_info = None
# pprint(get_excel_dict(PATH))
a = get_excel_dict(PATH)


