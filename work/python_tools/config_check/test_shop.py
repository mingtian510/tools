import xlrd
import xlwt
import sys
from txt_to_xlsx import txt_to_xlsx
from check_config_result import check_config_result
"""
步骤：1、将前台配置表ShopGoodsConfig.txt放入config文件夹中。
       2、后台配置表直接将所有商品条目复制到一张表中.取名"shop_list.cfg"
       3、可能会有数据结构不一致的情况，比如月石有第一次半价的设定，需要在前后配置表中将这些配置临时删除掉。已知的有70049
       
"""
itemConfig = {90101:'rmb',90102:'card_soul',90107:'corps_money',90001:'wood',90003:'mineral',90002:'iron',90018:'arena_money'}

txt_to_xlsx("D:/python_tools/config/ShopGoodsConfig.txt","D:/python_tools/config/ShopGoodsConfig.xlsx")
qian_config = xlrd.open_workbook("D:/python_tools/config/ShopGoodsConfig.xlsx")
table = qian_config.sheets()[0]
qian_data = {}

#qian_data ={65001:{'sid':40021,'number':5,'pricetype':90102,'price':150}}##折扣问题，pricetype需要转换

for n in range(3,table.nrows):
    #globals(qian_data)
    qian_id = int(table.cell_value(n,0))
   # qian_value_sid = table.cell_value(n,3)
    qian_value = {}
    qian_value.update(sid=table.cell_value(n,3))
    qian_value.update(number=table.cell_value(n,4))
    qian_value.update(pricetype=table.cell_value(n,5))
    qian_value.update(price=int(
                      (int(table.cell_value(n,6))*(int(table.cell_value(n,8))/10000))//1
                          ))
    #月石前台配置表为130+260暂时未处理，先临时删掉该配置
   # print(qian_value)
    qian_data[qian_id]=qian_value

for value in qian_data.values():
    value.update(pricetype = itemConfig[int(value['pricetype'])])

print(qian_data)

#qian_data为前台最终数据

#后台配置表操作：直接将所有商品条目复制到一张表中.(后台配置表有个七日狂欢卖信物的配置临时删除，格式和其他不一样
txt_to_xlsx("D:/python_tools/config/shop_list.cfg","D:/python_tools/config/shop_list.xlsx")
hou_config = xlrd.open_workbook("D:/python_tools/config/shop_list.xlsx")
table = hou_config.sheets()[0]
hou_data = {}
#处理数据结构
for n in range(table.nrows):
    hou_tmp = str(table.cell_value(n,0).replace(' ','').replace('\n','').replace('{','').replace('}','').replace('[','').replace(']',''))
    hou_tmp_split = hou_tmp.split(',')
    hou_tmp_value = []
    for n in range(len(hou_tmp_split)):
        if n in [0,2,3,4,5]:
            hou_tmp_value.append(hou_tmp_split[n])
    #print(hou_tmp_value)
    hou_value = {}
    hou_value.update(sid = hou_tmp_value[1])
    hou_value.update(number = hou_tmp_value[2])
    hou_value.update(pricetype = hou_tmp_value[3])
    hou_value.update(price = int(hou_tmp_value[4]))
    hou_data[int(hou_tmp_value[0])] = hou_value

print(hou_data)
print("前台配置总条目数量为{}".format(len(qian_data)))
print("后台配置总条目数量为{}".format(len(hou_data)))

check_config_result(qian_data,hou_data)
#"商品前后配置一致"
