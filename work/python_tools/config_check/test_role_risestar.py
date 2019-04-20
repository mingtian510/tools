import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result

def test_role_risestar():
    qian_role_risestar_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Role\RiseStarConfig.txt"
    hou_role_risestar_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\card_info.cfg"
    qian_role_risestar_file = r"D:\python_tools\config\RiseStarConfig.xlsx"
    txt_to_xlsx(qian_role_risestar_path,qian_role_risestar_file)

    qian_role_risestar_config = xlrd.open_workbook(qian_role_risestar_file)
    table_qian = qian_role_risestar_config.sheets()[0]
    qian_data_star = {}
    qian_data_smallstar = {}
    #处理前台配置表
    for n in range(3,table_qian.nrows):
        if table_qian.cell_value(n,0).endswith("11"):   #升星消耗
            #print(table_qian.cell_value(n,0))
            qian_data_star[table_qian.cell_value(n,0)] = table_qian.cell_value(n,9)
        elif table_qian.cell_value(n,0).endswith("00"):
            continue
        else:
            qian_id = table_qian.cell_value(n,0)
            qian_value = {}
            qian_value_tmp = table_qian.cell_value(n,15)
            qian_value.update(sid = qian_value_tmp.split("+")[0])
            qian_value.update(num = qian_value_tmp.split("+")[1].replace('\n',''))
            qian_data_smallstar[qian_id] = qian_value

    #处理后台配置表
    hou_data_star = {}
    hou_data_smallstar = {}

    hou_role_risestar_file = r"D:\python_tools\config\card_info.xlsx"
    txt_to_xlsx(hou_role_risestar_path,hou_role_risestar_file)
    hou_role_risestar_config = xlrd.open_workbook(hou_role_risestar_file)
    table_hou = hou_role_risestar_config.sheets()[0]

    num = {}
    for n in range(table_hou.nrows):
        hou_tmp = str(table_hou.cell_value(n,0).replace(' ',''))
        # print(table_hou.cell_value(n,0))
        if hou_tmp.startswith("[card_up_star,"):
            num.update(start_num = n+3)
        if hou_tmp.startswith("%%武将士兵升阶条件消耗"):
            num.update(stop_num = n-6)

    for m in range(num['start_num'],num['stop_num']):
        hou_tmp1 = str(table_hou.cell_value(m,0).replace(' ','').replace('\n','').replace('{','').replace('}','').replace('[','').replace(']','')).split(',')
        #整理数据格式
        while not hou_tmp1[-1]:
            hou_tmp1.pop()
        hou_tmp1.pop(2)
        if hou_tmp1[1] == '5':
            continue
        hou_data_star[hou_tmp1[0] + str(int(hou_tmp1[1])+1) + '11'] = hou_tmp1[-1]
        #print(prop_num)
        count = 0
        pos = [n for n in range(len(hou_tmp1)) if hou_tmp1[n] == 'prop']
        #print(hou_tmp1)
        for tmp1_value in hou_tmp1:
            if tmp1_value == 'prop':
                count += 1
                hou_data_smallstar_sid = hou_tmp1[0] +str((int(hou_tmp1[1])+1)* 100 + count)
                hou_data_smallstar_value = {}
                hou_data_smallstar_value.update(sid = hou_tmp1[pos[count-1] + 1])
                hou_data_smallstar_value.update(num = hou_tmp1[pos[count-1] + 2])
                hou_data_smallstar[hou_data_smallstar_sid] = hou_data_smallstar_value
    print(qian_data_star)
    print(hou_data_star)
    print(qian_data_smallstar)
    print(hou_data_smallstar)
    # print("前台升星配置总条目数量为{}".format(len(qian_data_star)))
    # print("后台升星配置总条目数量为{}".format(len(hou_data_star)))
    # print("前台激活星格配置总条目数量为{}".format(len(qian_data_smallstar)))
    # print("后台激活星格配置总条目数量为{}".format(len(hou_data_smallstar)))
    # result_list_star = []
    # result_list_smallstar = []

    check_config_result(qian_data_star,hou_data_star)
    #"英雄升星前后配置一致"
    check_config_result(qian_data_smallstar,hou_data_smallstar)
    #"英雄激活星格前后配置一致"

