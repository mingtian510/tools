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




