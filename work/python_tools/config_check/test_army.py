import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result

def test_army_quality():
    qian_quality_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Army\HeroArmyConfig.txt"
    hou_quality_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\card_info.cfg"
    qian_quality_file = r"D:\python_tools\config\HeroArmyConfig.xlsx"
    hou_quality_file = r"D:\python_tools\config\card_info.xlsx"
    #处理前台数据
    txt_to_xlsx(qian_quality_path,qian_quality_file)
    qian_quality_config = xlrd.open_workbook(qian_quality_file)
    table_qian = qian_quality_config.sheets()[0]
    qian_data ={}
    for n in range(3,table_qian.nrows):
        qian_sid = table_qian.cell_value(n,0)
        qian_tmp1 = table_qian.cell_value(n,12).split('|')
        qian_tmp = qian_tmp1[:-1]
        qian_data[qian_sid] = qian_tmp
    print(qian_data)
    #处理后台数据
    txt_to_xlsx(hou_quality_path,hou_quality_file)
    hou_quality_config = xlrd.open_workbook(hou_quality_file)
    table_hou = hou_quality_config.sheets()[0]
    hou_data = {}
    num = {}
    for m in range(table_hou.nrows):
        if table_hou.cell_value(m, 0).startswith("    [card_up_soldiers_quality,"):
            num['start'] = m + 3
        if table_hou.cell_value(m, 0).startswith("    [soldier_attr,"):
            num['stop'] = m - 6
            break
    hou_value1 = {}
    for num in range(num['start'], num['stop']):
        hou_value2 = []
        hou_tmp = table_hou.cell_value(num, 0).replace(' ', '').replace('\n', '').replace('{', '').replace('}','').replace('[', '').replace(']', '').split(',')
        #print(hou_index)
        qua = hou_tmp[1]
        if qua == '15': #去掉15阶的错误数据
            continue
        hou_index = [index for index in range(len(hou_tmp)) if hou_tmp[index] == 'prop']
        for x in hou_index:
            hou_value2.append(str(hou_tmp[int(x) + 1]))
            hou_value2.append(str(hou_tmp[int(x) + 2]))
        hou_value1[qua] = hou_value2
        #print(hou_value1)
        if qua == '14':
            hou_data[hou_tmp[0]] = hou_value1
            hou_value1 = {}
    print(hou_data)
    #assert断言
    for key in hou_data:
        key1 = qian_data[key]
        for value1 in key1:
            value1_tmp = value1.split('+')
            # print(key)
            # print(value1_tmp[1::])
            # print(hou_data[key][value1_tmp[0]])
            assert hou_data[key][value1_tmp[0]] == value1_tmp[1::]
#test_army_quality()

def test_army_upgrade():#配置表是有一定问题的，但由于所有资质经验值都相同，所以暂时没有问题
    qian_army_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Army\ArmyExpConfig.txt"
    hou_army_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\game_info.cfg"
    qian_army_file = r"D:\python_tools\config\ArmyExpConfig.xlsx"
    hou_army_file = r"D:\python_tools\config\game_info.xlsx"
    #处理前台数据
    txt_to_xlsx(qian_army_path,qian_army_file)
    qian_army_config = xlrd.open_workbook(qian_army_file)
    table_qian = qian_army_config.sheets()[0]
    qian_data ={}
    for m in range(2, 7):
        zizhi = table_qian.cell_value(2, m)[3:]
        value = []
        for n in range(4,table_qian.nrows):
            value.append(table_qian.cell_value(n, m))
            qian_data[zizhi] = value
    #print(qian_data)
    #处理后台数据
    txt_to_xlsx(hou_army_path,hou_army_file)
    hou_army_config = xlrd.open_workbook(hou_army_file)
    table_hou = hou_army_config.sheets()[0]
    hou_data = {}
    num = {}
    for m in range(table_hou.nrows):
        hou_num = table_hou.cell_value(m,0).replace(' ','')
        if hou_num.startswith('{soldiers_exps,'):
            num['start'] = m + 1
        if hou_num.startswith('{corps_exps'):
            num['stop'] = m - 1
    zizhi = ['60','80','100','110','120']
    pos = 0
    for num1 in range(num['start'], num['stop']):
        if num1 == num['start']:
            hou_value = str(table_hou.cell_value(num1,0).replace(' ', '').replace('{', '').replace('}', '').replace('\n', '')).split(',')
            hou_value1 = [x for x in hou_value if x != '']
            hou_data['40'] = hou_value1
        else:
            hou_tmp = str(table_hou.cell_value(num1, 4).replace(' ', '').replace('{', '').replace('}', '').replace('\n', '')).split(',')
            hou_tmp1 = [x for x in hou_tmp if x != '']
            hou_data[zizhi[pos]] = hou_tmp1
            pos += 1
    #print(hou_data)
    assert qian_data == hou_data

