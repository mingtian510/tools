import xlrd
import xlwt
import sys
import configparser
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result
def test_role_risestage():
    qian_role_risestage_path = r"F:\jiuzhou\code\int\Unity\Assets\Resources\Config\Game\Role\RiseStageCellConfig.txt"
    hou_role_risestage_path = r"F:\jiuzhou\后台\code\int\plugin\game\.cfg\card_info.cfg"
    #处理前台数据
    qian_role_risestage_file = "D:/python_tools/config/RiseStageCellConfig.xlsx"
    txt_to_xlsx(qian_role_risestage_path,qian_role_risestage_file)
    qian_role_risestage_config = xlrd.open_workbook(qian_role_risestage_file)
    table = qian_role_risestage_config.sheets()[0]
    qian_data = {}
    #qian_data = {1001:{'money':60,'price':['41000+1','41001+1']}}
    for n in range(3,table.nrows):
        if not table.cell_value(n,4):
            continue
        else:
            qian_id = table.cell_value(n,0)
            qian_value ={}
            qian_value.update(money=table.cell_value(n,3))
            qian_value_tmp = table.cell_value(n,4)
            qian_value.update(price=qian_value_tmp.split("|"))
            qian_data[qian_id] = qian_value

    #print(len(qian_data))
    #处理后台数据

    hou_role_risestage_file = "D:/python_tools/config/card_info.xlsx"
    txt_to_xlsx(hou_role_risestage_path,hou_role_risestage_file)
    hou_role_risestage_config = xlrd.open_workbook(hou_role_risestage_file)
    table_hou = hou_role_risestage_config.sheets()[0]
    hou_data = {}
    num = {}

    for n in range(table_hou.nrows):
        hou_tmp = str(table_hou.cell_value(n,0).replace(' ',''))
        # print(table_hou.cell_value(n,0))
        if hou_tmp.startswith("[card_quality_grid,"):
            num.update(start_num = n+3)
        if hou_tmp.startswith("%%武将升星"):
            num.update(stop_num = n-4)

    #print(num)
    for m in range(num['start_num'],num['stop_num']):
        # print(table_hou.cell_value(m,0))
        hou_tmp1 = str(table_hou.cell_value(m,0).replace(' ','').replace('\n','').replace('{','[').replace('}',']').replace('[','').replace(']','')).split(',') #.replace('prop,','')
        #print(hou_tmp1)
        if not hou_tmp1[1]:
            continue
        hou_tmp_value = []
        for n in range(len(hou_tmp1)):
            if n in [0,2,3,5,6,8]:
                hou_tmp_value.append(hou_tmp1[n])
        #print(hou_tmp_value)
        hou_data_value = {}
        hou_data_sid = hou_tmp_value[0]
        hou_data_value.update(price = [str(hou_tmp_value[1]+"+"+hou_tmp_value[2]),str(hou_tmp_value[3]+"+"+hou_tmp_value[4])])
        hou_data_value.update(money = str(hou_tmp_value[5]))
        hou_data[hou_data_sid] = hou_data_value
    print(qian_data)
    print(hou_data)
    print("前台配置总条目数量为{}".format(len(qian_data)))
    print("后台配置总条目数量为{}".format(len(hou_data)))

    check_config_result(qian_data,hou_data)
    #"英雄激活命格消耗前后配置一致"