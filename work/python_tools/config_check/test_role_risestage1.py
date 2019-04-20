import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx


qian_role_risestage_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Role\RiseStageConfig.txt"
hou_role_risestage_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\card_info.cfg"
qian_role_resestage_file = r"D:\python_tools\config\RiseStageConfig.xlsx"
hou_role_resestage_file = r"D:\python_tools\config\card_info.xlsx"

txt_to_xlsx(qian_role_risestage_path,qian_role_resestage_file)
#处理前台数据

qian_data = {}
qian_role_risestage_config = xlrd.open_workbook(qian_role_resestage_file)
table_qian = qian_role_risestage_config.sheets()[0]

for n in range(3,table_qian.nrows):
    qian_id = table_qian.cell_value(n,0)
    qian_value = {}
    qian_value.update(money = table_qian.cell_value(n,12))
    qian_value.update(cellstage = table_qian.cell_value(n,13).split('+'))
    qian_data[qian_id] = qian_value
print(qian_data)

#处理后台数据

hou_data = {}
txt_to_xlsx(hou_role_risestage_path,hou_role_resestage_file)
hou_role_risestage_config = xlrd.open_workbook(hou_role_resestage_file)
table_hou = hou_role_risestage_config.sheets()[0]

num = {}
for m in range(table_hou.nrows):
    hou_num = table_hou.cell_value(m,0).replace(' ','')
    if hou_num.startswith('%%武将卡牌升阶条件消耗'):
        num['start'] = m + 8
    if hou_num.startswith('%%阶格消耗'):
        num['stop'] = m - 6
result_list = []
for num in range(num['start'],num['stop']):
    hou_tmp = str(table_hou.cell_value(num, 0).replace(' ', '').replace('{', '').replace('}', '').replace('[', '').replace(']','').replace('\n', '')).split(',')
    if hou_tmp[1] == '15':
        continue
    hou_id = int(hou_tmp[2])//1000 * 100 + int(hou_tmp[1]) + 1
    #print(hou_id)
    hou_value = {}
    hou_value.update(cellstage =[hou_tmp[n] for n in range(2, 6)])
    hou_value.update(money = hou_tmp[9])
    assert qian_data[str(hou_id)] == hou_value
    #print(hou_value)
#     if qian_data[str(hou_id)] != hou_value:
#         result_list.append('{},{}'.format(hou_tmp[0],hou_tmp[1]))
#
#
# if result_list:
#     print("英雄升阶消耗和前置条件前后配置不一致")
#     print("不一致的有{}.format(result_list)")
# else:
#     print("英雄升阶消耗和前置条件前后配置一致")

#验证升阶线路是否正确
