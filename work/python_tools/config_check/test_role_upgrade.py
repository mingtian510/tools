import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx

def test_role_upgrade():
#英雄升级
    qian_role_exp_path =r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Role\RoleExpConfig.txt"
    hou_role_exp_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\game_info.cfg"
    #hou_role_exp_path = "D:/python_tools/config/game_info.cfg"
    qian_role_exp_file = "D:/python_tools/config/RoleExpConfig.xlsx"
    qian_role_exp=[]
    #处理前台配置表数据
    txt_to_xlsx(qian_role_exp_path,qian_role_exp_file)
    qian_role_exp_config = xlrd.open_workbook(qian_role_exp_file)
    table = qian_role_exp_config.sheets()[0]

    for n in range(4,table.nrows-1):
       # print(table.cell_value(n,1))
        data = int(table.cell_value(n,1))
       # print(data)
        qian_role_exp.append(int(data))

    #处理后台配置表数据
    hou_role_exp_config = open(hou_role_exp_path,'r',encoding='utf-8')
    hou_role_exp = []
    line_hou = hou_role_exp_config.readlines()
    #print(line_hou)
    line_hou1 = []
    for n in line_hou:
        a = n.replace(' ', '')
        line_hou1.append(a)
    #print(line_hou1)
    for n in line_hou1:
        if n.startswith('{card_exps'):
            #print(n)
            tmp = n[12:-4]
            tmp_list = tmp.split(",")
            for m in tmp_list:
                hou_role_exp.append(int(m))

    print("前台英雄等级经验值配置为：{}".format(qian_role_exp))
    print("后台英雄等级经验值配置为：{}".format(hou_role_exp))

    assert qian_role_exp == hou_role_exp
    # if qian_role_exp == hou_role_exp:
    #     print("英雄等级经验值前后一致")
    # else:
    #     print("英雄等级经验值前后不一致！！！")


