import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result

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
    print(qian_data)

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
    print(hou_data)
    check_config_result(qian_data,hou_data)