import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result

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
