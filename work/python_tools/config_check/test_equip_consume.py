import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
import unittest
import configparser

def test_equip_consume():
    qian_equip_consume_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Equipment\EquipConfig.txt"
    hou_equip_consume_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\equipment_info.cfg"

    qian_equip_consume_file = r"D:\python_tools\config\EquipConfig.xlsx"
    hou_equip_consume_file = r"D:\python_tools\config\equipment_info.xlsx"

    txt_to_xlsx(hou_equip_consume_path,hou_equip_consume_file)
    #处理后台数据

    hou_equip_consume_config = xlrd.open_workbook(hou_equip_consume_file)
    hou_table = hou_equip_consume_config.sheets()[0]

    hou_data = {}
    hou_value_1 = []
    hou_value_2 = []
    hou_value_3 = []
    hou_value_4 = []
    hou_value_5 = []
    for n in range(13,(hou_table.nrows-5)):
        hou_tmp = str(hou_table.cell_value(n, 0).replace('\n','').replace(' ', '').replace('{','').replace('}','').replace('[','').replace(']','')).split(',')
        #print(hou_tmp)
        if hou_tmp[0] == '1':
            hou_value_1.append(hou_tmp[3])
        if hou_tmp[0] == '2':
            hou_value_2.append(hou_tmp[3])
        if hou_tmp[0] == '3':
            hou_value_3.append(hou_tmp[3])
        if hou_tmp[0] == '4':
            hou_value_4.append(hou_tmp[3])
        if hou_tmp[0] == '5':
            hou_value_5.append(hou_tmp[3])
    hou_data[1] = hou_value_1
    hou_data[2] = hou_value_2
    hou_data[3] = hou_value_3
    hou_data[4] = hou_value_4
    hou_data[5] = hou_value_5


    #{1: ['60', '72', '84', '108', '120', '144', '156', '163', '232', '319', '425', '552', '702', '876', '1078', '1309', '1570', '1863', '2192', '2556'],

    #处理前台数据
    txt_to_xlsx(qian_equip_consume_path,qian_equip_consume_file)
    qian_equip_consume_config = xlrd.open_workbook(qian_equip_consume_file)
    qian_table = qian_equip_consume_config.sheets()[0]

    qian_data = {}
    for m in range(3,qian_table.nrows):
        qian_id = qian_table.cell_value(m,0)
        qian_quality = qian_table.cell_value(m,2)
        qian_value_tmp = str(qian_table.cell_value(m,17)).split('+')
        qian_value = {}
        qian_value_num = []
        for value in range(1,len(qian_value_tmp)):
            qian_value_num.append(qian_value_tmp[value])
        qian_value[qian_quality] = qian_value_num
        qian_data[qian_id] = qian_value

    print(hou_data)
    print(qian_data)
    result_list = []
    for data_value in qian_data.values():
        for key,value in data_value.items():
           # print(value)
            assert value == hou_data[int(key)]
    #         if not value == hou_data[int(key)]:
    #             result_list.append(value)
    # if result_list:
    #     print(result_list)
    # else:
    #     print("装备强化消耗前后配置一致！")

