import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result

qian_chapter_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Level\ChapterConfig.txt"
hou_chapter_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\duplicate.cfg"
qian_chapter_file = r"D:\python_tools\config\ChapterConfig.xlsx"
hou_chapter_file = r"D:\python_tools\config\duplicate.xlsx"

#处理前台数据
txt_to_xlsx(qian_chapter_path,qian_chapter_file)
qian_chapter_config = xlrd.open_workbook(qian_chapter_file)
table_qian = qian_chapter_config.sheets()[0]

qian_data = {}

for n in range(3,table_qian.nrows):
    qian_id = table_qian.cell_value(n,0)
    qian_value = {}
    qian_value.update(con = table_qian.cell_value(n,4).split("+"))
    qian_value.update(value = table_qian.cell_value(n,5).split("+"))
    qian_data[qian_id] = qian_value
print(qian_data)


#处理后台数据

txt_to_xlsx(hou_chapter_path,hou_chapter_file)
hou_chapter_config = xlrd.open_workbook(hou_chapter_file)
table_hou = hou_chapter_config.sheets()[0]

hou_data = {}
num = {}
for m in range(table_hou.nrows):
    hou_num = table_hou.cell_value(m,0).replace(' ','')
    if hou_num.startswith('%%关卡星星奖励'):
        num['start'] = m + 6
    num['stop'] = table_hou.nrows - 8


for num in range(num['start'],num['stop']):
    hou_tmp = str(table_hou.cell_value(num, 0).replace(' ', '').replace('{', '').replace('}', '').replace('[', '').replace(']','').replace('\n', '')).split(',')
    hou_id = hou_tmp[0]
    hou_con = []
    hou_value = []
    hou_data_tmp = {}
    for num1 in range(len(hou_tmp)):
        if num1 in [1,3,5]:
            hou_con.append(hou_tmp[num1])
        if num1 in [2,4,6]:
            hou_value.append(hou_tmp[num1])
    hou_data_tmp.update(con = hou_con)
    hou_data_tmp.update(value = hou_value)
    hou_data[hou_id] = hou_data_tmp
print(hou_data)


check_config_result(qian_data,hou_data)
#"副本章节奖励前后配置一致"