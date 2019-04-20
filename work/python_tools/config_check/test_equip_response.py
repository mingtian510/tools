import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result
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
    print(hou_data)

    check_config_result(qian_data,hou_data)