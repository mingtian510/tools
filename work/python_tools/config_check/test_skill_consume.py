import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx


qian_skill_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Skill\SkillConfig.txt"
hou_skill_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\card_skill.cfg"
qian_skill_file = r"D:\python_tools\config\SkillConfig.xlsx"
hou_skill_file = r"D:\python_tools\config\card_skill.xlsx"
#处理前台数据
txt_to_xlsx(qian_skill_path,qian_skill_file)
qian_skill_config = xlrd.open_workbook(qian_skill_file)
table_qian = qian_skill_config.sheets()[0]
qian_data = {}

for n in range(3,table_qian.nrows):
    qian_id = table_qian.cell_value(n,0)
    qian_value = table_qian.cell_value(n,6).split('|')
    del qian_value[0]
    qian_data[qian_id] = qian_value
print(qian_data)
print(len(qian_data))

#处理后台数据
txt_to_xlsx(hou_skill_path,hou_skill_file)
hou_skill_config = xlrd.open_workbook(hou_skill_file)
table_hou = hou_skill_config.sheets()[0]
hou_data = {}

for n in range(6,(table_hou.nrows-4)):
    hou_tmp = str(table_hou.cell_value(n, 0).replace(' ', '').replace('{', '').replace('}', '').replace('[', '').replace(']','').replace('\n', '')).split(',')
    #print(hou_tmp)
    index = [i for i, x in enumerate(hou_tmp) if x == 'prop']
    hou_id = hou_tmp[0]
    hou_value = []
    for num in index:
        hou_value.append(hou_tmp[num+1]+ '+' +hou_tmp[num+2])
    hou_data[hou_id] = hou_value
print(hou_data)
print(len(hou_data))
result_list = []
for key,value in hou_data.items():
    assert value == qian_data[key]
#     if value != qian_data[key]:
#         result_list.append(key)
# if result_list:
#     print("英雄技能消耗前后配置不一致")
#     print("不一致的技能id为{}".format(result_list))
# else:
#     print("英雄技能消耗前后配置一致")