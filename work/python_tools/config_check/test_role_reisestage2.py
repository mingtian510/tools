import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx


qian_role_risestage_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Role\RoleConfig.txt"
hou_role_risestage_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\card_info.cfg"
qian_role_resestage_file = r"D:\python_tools\config\RoleConfig.xlsx"
hou_role_resestage_file = r"D:\python_tools\config\card_info.xlsx"

txt_to_xlsx(qian_role_risestage_path,qian_role_resestage_file)
qian_data = {}
qian_role_risestage_config = xlrd.open_workbook(qian_role_resestage_file)
table_qian = qian_role_risestage_config.sheets()[0]

for n in range(3,table_qian.nrows):
    qian_id = table_qian.cell_value(n,0)
    qian_value = table_qian.cell_value(n,21)[2]
    qian_data[qian_id] = qian_value
print(qian_data)
print(len(qian_data))

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

for num in range(num['start'],num['stop']):
    hou_tmp = str(table_hou.cell_value(num, 0).replace(' ', '').replace('{', '').replace('}', '').replace('[', '').replace(']','').replace('\n', '')).split(',')
    hou_id = hou_tmp[0]
    hou_value = hou_tmp[2][0]
    hou_data[hou_id] = hou_value

print(hou_data)
print(len(hou_data))

for key,value in hou_data.items():
    assert value == qian_data[key]
#     if value != qian_data[key]:
#         result_list.append(key)
# if result_list:
#     print("英雄升阶路线前后配置不一致")
#     print("不一致的英雄id为{}".format(result_list))
# else:
#     print("英雄升阶路线前后配置一致")
