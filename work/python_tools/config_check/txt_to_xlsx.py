import xlwt


def txt_to_xlsx(file_txt_path,file_xlsx_name):
    try:
        file_txt = open(file_txt_path,'r',encoding='utf-8')
        file_xlsx = xlwt.Workbook()
        sheet = file_xlsx.add_sheet('shee1',cell_overwrite_ok=True)
        x = 0
        while True:
                #按行循环，读取文本文件
            line = file_txt.readline()
            if not line:
                break  #如果没有内容，则退出循环
            for i in range(len(line.split('\t'))):
                item = line.split('\t')[i]      #replace('\t','').
                sheet.write(x,i,item)  #x单元格经度，i单元格纬度
            x += 1          #excel另起一行
        file_txt.close()
        file_xlsx.save(file_xlsx_name)
        #print("保存成功！")
    except:
        raise