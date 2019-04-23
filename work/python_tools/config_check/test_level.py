import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result

def test_level_chapter():
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

def level_consume():
    qian_level_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Level\LevelConfig.txt"
    hou_level_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\duplicate.cfg"
    qian_level_file = r"D:\python_tools\config\LevelConfig.xlsx"
    hou_level_file = r"D:\python_tools\config\duplicate.xlsx"
    #处理前台数据
    txt_to_xlsx(qian_level_path,qian_level_file)
    qian_level_config = xlrd.open_workbook(qian_level_file)
    table_qian = qian_level_config.sheets()[0]
    qian_data ={}
    for n in range(3,table_qian.nrows):
        if int(table_qian.cell_value(n,1)) + int(table_qian.cell_value(n,2)) == 0:
            continue
        qian_id = table_qian.cell_value(n,0)
        qian_value = {}
        qian_stength = table_qian.cell_value(n,21)
        qian_maxtime = table_qian.cell_value(n,22)
        qian_cost = table_qian.cell_value(n,23).split('+')
        qian_value.update(stength = qian_stength)
        qian_value.update(maxtime = qian_maxtime)
        #qian_value.update(cost = qian_cost)
        qian_data[qian_id] = qian_value
    print(qian_data)
    #print(len(qian_data))
    #处理后台数据
    txt_to_xlsx(hou_level_path,hou_level_file)
    hou_level_config = xlrd.open_workbook(hou_level_file)
    table_hou = hou_level_config.sheets()[0]
    hou_data ={}
    num = {}
    for m in range(table_hou.nrows):
        hou_num = table_hou.cell_value(m,0).replace(' ','')
        if hou_num.startswith('[duplicate,'):
            num['start_level'] = m + 4
        if hou_num.startswith('%%todo张斯阳测试配置普通副本第一章'):
            num['stop_level'] = m - 2
        if hou_num.startswith('[duplicate_reset'):
            num['start_reset'] = m + 2
        if hou_num.startswith('%%关卡扫荡'):
            num['stop_reset'] = m - 6

    hou_tmp_520110 = table_hou.cell_value(num['start_level'],3).replace(' ', '').replace('\n', '').replace('{', '').replace('}', '').replace('[', '').replace(']', '').split(',')
    hou_id = hou_tmp_520110[0]
    stength_index = hou_tmp_520110.index('pve')
    maxtime_index = hou_tmp_520110.index('day_num')
    hou_value = {}
    hou_value.update(stength=hou_tmp_520110[stength_index + 1])
    hou_value.update(maxtime=hou_tmp_520110[maxtime_index + 2])
    hou_data[hou_id] = hou_value

    for level_num in range(num['start_level']+ 1,num['stop_level']):
        hou_tmp_level = table_hou.cell_value(level_num, 0).replace(' ', '').replace('\n', '').replace('{', '').replace('}', '').replace('[', '').replace(']', '').split(',')
        if len(hou_tmp_level) == 1:
            continue
        #print(hou_tmp_level)
        hou_id = hou_tmp_level[0]
        if hou_id[4] in ['6','7']:
            stength_index = hou_tmp_level.index('pve')
            maxtime_index = hou_tmp_level.index('forever_num')
            hou_value = {}
            hou_value.update(stength = hou_tmp_level[stength_index + 1])
            hou_value.update(maxtime=hou_tmp_level[maxtime_index + 1])
        else:
            stength_index = hou_tmp_level.index('pve')
            maxtime_index = hou_tmp_level.index('day_num')
            hou_value = {}
            hou_value.update(stength = hou_tmp_level[stength_index + 1])
            hou_value.update(maxtime = hou_tmp_level[maxtime_index + 2] )
        hou_data[hou_id] = hou_value

    #处理后台重置副本消耗数据
    # hou_cost_tmp = table_hou.cell_value(num['start_reset'],0).replace(' ', '').replace('\n', '').replace('{', '').replace('}', '').replace('[', '').replace(']', '').split(',')
    #
    # for key,value in hou_data.items():
    #     if key[4] in ['6','7']:
    #         continue
    #     elif key[1] == '2':
    #         table_hou.cell_value(num['start_reset'],0)
    print(hou_data)
    #print(len(hou_data))
    check_config_result(qian_data,hou_data)
#"副本前后体力消耗和最大挑战次数配置一致"