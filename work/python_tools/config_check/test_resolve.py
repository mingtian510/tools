import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result


def test_resolve1():
    qian_resolve1_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Role\RoleConfig.txt"
    hou_resolve1_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\resolve_info.cfg"
    qian_resolve1_file = r"D:\python_tools\config\RoleConfig.xlsx"
    hou_resolve1_file = r"D:\python_tools\config\resolve_info.xlsx"
    # 处理前台数据
    txt_to_xlsx(qian_resolve1_path, qian_resolve1_file)
    qian_resolve1_config = xlrd.open_workbook(qian_resolve1_file)
    table_qian = qian_resolve1_config.sheets()[0]
    qian_data = {}
    for n in range(3, table_qian.nrows):
        qian_sid = table_qian.cell_value(n, 0)
        qian_value = table_qian.cell_value(n,32)
        qian_data[qian_sid] = qian_value
    print(qian_data)

    #处理后台数据
    txt_to_xlsx(hou_resolve1_path,hou_resolve1_file)
    hou_resolve1_config = xlrd.open_workbook(hou_resolve1_file)
    table_hou = hou_resolve1_config.sheets()[0]
    hou_data = {}

    num = {}
    for n in range(table_hou.nrows):
        hou_tmp = str(table_hou.cell_value(n, 0).replace(' ', ''))
        if hou_tmp.startswith("%武将分解"):
            num.update(start_num = n + 5)
        if hou_tmp.startswith("%%获得同名卡牌转换成碎片数量"):
            num.update(stop_num = n - 6)

    for m in range(num['start_num'], num['stop_num']):
        hou_tmp1 =str(table_hou.cell_value(m, 0).replace(' ', '').replace('\n', '').replace('{', '').replace('}', '').replace('[',    '').replace(']', '')).split(',')
        hou_sid = hou_tmp1[0]
        hou_value = hou_tmp1[2]
        hou_data[hou_sid] = hou_value
    print(hou_data)
    for key in hou_data.keys():
        assert hou_data[key] == qian_data[key]

def test_resolve2():
    qian_resolve2_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Equipment\EquipConfig.txt"
    hou_resolve2_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\resolve_info.cfg"
    qian_resolve2_file = r"D:\python_tools\config\EquipmentConfig.xlsx"
    hou_resolve2_file = r"D:\python_tools\config\resolve_info.xlsx"
    # 处理前台数据
    txt_to_xlsx(qian_resolve2_path,qian_resolve2_file)
    qian_resolve2_config = xlrd.open_workbook(qian_resolve2_file)
    table_qian = qian_resolve2_config.sheets()[0]
    qian_data ={}

    for n in range(3, table_qian.nrows):
        qian_sid = table_qian.cell_value(n, 0)
        qian_value = table_qian.cell_value(n,13)
        qian_data[qian_sid] = qian_value
    print(qian_data)
    #处理后台数据
    txt_to_xlsx(hou_resolve2_path, hou_resolve2_file)
    hou_resolve1_config = xlrd.open_workbook(hou_resolve2_file)
    table_hou = hou_resolve1_config.sheets()[0]
    hou_data = {}

    num = {}
    for n in range(table_hou.nrows):
        hou_tmp = str(table_hou.cell_value(n, 0).replace(' ', ''))
        if hou_tmp.startswith("%%装备分解"):
            num.update(start_num = n + 5)
        if hou_tmp.startswith("%武将分解"):
            num.update(stop_num = n - 4)

    for m in range(num['start_num'], num['stop_num']):
        hou_tmp1 = str(table_hou.cell_value(m, 0).replace(' ', '').replace('\n', '').replace('{', '').replace('}', '').replace('[','').replace(']', '')).split(',')
        hou_sid = hou_tmp1[0]
        hou_value = str(hou_tmp1[2] + "+" + hou_tmp1[3])
        hou_data[hou_sid] = hou_value
    print(hou_data)
    for key in hou_data.keys():
        assert hou_data[key] == qian_data[key]

def test_resolve3():
    qian_resolve3_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\CompoundFragmentConfig.txt"
    hou_resolve3_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\resolve_info.cfg"
    qian_resolve3_file = r"D:\python_tools\config\CompoundFragmentConfig.xlsx"
    hou_resolve3_file = r"D:\python_tools\config\resolve_info.xlsx"
    # 处理前台数据
    txt_to_xlsx(qian_resolve3_path, qian_resolve3_file)
    qian_resolve1_config = xlrd.open_workbook(qian_resolve3_file)
    table_qian = qian_resolve1_config.sheets()[0]
    qian_data = {}
    for n in range(3, table_qian.nrows):
        qian_sid = table_qian.cell_value(n, 0)
        qian_value = table_qian.cell_value(n, 1).strip()
        qian_data[qian_sid] = qian_value
    print(qian_data)

    #处理后台数据
    txt_to_xlsx(hou_resolve3_path, hou_resolve3_file)
    hou_resolve1_config = xlrd.open_workbook(hou_resolve3_file)
    table_hou = hou_resolve1_config.sheets()[0]
    hou_data = {}

    num = {}
    for n in range(table_hou.nrows):
        hou_tmp = str(table_hou.cell_value(n, 0).replace(' ', ''))
        if hou_tmp.startswith("%碎片分解转换信物"):
            num.update(start_num= n + 5)
        # if hou_tmp.startswith("%%获得同名卡牌转换成碎片数量"):
        #     num.update(stop_num= n - 6)

    for m in range(num['start_num'], table_hou.nrows - 5):
        hou_tmp1 = str(
            table_hou.cell_value(m, 0).replace(' ', '').replace('\n', '').replace('{', '').replace('}', '').replace('[','').replace(']', '')).split(',')
        hou_sid = hou_tmp1[0]
        hou_value = hou_tmp1[2]
        hou_data[hou_sid] = hou_value
    print(hou_data)
    check_config_result(qian_data,hou_data)
