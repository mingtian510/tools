import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result

def test_equip_basic():
    qian_equip_basic_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Equipment\EquipConfig.txt"
    hou_equip_basic_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\equipment.cfg"
    qian_equip_basic_file = r"D:\python_tools\config\EquipResponseConfig.xlsx"
    hou_equip_basic_file = r"D:\python_tools\config\equipment.xlsx"

    # 处理前台数据
    txt_to_xlsx(qian_equip_basic_path, qian_equip_basic_file)
    qian_equip_basic_config = xlrd.open_workbook(qian_equip_basic_file)
    table_qian = qian_equip_basic_config.sheets()[0]
    qian_data = {}
    for n in range(3,table_qian.nrows):
        qian_value = table_qian.cell_value(n,15).split('+')[2]
        print(qian_value)
        qian_data[table_qian.cell_value(n,0)] = qian_value
    #print(qian_data)

    #处理后台数据
    txt_to_xlsx(hou_equip_basic_path,hou_equip_basic_file)
    hou_equip_basic_config = xlrd.open_workbook(hou_equip_basic_file)
    table_hou = hou_equip_basic_config.sheets()[0]
    hou_data = {}
    num ={}
    for m in range(table_hou.nrows):
        if table_hou.cell_value(m,0).startswith("{[gateway], zm_config"):
            num['start'] = m + 4
        if table_hou.cell_value(m,0).startswith("], [{keypos,2}]"):
            num['stop'] = m - 2
            break
    for num in range(num['start'],num['stop']):
        hou_tmp = table_hou.cell_value(num, 0).replace(' ', '').replace('\n', '').replace('{', '').replace('}','').replace('[', '').replace(']', '').split(',')
        hou_value = hou_tmp[14]
        hou_data[hou_tmp[1]] = hou_value
    # print(hou_data)
    check_config_result(qian_data,hou_data)

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
    result_list = []
    for data_value in qian_data.values():
        for key,value in data_value.items():
            assert value == hou_data[int(key)]

def test_equip_promote():
    qian_equip_promote_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Equipment\EquipConfig.txt"
    hou_equip_promote_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\attrs_equipment.cfg"
    qian_equip_promote_file = r"D:\python_tools\config\EquipResponseConfig.xlsx"
    hou_equip_promote_file = r"D:\python_tools\config\attrs_equipment.xlsx"
    # 处理前台数据
    txt_to_xlsx(qian_equip_promote_path, qian_equip_promote_file)
    qian_equip_basic_config = xlrd.open_workbook(qian_equip_promote_file)
    table_qian = qian_equip_basic_config.sheets()[0]
    qian_data = {}
    for n in range(3,table_qian.nrows):
        qian_value = table_qian.cell_value(n,16).split('+')[2]
        #print(qian_value)
        qian_data[table_qian.cell_value(n,2) + table_qian.cell_value(n,1)] = qian_value
    # 处理后台数据
    txt_to_xlsx(hou_equip_promote_path, hou_equip_promote_file)
    hou_equip_basic_config = xlrd.open_workbook(hou_equip_promote_file)
    table_hou = hou_equip_basic_config.sheets()[0]
    hou_data = {}
    num = {}
    for m in range(table_hou.nrows):
        if table_hou.cell_value(m, 0).startswith("    [equipment_streng_attr"):
            num['start'] = m + 4
        if table_hou.cell_value(m, 0).startswith("        ], [{keypos, 1}]"):
            num['stop'] = m
            break
    #print(num)
    for num in range(num['start'], num['stop']):
        hou_tmp = table_hou.cell_value(num, 0).replace(' ', '').replace('\n', '').replace('{', '').replace('}','').replace('[', '').replace(']', '').split(',')
        hou_value = hou_tmp[5]
        hou_data[hou_tmp[0] + hou_tmp[1]] = hou_value
    #print(hou_data)
    check_config_result(qian_data, hou_data)

def test_equip_resolve():
    qian_equip_resolve_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Equipment\EquipConfig.txt"
    hou_equip_resolve_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\resolve_info.cfg"
    qian_equip_resolve_file = r"D:\python_tools\config\EquipConfig.xlsx"
    hou_equip_resolve_file = r"D:\python_tools\config\resolve_info.xlsx"
    #处理前台数据
    txt_to_xlsx(qian_equip_resolve_path,qian_equip_resolve_file)
    qian_equip_resolve_config = xlrd.open_workbook(qian_equip_resolve_file)
    table_qian = qian_equip_resolve_config.sheets()[0]
    qian_data = {}
    for n in range(3,table_qian.nrows):
        qian_id = table_qian.cell_value(n,0)
        qian_value = {}
        qian_tmp = table_qian.cell_value(n,13).split('+')
        qian_value.update(sid = qian_tmp[0])
        qian_value.update(num = qian_tmp[1])
        qian_data[qian_id] = qian_value
    #处理后台数据
    txt_to_xlsx(hou_equip_resolve_path,hou_equip_resolve_file)
    hou_equip_resolve_config = xlrd.open_workbook(hou_equip_resolve_file)
    table_hou = hou_equip_resolve_config.sheets()[0]
    hou_data ={}
    num = {}
    for m in range(table_hou.nrows):
        hou_num = table_hou.cell_value(m,0).replace(' ','')
        if hou_num.startswith('%%装备分解'):
            num['start'] = m + 5
        if hou_num.startswith('%武将分解'):
            num['stop'] = m - 4
    for num in range(num['start'],num['stop']):
        hou_tmp = str(table_hou.cell_value(num,0).replace(' ','').replace('{','').replace('}','').replace('[','').replace(']','').replace('\n','')).split(',')
        hou_value = {}
        hou_id = hou_tmp[0]
        hou_value.update(sid = hou_tmp[2])
        hou_value.update(num = hou_tmp[3])
        hou_data[hou_id] = hou_value
    check_config_result(qian_data,hou_data)

def test_equip_response():
    qian_equip_response_path =r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Equipment\EquipResponseConfig.txt"
    hou_equip_response_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\attrs_equipment.cfg"
    qian_equip_response_file = r"D:\python_tools\config\EquipResponseConfig.xlsx"
    hou_equip_response_file = r"D:\python_tools\config\attrs_equipment.xlsx"
    #处理前台数据
    txt_to_xlsx(qian_equip_response_path,qian_equip_response_file)
    qian_equip_response_config = xlrd.open_workbook(qian_equip_response_file)
    qian_table = qian_equip_response_config.sheets()[0]
    qian_data = {}
    for n in range(3,qian_table.nrows):
        qian_lv = qian_table.cell_value(n,1)
        qian_value = []
        qian_value_tmp = qian_table.cell_value(n,3).replace("\n","").split("|")
        for value_tmp in qian_value_tmp:
            qian_value.append(value_tmp.split("+")[2])
        qian_data[qian_lv] = qian_value
    print(qian_data)
    #处理后台数据
    txt_to_xlsx(hou_equip_response_path,hou_equip_response_file)
    hou_equip_response_config = xlrd.open_workbook(hou_equip_response_file)
    hou_table = hou_equip_response_config.sheets()[0]
    hou_data = {}
    num = {}
    for m in range(hou_table.nrows):
        hou_num = hou_table.cell_value(m,0).replace(' ','')
        if hou_num.startswith('%装备共鸣属性'):
            num['start'] = m + 4
            num['stop'] = m + 10
    #print(num)
    for num in range(num['start'],num['stop']):
        hou_tmp = hou_table.cell_value(num,0).replace(' ','').replace('\n','').replace('{','').replace('}','').replace('[','').replace(']','').split(',')
        #print(hou_tmp)
        hou_value = []
        hou_value.append(hou_tmp[4])
        hou_value.append(hou_tmp[7])
        hou_data[hou_tmp[0]] = hou_value
    check_config_result(qian_data,hou_data)